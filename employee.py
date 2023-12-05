from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


class employee:
    def __init__(self,window):
        self.window=window
        self.window.geometry("1530x790+0+0")
        self.window.title("Employee management system")

        
        #variable
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_phone_no=StringVar()
        self.var_email=StringVar()
        self.var_country=StringVar()
        self.var_idprooftable=StringVar()
        self.var_idproof=StringVar()
        self.var_address=StringVar()
        self.var_status=StringVar()
        self.var_salary=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_gender=StringVar()


        label_title=Label(self.window,text='EMPOLYEE  MANAGEMENT  SYSTEM',font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        label_title.place(x=0,y=0,width=1530,height=50)

         #logo
        img_logo=Image.open('Images/logo.png')
        img_logo=img_logo.resize((50,50))
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.window,image=self.photo_logo)
        self.logo.place(x=255,y=0,width=50,height=50)

        #Frame

        img_frame=Frame(self.window,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        #1st image
        img1=Image.open('Images/employee 1.png')
        img1=img1.resize((510,160))
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_place=Label(img_frame,image=self.photo1)
        self.img_place.place(x=0,y=0,width=520,height=160)

        #2nd image
        img2=Image.open('Images/emp2.png')
        img2=img2.resize((510,160))
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_place2=Label(img_frame,image=self.photo2)
        self.img_place2.place(x=510,y=0,width=510,height=160)
 
        #3rd image
        img3=Image.open('Images/emp3.png')
        img3=img3.resize((510,160))
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_place3=Label(img_frame,image=self.photo3)
        self.img_place3.place(x=1000,y=0,width=520,height=160)


        #main frame
        Main_frame=Frame(self.window,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=215,width=1340,height=560)

        #upper frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee information',font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=2,width=1320,height=270)


        

        #label and entry fields
        #department
        lbl_dept=Label(upper_frame,text='Department',font=('arial',11,'bold'),bg='white')
        lbl_dept.grid(row=0,column=0,padx=2,sticky=W)

        combo_dept=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',11,'bold'),width=18,state='readonly')
        combo_dept['value']= ('Select Department','HR','Software department','Manager')
        combo_dept.current(0)
        combo_dept.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Name
        lbl_name=Label(upper_frame,text='Name:',font=('arial',12,'bold'),bg='white')
        lbl_name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,font=('arial',11,'bold'),width=22)
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        #Phone no.
        lbl_phone=Label(upper_frame,text='Phone no.:',font=('arial',12,'bold'),bg='white')
        lbl_phone.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone_no,font=('arial',11,'bold'),width=22)
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        #Designation
        lbl_Designation=Label(upper_frame,text='Designation:',font=('arial',12,'bold'),bg='white')
        lbl_Designation.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_Designation=ttk.Entry(upper_frame,textvariable=self.var_designation,font=('arial',11,'bold'),width=22)
        txt_Designation.grid(row=1,column=1,padx=2,pady=7)

        #Email
        lbl_email=Label(upper_frame,text='Email:',font=('arial',12,'bold'),bg='white')
        lbl_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,font=('arial',11,'bold'),width=22)
        txt_email.grid(row=1,column=3,padx=2,pady=7)

        #country
        lbl_country=Label(upper_frame,text='country:',font=('arial',12,'bold'),bg='white')
        lbl_country.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,font=('arial',11,'bold'),width=22 )
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        #Address
        lbl_Address=Label(upper_frame,text='Address:',font=('arial',12,'bold'),bg='white')
        lbl_Address.grid(row=2,column=0,padx=0,pady=7,sticky=W)

        txt_Address=ttk.Entry(upper_frame,textvariable=self.var_address,font=('arial',11,'bold'),width=22)
        txt_Address.grid(row=2,column=1,padx=0,pady=7)

        #married status
        lbl_status=Label(upper_frame,text='Status:',font=('arial',12,'bold'),bg='white')
        lbl_status.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        combo_status=ttk.Combobox(upper_frame,textvariable=self.var_status,font=('arial',12,'bold'),width=18,state='readonly')
        combo_status['value']=('select status','Married','Unmarried')
        combo_status.current(0)
        combo_status.grid(row=2,column=3,padx=2,pady=7)

        #salary
        lbl_salary=Label(upper_frame,text='Salary(CTC):',font=('arial',12,'bold'),bg='white')
        lbl_salary.grid(row=2,column=4,padx=0,pady=7,sticky=W)

        txt_salary=ttk.Entry(upper_frame,textvariable=self.var_salary,font=('arial',11,'bold'),width=22)
        txt_salary.grid(row=2,column=5,padx=0,pady=7)

        #DOB
        lbl_DOB=Label(upper_frame,text='DOB:',font=('arial',12,'bold'),bg='white')
        lbl_DOB.grid(row=3,column=0,padx=0,pady=7,sticky=W)

        txt_DOB=ttk.Entry(upper_frame,textvariable=self.var_dob,font=('arial',11,'bold'),width=22)
        txt_DOB.grid(row=3,column=1,padx=0,pady=7)

        #DOJ
        lbl_DOJ=Label(upper_frame,text='DOJ:',font=('arial',12,'bold'),bg='white')
        lbl_DOJ.grid(row=3,column=2,padx=0,pady=7,sticky=W)

        txt_DOJ=ttk.Entry(upper_frame,textvariable=self.var_doj,font=('arial',11,'bold'),width=22)
        txt_DOJ.grid(row=3,column=3,padx=0,pady=7)

        #ID proof card
        
        combo_IDproof=ttk.Combobox(upper_frame,textvariable=self.var_idprooftable,font=('arial',12,'bold'),width=18,state='readonly')
        combo_IDproof['value']=('Id proof','Pan card','Aadhar card','driving licence')
        combo_IDproof.current(0)
        combo_IDproof.grid(row=4,column=0,padx=2,pady=7)

        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,font=('arial',11,'bold'),width=22)
        txt_proof.grid(row=4,column=1,sticky=W,padx=2,pady=7)

        #Gender
        lbl_Gender=Label(upper_frame,text='Gender:',font=('arial',12,'bold'),bg='white')
        lbl_Gender.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        combo_Gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',12,'bold'),width=17,state='readonly')
        combo_Gender['value']=('Select','Male','Female')
        combo_Gender.current(0)
        combo_Gender.grid(row=4,column=3,padx=0,pady=7,sticky=W)

        #mask image
        mask=Image.open('Images/mask lady.png')
        mask=mask.resize((220,250))
        self.photo4=ImageTk.PhotoImage(mask)

        self.img_place3=Label(upper_frame,image=self.photo4)
        self.img_place3.place(x=930,y=0,width=210,height=250)


        #button frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1150,y=3,width=150,height=215)

        #buttons(Save)
        buttons_add=Button(button_frame,text='Save',command=self.add_data,font=('arial',15,'bold'),width=11,bg='blue',fg='white')
        buttons_add.grid(row=0,column=0,padx=1,pady=5)

        #update
        buttons_add=Button(button_frame,text='Update',command=self.update_data,font=('arial',15,'bold'),width=11,bg='blue',fg='white')
        buttons_add.grid(row=1,column=0,padx=1,pady=5)
        
        #delete
        buttons_add=Button(button_frame,text='Delete',command=self.delete_data,font=('arial',15,'bold'),width=11,bg='blue',fg='white')
        buttons_add.grid(row=2,column=0,padx=1,pady=5)
        
        #reset
        buttons_add=Button(button_frame,text='Rest',command=self.reset_data,font=('arial',15,'bold'),width=11,bg='blue',fg='white')
        buttons_add.grid(row=3,column=0,padx=1,pady=5)


        #down frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee information table',font=('times new roman',11,'bold'),fg='blue')
        down_frame.place(x=10,y=275,width=1320,height=270)

        #search frame
        Search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search employee information',font=('arial',8,'bold'),fg='blue')
        Search_frame.place(x=0,y=0,width=1420,height=60)
        #Search by label
        search_by=Label(Search_frame,text='Search by:',font=('arial',12,'bold'),fg='black',bg='red')
        search_by.grid(row=0,column=0,padx=5,sticky=W)

        #search box
        self.var_combo_search=StringVar()
        combo_search=ttk.Combobox(Search_frame,textvariable=self.var_combo_search,font=('arial',12,'bold'),width=11,state='readonly')
        combo_search['value']=('Select','Phone no.','Name','DOB','Gender','department')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2,pady=7,sticky=W)
        
         #entry
        self.var_entry=StringVar()
        txt_search=ttk.Entry(Search_frame,textvariable=self.var_entry,font=('arial',12,'bold'),width=22)
        txt_search.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        search_button=Button(Search_frame,text='Search',command=self.search_data,font=('arial',12,'bold'),bg='blue',fg='white',width=10)
        search_button.grid(row=0,column=3,padx=2,pady=7,sticky=W)

        show_button=Button(Search_frame,text='Show all',command=self.fetch_data,font=('arial',12,'bold'),bg='blue',fg='white',width=11)
        show_button.grid(row=0,column=4,padx=4,pady=7,sticky=W)

        mask_label=Label(Search_frame,text='Wear a Mask',font=('times new roman',30,'bold'),bg='white',fg='red')
        mask_label.place(x=680,y=0,width=600,height=30)

        mask_img=Image.open('Images/mask lady.png')
        mask_img=mask_img.resize((50,50))
        self.mask_logo=ImageTk.PhotoImage(mask_img)

        self.photo_logo=Label(Search_frame,image=self.mask_logo)
        self.photo_logo.place(x=800,y=0,width=50,height=50)


                        #================Employee table==========

        table_frame=Frame(down_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=0,y=55,width=1325,height=130)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("dep","Name","desi","phone no.","email","cou","idprooftable","idproof","address","status","sala","dob","doj","gend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("dep",text="Department")
        self.employee_table.heading("Name",text="Name")
        self.employee_table.heading("desi",text="Designation")
        self.employee_table.heading("phone no.",text="Phone_no")
        self.employee_table.heading("email",text="Email")
        self.employee_table.heading("cou",text="country")
        self.employee_table.heading("idprooftable",text="id_proof_type")
        self.employee_table.heading("idproof",text="id_proof")
        self.employee_table.heading("address",text="Address")
        self.employee_table.heading("status",text="Status")
        self.employee_table.heading("sala",text="Salary")
        self.employee_table.heading("dob",text="DOB")
        self.employee_table.heading("doj",text="DOJ")
        self.employee_table.heading("gend",text="Gender")

        self.employee_table['show']='headings'

        self.employee_table.column("dep",width=100)
        self.employee_table.column("Name",width=100)
        self.employee_table.column("desi",width=100)
        self.employee_table.column("phone no.",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("cou",width=100)
        self.employee_table.column("idprooftable",width=100)
        self.employee_table.column("idproof",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("status",width=100)
        self.employee_table.column("sala",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("gend",width=100)


        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        #******************************function declaration *************************

    # addition data in database you save the entries
      
    def add_data(self):
        if self.var_dep.get()==" " or self.var_email.get()==" ":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Devi*2001',database='my_data')
                my_cursor=conn.cursor()
                my_cursor.execute('insert ignore into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',( 

                                                                                                               self.var_dep.get(),
                                                                                                               self.var_name.get(),
                                                                                                               self.var_designation.get(),
                                                                                                               self.var_phone_no.get(),
                                                                                                               self.var_email.get(),
                                                                                                               self.var_country.get(),
                                                                                                               self.var_idprooftable.get(),
                                                                                                               self.var_idproof.get(),
                                                                                                               self.var_address.get(),
                                                                                                               self.var_status.get(),
                                                                                                               self.var_salary.get(),
                                                                                                               self.var_dob.get(),
                                                                                                               self.var_doj.get(),
                                                                                                               self.var_gender.get(),                                                                                                              
                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee has been added',parent=self.window)

            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.window)

     #add in interface from database
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Devi*2001',database='my_data')
        my_cursor=conn.cursor()
        my_cursor.execute('select *from employee1')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()
            
            #when you select data it will show on boxes

    def get_cursor(self, event=" "):
        cursor_row= self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        
        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designation.set(data[2])
        self.var_phone_no.set(data[3])
        self.var_email.set(data[4])
        self.var_country.set(data[5])
        self.var_idprooftable.set(data[6])
        self.var_idproof.set(data[7])
        self.var_address.set(data[8])
        self.var_status.set(data[9])
        self.var_salary.set(data[10])
        self.var_dob.set(data[11])
        self.var_doj.set(data[12])
        self.var_gender.set(data[13])


    #update_data(button working code)

    def update_data(self):
        if self.var_dep.get()==" " or self.var_email.get()==" ":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure update this employee')
                if update>0:

                    conn=mysql.connector.connect(host='localhost',username='root',password='Devi*2001',database='my_data')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update employee1 set Department=%s,Name=%s,Designation=%s,Phone_no=%s,Email=%s,country=%s,id_proof_type=%s,Address=%s,Status=%s,Salary=%s,DOB=%s,DOJ=%s,Gender=%s where id_proof=%s',(

                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                                                    self.var_designation.get(),
                                                                                                                                                                                                                    self.var_phone_no.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_country.get(),
                                                                                                                                                                                                                    self.var_idprooftable.get(),
                                                                                                                                                                                                                    
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_status.get(),
                                                                                                                                                                                                                    self.var_salary.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_doj.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_idproof.get()                                                                                                     
                                                                                                                                                                                                                 ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Employee successfully updated',parent=self.window)


            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.window)



        #delete button (working code)

    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                delete=messagebox.askyesno('delete','Are you sure delete this employee')
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Devi*2001',database='my_data')
                    my_cursor=conn.cursor()
                    sql='delete from employee1 where id_proof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('delete','Employee successfully deleted',parent=self.window)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.window)




    #reset button (working)
    def reset_data(self):
        self.var_dep.set('Select Department')
        self.var_name.set('')
        self.var_designation.set('')
        self.var_phone_no.set('')
        self.var_email.set('')
        self.var_country.set('')
        self.var_idprooftable.set('Select id_proof')
        self.var_idproof.set('')
        self.var_address.set('')
        self.var_status.set('Status')
        self.var_salary.set('')
        self.var_dob.set('')
        self.var_doj.sett('')
        self.var_gender.set('')

    #search button 
    def search_data(self):
        if self.var_combo_search.get()==" " or self.var_entry.get()==" ":
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Devi*2001',database='my_data')
                my_cursor=conn.cursor()
                my_cursor.execute("Select *from employee1 where "+str(self.var_combo_search.get())+" LIKE '%"+str(self.var_entry.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:

                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:

                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.window)





         
         

                    
    


        







                          
if __name__=="__main__":
    window=Tk()
    obj=employee(window)
    window.mainloop()
