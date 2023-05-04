from re import L
from helper_func import *
from db_queries import *
import tkinter as tk
from tkinter import messagebox


"""def checkin_clicked(window, fare, pic_path):
    new_pic_path = pic_path.replace('/', '\\')
    fare = float(fare)
    number_plate_str = getNumberPlateSting(new_pic_path)
    res = addVehicleCheckin(vehicle_num=number_plate_str, fare=fare)
    if(res == True):
        messagebox.showinfo(
            'SUCCESS!!!', 'Vehicle is allocated with parking slot')"""
parking_slot_num=1
def checkin_clicked(window, fare, pic_path):
    global parking_slot_num
    
    new_pic_path = pic_path.replace('/', '\\')
    fare = float(fare)
    number_plate_str = getNumberPlateSting(new_pic_path)
    res = addVehicleCheckin(vehicle_num=number_plate_str, fare=fare)
    if res:
        messagebox.showinfo('success', f'Vehicle is allocated with parking slot {parking_slot_num}')
        parking_slot_num += 1
    else:
        messagebox.showerror('error', 'Failed to allocate parking slot')

def checkout_clicked(window, pic_path):
    new_pic_path = pic_path.replace('/', '\\')
    number_plate_str = getNumberPlateSting(pic_path)
    res = addVehicleCheckout(vehicle_num=number_plate_str)
    ans = getCheckoutdetails(vehicle_num=number_plate_str)

    text_str = 'Number= '+str(ans[0])+'\n'+'Check-In Time= ' + str(ans[1])+'\n'+'Check-Out Time= '+str(ans[2])+'\n'+'Base Fare  = '+"₹"+str(ans[3])+'\n'+'Collectible Fare  = ' +"₹"+ \
        str(ans[4])+'\n'+'Durationin seconds = '+str(ans[5])+'\n'
    if(res == True):
        messagebox.showinfo(
            'Charges Calculated!!', text_str)
    delete(vehicle_num=number_plate_str)
    # pass
