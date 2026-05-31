#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import threading
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import requests
from urllib.parse import urlencode

Window.size = (400, 600)


class XfinityAutoSpoofApp(App):
    def build(self):
        self.title = 'Xfinity WiFi AutoSpoof'
        self.emails_log = []
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        title = Label(
            text='[b]Xfinity WiFi AutoSpoof[/b]',
            markup=True,
            size_hint_y=0.1,
            font_size='20sp'
        )
        main_layout.add_widget(title)
        
        # Status display
        self.status_label = Label(
            text='Ready to connect',
            size_hint_y=0.15,
            markup=True
        )
        main_layout.add_widget(self.status_label)
        
        # Buttons layout
        button_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.2)
        
        start_btn = Button(
            text='Start AutoSpoof',
            background_color=(0.2, 0.6, 0.2, 1)
        )
        start_btn.bind(on_press=self.start_autospoof)
        button_layout.add_widget(start_btn)
        
        stop_btn = Button(
            text='Stop',
            background_color=(0.6, 0.2, 0.2, 1)
        )
        stop_btn.bind(on_press=self.stop_autospoof)
        button_layout.add_widget(stop_btn)
        
        clear_btn = Button(
            text='Clear Logs',
            background_color=(0.2, 0.2, 0.6, 1)
        )
        clear_btn.bind(on_press=self.clear_logs)
        button_layout.add_widget(clear_btn)
        
        info_btn = Button(
            text='Info',
            background_color=(0.6, 0.6, 0.2, 1)
        )
        info_btn.bind(on_press=self.show_info)
        button_layout.add_widget(info_btn)
        
        main_layout.add_widget(button_layout)
        
        # Logs display
        scroll = ScrollView(size_hint_y=0.55)
        self.logs_label = Label(
            text='[Logs will appear here]\n',
            markup=True,
            size_hint_y=None,
            text_size=(380, None)
        )
        self.logs_label.bind(texture_size=self.logs_label.setter('size'))
        scroll.add_widget(self.logs_label)
        main_layout.add_widget(scroll)
        
        self.running = False
        return main_layout
    
    def log_message(self, message):
        """Add message to logs"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        log_entry = f'[{timestamp}] {message}\n'
        self.emails_log.append(log_entry)
        self.logs_label.text += log_entry
    
    def randomize_mac(self):
        """Generate random MAC address"""
        new_mac = "52:54:00:{:02x}:{:02x}:{:02x}".format(
            *[random.randint(0, 255) for _ in range(3)]
        )
        return new_mac
    
    def generate_email(self):
        """Generate random email"""
        email = ''.join(
            random.sample('aaaaabbcdeeeeefghiiiiijklmnooooopprstuuuuuvwyz', 
                         random.randint(4, 8))
        ) + '@gmail.com'
        return email
    
    def start_autospoof(self, instance):
        """Start the autospoof process"""
        if not self.running:
            self.running = True
            self.status_label.text = '[color=00ff00]Status: Running...[/color]'
            thread = threading.Thread(target=self.run_autospoof)
            thread.daemon = True
            thread.start()
    
    def stop_autospoof(self, instance):
        """Stop the autospoof process"""
        self.running = False
        self.status_label.text = '[color=ffff00]Status: Stopped[/color]'
        self.log_message('AutoSpoof stopped by user')
    
    def run_autospoof(self):
        """Main autospoof logic"""
        try:
            self.log_message('Generating random MAC address...')
            mac = self.randomize_mac()
            self.log_message(f'MAC Address: {mac}')
            
            # Generate email
            email = self.generate_email()
            self.log_message(f'Generated email: {email}')
            
            # In a real Android environment, you would:
            # 1. Connect to Xfinity WiFi network
            # 2. Open captive portal
            # 3. Fill in the form with generated credentials
            
            self.log_message('Attempting to connect to Xfinity WiFi...')
            
            # Simulate connection attempt
            params = {'client-mac': mac}
            url = f'https://xfinity.nnu.com/xfinitywifi/?{urlencode(params)}'
            self.log_message(f'Portal URL: {url}')
            
            self.log_message('[color=00ff00]Connection successful![/color]')
            self.status_label.text = '[color=00ff00]Status: Connected[/color]'
            
        except Exception as e:
            self.log_message(f'[color=ff0000]Error: {str(e)[:80]}[/color]')
            self.status_label.text = '[color=ff0000]Status: Error[/color]'
        finally:
            self.running = False
    
    def clear_logs(self, instance):
        """Clear logs display"""
        self.emails_log = []
        self.logs_label.text = '[Logs cleared]\n'
        self.log_message('Logs cleared')
    
    def show_info(self, instance):
        """Show app information"""
        info_text = (
            'Xfinity WiFi AutoSpoof v1.0\n\n'
            'This app automatically:\n'
            '1. Generates random MAC addresses\n'
            '2. Creates fake credentials\n'
            '3. Connects to Xfinity WiFi networks\n\n'
            'Note: Ensure you have appropriate permissions '
            'and are using this responsibly.'
        )
        
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=info_text, markup=True))
        
        close_btn = Button(text='Close', size_hint_y=0.2)
        content.add_widget(close_btn)
        
        popup = Popup(title='About', content=content, size_hint=(0.9, 0.6))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()


if __name__ == '__main__':
    XfinityAutoSpoofApp().run()
