import tkinter as tk
import coronavirus_tracker_functions as tfunc

class Features:
    def __init__(self):
        # !MAIN BG:
        self.bg = "#CB4335"
        
        # !FONT STYLES:
        self.title_font = ("century gothic", 40)
        self.title_font2 = ("century gothic", 23)
        self.secondary_title_font = ("century gothic", 10, "bold")
        self.button_font = ("century gothic", 11)
        self.version_font = ("century gothic", 9)
        self.cards_img_txt_font = ("century gothic", 12, "italic")
        self.cards_lbl_txt_font = ("century gothic", 11)
        self.info_font = ("century gothic", 11)

        # !TEXTS AND TITLES:
        self.title_txt = "H . O . U . N . D"
        self.secondary_title_txt = "- COVID-19 TRACKER -"   
        self.statistics_page_title = "STATISTICS PAGE"
        self.version_txt = "VERSION 2.0"
        self.info_txt = "This app allows the user(you) to observe the local\n(Sri Lankan) and global coronavirus statistics.\nAll the information provided via this app was \nobtained from the: Health Promotion Bureau"

        # !BUTTON COLOURS:
        self.button_bg = "#181818"
        self.button_active_bg = "#111"
        self.button_hover_bg = "#111"
        self.button_fg = self.bg

        # !OTHER COLOURS:
        self.button_frm_bg = "#fff"
        self.title_bg = self.bg
        self.title_fg = "#1B262C"
        self.secondary_title_bg = self.bg
        self.secondary_title_fg = "#fff"
        self.status_bar_bg = "#181818"
        self.version_bg = self.status_bar_bg
        self.version_fg = self.bg
        self.region_bg = self.status_bar_bg
        self.region_fg = "#28B463"
        self.card_bg = "#1B262C"
        self.deaths_img_txt_fg = "#C0392B"
        self.recovered_img_txt_fg = "#28B463"
        self.infected_img_txt_fg = "#C68910"
        self.total_deaths_txt_fg = "#17A589"
        self.info_bg = "#1B262C"
        self.info_fg = "#fff" 

        # !PADDING, WIDTH AND HEIGHT:
        self.padx = 10
        self.pady = 15
        self.button_width = 10
        self.button_inner_pady = 5
        self.button_inner_padx = 5
        self.version_inner_pady = 5
        self.version_inner_padx = 8
        self.card_width = 15
        self.card_height = 5

class Corona_virus_tracker(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("650x500")
        self.title("H . O . U . N . D")
        self.resizable(False, False)
        self.iconbitmap("Logo/pngtree___stay_home_to_protect_from_5341432_QmL_icon.ico")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}
        lst = [Start_page, Statistics_page, Info_page]

        for F in lst:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            

        self.showFrame(Start_page)

    def showFrame(self, page):
        frame = self.frames[page]  
        frame.tkraise()   

class Start_page(tk.Frame, Features):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Features.__init__(self)

        # !FUNCTIONS START HERE
        def button_hover_in(event):
            next_btn["bg"] = self.button_hover_bg
            status_bar.configure(text="NEXT PAGE")

        def button_hover_out(event):
            next_btn["bg"] = self.button_bg
            status_bar.configure(text=self.version_txt)

        self.configure(bg=self.bg)

        # !FRAMES START HERE
        main_frm = tk.Frame(self, bg=self.bg)
        main_frm.place(relx=0.5, rely=0.5, anchor="center")
        self.main_frm = main_frm

        button_frm = tk.Frame(self, bg="blue")
        button_frm.place(relx=0.012, rely=0.91, anchor="sw")
        self.button_frm = button_frm

        # !LABELS START HERE
        primary_lbl = tk.Label(self.main_frm, text=self.title_txt, font=self.title_font, fg=self.title_fg, bg=self.title_bg)
        primary_lbl.pack()

        secondary_lbl = tk.Label(self.main_frm, text=self.secondary_title_txt, font=self.secondary_title_font, bg=self.secondary_title_bg, fg=self.secondary_title_fg)
        secondary_lbl.pack()

        # !BUTTONS START HERE
        next_btn = tk.Button(self.button_frm, text="NEXT", width=self.button_width, font=self.button_font, bg=self.button_bg, fg=self.button_fg, borderwidth=0, activebackground=self.button_bg, activeforeground=self.button_fg, pady=self.button_inner_pady, padx=self.button_inner_pady, command=lambda:controller.showFrame(Statistics_page))
        next_btn.pack()

        next_btn.bind("<Enter>", button_hover_in)
        next_btn.bind("<Leave>", button_hover_out)


        # !STATUS BAR STARTS HERE
        status_bar = tk.Label(self, text=self.version_txt, bg=self.version_bg, fg=self.version_fg, anchor="e", pady=self.version_inner_pady+2, padx=self.version_inner_padx, font=self.version_font)
        status_bar.pack(side="bottom", fill="both")

