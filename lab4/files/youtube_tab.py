import tkinter as tk
from tkinter import ttk, messagebox
import yt_dlp as ytdlp
from plyer import notification
import requests
import threading

YOUTUBE_API_KEY = "AIzaSyAClAIfN2WoHaC5NsVk8i0CR4GmRTFUy4o"
BASE_YOUTUBE_URL = "https://www.youtube.com/watch?v="


class YouTubeMonitorTab:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.channel_input = tk.StringVar()
        self.video_list = []
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.frame, text="Моніторинг YouTube-каналу", font=("Arial", 14)).pack(pady=10)
        ttk.Label(self.frame, text="Введіть @username або ID каналу:").pack(pady=5)
        ttk.Entry(self.frame, textvariable=self.channel_input, width=50).pack(pady=5)
        ttk.Button(self.frame, text="Перевірити нові відео", command=self.check_videos).pack(pady=5)

        # Додавання таблиці для відображення відео
        self.video_tree = ttk.Treeview(self.frame, columns=("title", "date", "link"), show="headings", height=10)
        self.video_tree.heading("title", text="Назва")
        self.video_tree.heading("date", text="Дата")
        self.video_tree.heading("link", text="Посилання")
        self.video_tree.column("title", width=300)
        self.video_tree.column("date", width=100)
        self.video_tree.column("link", width=250)
        self.video_tree.pack(pady=10)

        ttk.Button(self.frame, text="Завантажити вибране відео", command=self.download_video).pack(pady=5)

        ttk.Label(self.frame, text="Введіть URL відео YouTube:").pack(pady=5)
        self.url_input = tk.StringVar()
        ttk.Entry(self.frame, textvariable=self.url_input, width=50).pack(pady=5)
        ttk.Button(self.frame, text="Завантажити відео за URL", command=self.download_video_from_url).pack(pady=5)

    def get_channel_id(self, input_value):
        """Визначає channelId за псевдонімом (@username) або повертає введений ID."""
        if input_value.startswith("@"):
            url = f"https://www.googleapis.com/youtube/v3/channels?part=id&forUsername={input_value[1:]}&key={YOUTUBE_API_KEY}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if "items" in data and len(data["items"]) > 0:
                    return data["items"][0]["id"]
                else:
                    messagebox.showerror("Помилка", "Не вдалося знайти канал за псевдонімом!")
            else:
                messagebox.showerror("Помилка", "Помилка доступу до API!")
        else:
            return input_value  # Якщо це ID каналу

        return None

    def check_videos(self):
        user_input = self.channel_input.get().strip()
        if not user_input:
            messagebox.showerror("Помилка", "Будь ласка, введіть @username або ID каналу!")
            return

        # Отримуємо channelId
        channel_id = self.get_channel_id(user_input)
        if not channel_id:
            return


        url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={channel_id}&key={YOUTUBE_API_KEY}"
        response = requests.get(url)

        if response.status_code != 200:
            messagebox.showerror("Помилка", "Не вдалося отримати ID плейлиста!")
            return

        playlist_data = response.json()
        try:
            uploads_playlist_id = playlist_data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
        except (KeyError, IndexError):
            messagebox.showerror("Помилка", "Не вдалося знайти плейлист завантажених відео!")
            return


        videos = []
        next_page_token = None
        while True:
            url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={uploads_playlist_id}&maxResults=10&key={YOUTUBE_API_KEY}"
            if next_page_token:
                url += f"&pageToken={next_page_token}"

            response = requests.get(url)

            if response.status_code != 200:
                messagebox.showerror("Помилка", "Не вдалося отримати відео з плейлиста!")
                return

            data = response.json()
            for item in data.get("items", []):
                videos.append({
                    "title": item["snippet"]["title"],
                    "date": item["snippet"]["publishedAt"],
                    "link": BASE_YOUTUBE_URL + item["snippet"]["resourceId"]["videoId"],
                })


            next_page_token = data.get("nextPageToken")
            if not next_page_token:
                break

        self.video_list = videos
        if not self.video_list:
            messagebox.showinfo("Результат", "Нових відео не знайдено!")
            return

        self.update_video_list()
        notification.notify(
            title="Нові відео знайдено",
            message=f"Знайдено {len(self.video_list)} нових відео.",
            app_name="Automation Tool",
        )

    def update_video_list(self):
        # Очистка списка видео
        for row in self.video_tree.get_children():
            self.video_tree.delete(row)


        for video in self.video_list:
            self.video_tree.insert("", "end", values=(video["title"], video["date"], video["link"]))

    def download_video(self):
        selected_item = self.video_tree.selection()
        if not selected_item:
            messagebox.showerror("Помилка", "Будь ласка, виберіть відео для завантаження!")
            return

        video_data = self.video_tree.item(selected_item[0])["values"]
        video_url = video_data[2]


        download_thread = threading.Thread(target=self.download_video_thread, args=(video_url,))
        download_thread.start()

    def download_video_thread(self, video_url):
        try:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
            }
            with ytdlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            messagebox.showinfo("Успіх", f"Відео успішно завантажено!")
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося завантажити відео: {e}")

    def download_video_from_url(self):
        video_url = self.url_input.get().strip()
        if not video_url:
            messagebox.showerror("Помилка", "Будь ласка, введіть URL відео!")
            return


        download_thread = threading.Thread(target=self.download_video_thread, args=(video_url,))
        download_thread.start()


# For test
if __name__ == "__main__":
    root = tk.Tk()
    root.title("YouTube Monitor")
    tab_control = ttk.Notebook(root)
    youtube_monitor_tab = YouTubeMonitorTab(tab_control)
    tab_control.add(youtube_monitor_tab.frame, text="Моніторинг YouTube")
    tab_control.pack(expand=1, fill="both")
    root.mainloop()
