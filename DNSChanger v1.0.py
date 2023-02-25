import tkinter
import customtkinter
import os
import datetime


class App (customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        # Modes: system (default), light, dark
        customtkinter.set_appearance_mode("System")
        # Themes: blue (default), dark-blue, green
        customtkinter.set_default_color_theme("blue")

        # textbox
        self.tb = customtkinter.CTkTextbox(
            master=self, width=1300, height=400, corner_radius=0)
        self.tb.grid(row=0, column=0, sticky=tkinter.N, columnspan=3, pady=5)
        # self.tb.configure(state='disabled')
        # clear cmd
        self.btn1 = customtkinter.CTkButton(
            master=self, text="Clear Console", command=self.clr_cmd)
        self.btn1.grid(row=1, column=0, sticky=tkinter.E, padx=2, pady=5)
        # set dns btn
        self.btn = customtkinter.CTkButton(
            master=self, text="Set Shecan DNS", command=self.set_dns)
        self.btn.grid(row=1, column=1, sticky=tkinter.E, padx=2, pady=5)

        # unset dns btn

        self.btn2 = customtkinter.CTkButton(
            master=self, text="Unset Shecan DNS", command=self.dhcp_dns)
        self.btn2.grid(row=1, column=2, sticky=tkinter.E, padx=2, pady=5)

    def button_function(self):
        intefacs = os.popen('netsh interface ipv4 show interfaces').read()
        print(intefacs)
        self.show_cmd(txt=intefacs)

    def set_dns(self):
        # -----Primary DNS    ------
        cmd_message_configs = os.popen(
            'netsh interface ipv4 show dnsservers name = "Wi-Fi"').read()
        if '178.22.122.100' not in cmd_message_configs:
            self.show_cmd(
                txt='netsh interface ipv4 set dns name="Wi-Fi" static 178.22.122.100')
            cmd_message = os.popen(
                'netsh interface ipv4 set dns name="Wi-Fi" static 178.22.122.100').read()
            if cmd_message != "\n":
                self.show_cmd(cmd_message)
            else:
                self.show_cmd(
                    "Successfully! DNS 178.22.122.100 was Set!")
        else:
            self.show_cmd("DNS is already set!")

        # -----Second DNS    ------
        if '185.51.200.2' not in cmd_message_configs:
            self.show_cmd(
                txt='netsh interface ipv4 add dns name="Wi-Fi" 185.51.200.2 index=2')
            cmd = os.popen(
                'netsh interface ipv4 add dns name="Wi-Fi" 185.51.200.2 index=2').read()
            if cmd != "\n":
                self.show_cmd(cmd_message)
            else:
                self.show_cmd("Successfully! DNS 185.51.200.2 was Set!")
        else:
            self.show_cmd("DNS is already set!")

    def dhcp_dns(self):
        self.show_cmd(
            'netsh interface ip set dns "Wi-Fi" dhcp')

        cmd_message = os.popen(
            'netsh interface ip set dns "Wi-Fi" dhcp').read()
        if cmd_message is "\n":
            self.show_cmd("Successfully UnSet!")
        else:
            self.show_cmd(cmd_message)

    def show_cmd(self, txt):

        self.tb.insert(index=tkinter.END, text="\n"+"-" +
                       datetime.datetime.now().strftime("%X") + "- "+txt)

    def clr_cmd(self):
        self.tb.delete(index1="0.0", index2=tkinter.END)


app = App()  # create CTk window like you do with the Tk window
app.geometry("400x600")
app.title("DNS Changer")
app.resizable(True, False)

app.mainloop()