class Statistics_page(tk.Frame, Features):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Features.__init__(self)

        # !FRAMES START HERE

        self.configure(bg=self.bg)

        main_frm = tk.Frame(self, bg="#181818")
        main_frm.place(relx=0.5, rely=0.5, anchor="center")
        self.main_frm = main_frm

        card_frm1 = tk.Frame(self.main_frm, bg=self.bg)
        card_frm1.pack(fill="both")
        self.card_frm1 = card_frm1

        card_frm2 = tk.Frame(self.main_frm, bg=self.bg)
        card_frm2.pack(fill="both")
        self.card_frm2 = card_frm2

        button_frm = tk.Frame(self, bg=self.bg)
        button_frm.place(relx=0.5, rely=0.85, anchor="center")
        self.button_frm = button_frm

        deaths_frm = tk.Frame(self.card_frm1)
        deaths_frm.pack(side="left", padx=self.padx)
        self.deaths_frm = deaths_frm

        recovered_frm = tk.Frame(self.card_frm1)
        recovered_frm.pack(side="right", padx=self.padx)
        self.recovered_frm = recovered_frm

        infected_frm = tk.Frame(self.card_frm1)
        infected_frm.pack()
        self.infected_frm = infected_frm

        total_deaths_frm = tk.Frame(self.card_frm2)
        total_deaths_frm.pack(padx=self.padx, pady=self.pady)
        self.total_deaths_frm = total_deaths_frm


        # !TITLE STARTS HERE
        main_title = tk.Label(self, text=self.statistics_page_title, font=self.title_font2, fg=self.title_fg, bg=self.title_bg)
        main_title.place(relx=0.5, rely=0.1, anchor="center")


        # !IMAGES START HERE
        deaths_img = tk.Label(self.deaths_frm, text="NEW DEATHS", bg=self.card_bg, width=self.card_width, height=self.card_height, font=self.cards_img_txt_font, fg=self.deaths_img_txt_fg)
        deaths_img.pack(fill="both")

        recovered_img = tk.Label(self.recovered_frm, text="TOTAL RECOVERED", bg=self.card_bg, width=self.card_width, height=self.card_height, font=self.cards_img_txt_font, fg=self.recovered_img_txt_fg)
        recovered_img.pack(fill="both")

        infected_img = tk.Label(self.infected_frm, text="TOTAL INFECTED", bg=self.card_bg, width=self.card_width, height=self.card_height, font=self.cards_img_txt_font, fg=self.infected_img_txt_fg)
        infected_img.pack(fill="both")

        total_deaths_img = tk.Label(self.total_deaths_frm, text="TOTAL DEATHS", fg=self.total_deaths_txt_fg, bg=self.card_bg, width=self.card_width+10, font=self.cards_img_txt_font)
        total_deaths_img.pack(side="left", fill="y")

        # !CARD LABLES
        deaths_lbl = tk.Label(self.deaths_frm, text="000", width=20, height=5, font=self.cards_lbl_txt_font)
        deaths_lbl.pack(fil="both")

        recovered_lbl = tk.Label(self.recovered_frm, text="000", width=20, height=5, font=self.cards_lbl_txt_font)
        recovered_lbl.pack(fil="both")

        infected_lbl = tk.Label(self.infected_frm, text="000", width=20, height=5, font=self.cards_lbl_txt_font)
        infected_lbl.pack(fil="both")

        total_deaths_lbl = tk.Label(self.total_deaths_frm, text="000", width=self.card_width+20, height=self.card_height-2, font=self.cards_lbl_txt_font)
        total_deaths_lbl.pack(side="right")

        # !BUTTONS START HERE
        local_btn = tk.Button(self.button_frm, text="LOCAL", bg=self.button_bg, fg=self.button_fg, font=self.button_font, padx=self.button_inner_padx, pady=self.button_inner_pady, width=self.button_width, borderwidth=0, activebackground=self.button_active_bg, activeforeground=self.button_fg, command=lambda:get_data(option="local"))
        local_btn.pack(side="left", padx=self.padx)

        info_btn = tk.Button(self.button_frm, text="INFO PAGE", bg=self.button_bg, fg=self.button_fg, font=self.button_font, padx=self.button_inner_padx, pady=self.button_inner_pady, width=self.button_width, borderwidth=0, activebackground=self.button_active_bg, activeforeground=self.button_fg, command=lambda:controller.showFrame(Info_page))
        info_btn.pack(side="right", padx=self.padx)

        home_btn = tk.Button(self.button_frm, text="HOME", bg=self.button_bg, fg=self.button_fg, font=self.button_font, padx=self.button_inner_padx, pady=self.button_inner_pady, width=self.button_width, borderwidth=0, activebackground=self.button_active_bg, activeforeground=self.button_fg, command=lambda:controller.showFrame(Start_page))
        home_btn.pack(side="right", padx=self.padx)

        global_btn = tk.Button(self.button_frm, text="GLOBAL", bg=self.button_bg, fg=self.button_fg, font=self.button_font, padx=self.button_inner_padx, pady=self.button_inner_pady, width=self.button_width, borderwidth=0, activebackground=self.button_active_bg, activeforeground=self.button_fg, command=lambda:get_data(option="global"))
        global_btn.pack(side="left", padx=self.padx)



        # !STATUS BAR STARTS HERE
        status_bar = tk.Label(self, text="UPDATED DATE", bg=self.version_bg, fg=self.version_fg, anchor="e", pady=self.version_inner_pady, padx=self.version_inner_padx, font=self.version_font)
        status_bar.pack(side="bottom", fill="both")

        region_lbl = tk.Label(status_bar, text="REGION", bg=self.region_bg, fg=self.region_fg, pady=self.version_inner_pady, padx=self.version_inner_padx, font=self.version_font)
        region_lbl.pack(side="left")


        # !FUNCTIONS START HERE
        def configure_labels(lbl_name, item):
            lbl_name.configure(text=tfunc.Corona_virus_tracker_functions.get_data(tfunc.Corona_virus_tracker_functions.get_data, item))

        def get_data(option="local"):
            try:
                configure_labels(status_bar, "update_date_time")

                if option == "local":
                    configure_labels(deaths_lbl, "local_new_deaths")
                    configure_labels(infected_lbl, "local_total_cases")
                    configure_labels(recovered_lbl, "local_recovered")
                    configure_labels(total_deaths_lbl, "local_deaths")
                    region_lbl.configure(text="LOCAL")

                else:
                    configure_labels(deaths_lbl, "global_new_deaths")
                    configure_labels(infected_lbl, "global_total_cases")
                    configure_labels(recovered_lbl, "global_recovered")
                    configure_labels(total_deaths_lbl, "global_deaths")
                    region_lbl.configure(text="GLOBAL")
            except:
                status_bar.configure(text="PLEASE CONNECT TO THE INTERNET")                

        get_data()

class Info_page(tk.Frame, Features):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Features.__init__(self)

        self.configure(bg=self.bg)

        # !FRAMES START HERE
        content_frm = tk.Frame(self, bg=self.button_frm_bg)
        content_frm.place(relx=0.5, rely=0.5, anchor="center")
        # self.content_frm = content_frm

        button_frm = tk.Frame(content_frm, bg=self.button_frm_bg)
        button_frm.pack(side="bottom")

        # !LABELS START HERE

        main_lbl = tk.Label(self, text="INFO PAGE", font=self.title_font2, bg=self.title_bg, fg=self.title_fg)
        main_lbl.place(relx=0.5, rely=0.1, anchor="center")

        info_lbl = tk.Label(content_frm, text=self.info_txt, bg=self.info_bg, fg=self.info_fg, padx=self.padx, font=self.info_font, height=self.card_height+5, anchor="center")
        info_lbl.pack(fill="both")

        # !BUTTONS START HERE
        back_btn = tk.Button(button_frm, text="GO BACK", fg=self.button_fg, bg=self.button_bg, font=self.button_font, pady=self.button_inner_pady, padx=self.button_inner_padx, width=self.button_width, borderwidth=0, activebackground=self.button_active_bg, activeforeground=self.button_fg, command=lambda:controller.showFrame(Statistics_page))
        back_btn.pack(side="left", padx=self.padx+10, pady=self.pady+10)

        visit_btn = tk.Button(button_frm, text="VISIT SITE", fg=self.button_fg, bg=self.button_bg, font=self.button_font, pady=self.button_inner_pady, padx=self.button_inner_padx, width=self.button_width, borderwidth=0, activebackground=self.button_active_bg, activeforeground=self.button_fg, command=lambda:visit_site(self))
        visit_btn.pack(side="right", padx=self.padx+10, pady=self.pady+10)

        # !STATUS BAR STARTS HERE
        status_bar = tk.Label(self, text=self.version_txt, bg=self.version_bg, fg=self.version_fg, anchor="e", pady=self.version_inner_pady+2, padx=self.version_inner_padx, font=self.version_font)
        status_bar.pack(side="bottom", fill="both")


        # !FUNCTIONS START HERE
        def visit_site(self):
            tfunc.Corona_virus_tracker_functions.visit_site(tfunc.Corona_virus_tracker_functions)

app = Corona_virus_tracker()
app.mainloop()