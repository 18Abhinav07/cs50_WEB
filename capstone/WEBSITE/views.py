from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
import datetime
# from .FRCG import res
import os
from django.http import JsonResponse


def home(request):
    print(datetime.datetime.now())
    return render(request, "BASE/home.html", {})


def login_user(request, user_group):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user_auth = authenticate(request, username=username, password=password)

        if user_auth is not None:
            if user_auth.groups.filter(name="admin").exists():
                login(request, user_auth)
                messages.success(request, "You have been logged in as an Admin.")
                request.session["username"] = username
                return render(request, "ADMINS/admin.html", {"user_group": user_group})

            elif user_auth.groups.filter(name="guard").exists():
                login(request, user_auth)
                messages.success(request, "You have been logged in as an Guard.")
                request.session["username"] = username
                return render(
                    request,
                    "GUARDS/guard.html",
                    {
                        "user_group": user_group,
                        "form1": AddInstituteAdmittedDetailsForm,
                        "form2": AddNIPDetailsForm,
                    },
                )

            else:
                messages.success(
                    request,
                    "There was an error in logging you in, You are not an Admin.",
                )
                return redirect("home")
        else:
            messages.success(
                request, "There was an error in logging you in, Please try again."
            )
            return redirect("home")

    else:
        if user_group == "admin":
            return render(request, "BASE/login.html", {"user_group": user_group})
        elif user_group == "guard":
            return render(request, "BASE/login.html", {"user_group": user_group})
        else:
            messages.success(
                "You are not meeting the required demands. Please try a valid method."
            )
            return redirect("home")


def upload_image(request, user):
    if request.method == "POST" and request.FILES["image"]:
        image_file = request.FILES["image"]
        image_file.name = "temp.jpg"
        filepath = os.path.join("test/", image_file.name)
        os.makedirs("test/", exist_ok=True)
        with open(filepath, "wb") as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

        print("Image saved to:", filepath)
        db_path = "./WEBSITE/train/"  # path/to/file
        # roll_num = res(filepath)
        # roll_num = roll_num.replace(db_path, "")
        # roll_num = roll_num.replace("/", "")
        # print(
        #     "roll",
        #     roll_num,
        # )
        if user == "guard":

            s_details = STUDENTS_DATA.objects.get(roll_no=roll_num)

            new_obj = INSTITUTE_ADMITTED()
            new_obj.name = s_details.name
            new_obj.roll_no = s_details.roll_no
            new_obj.reason = "FROM IMAGE"
            new_obj.permission = "NO"
            new_obj.phone = s_details.phone
            new_obj.branch = s_details.branch
            new_obj.batch = s_details.batch
            new_obj.vehicle_no = "NA"
            new_obj.created_at = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            new_obj.save()
            
            messages.success(request, "The student record was successfully added.")

            form1 = AddInstituteAdmittedDetailsForm()
            form2 = AddNIPDetailsForm()
            return render(
                request,
                "GUARDS/guard.html",
                {"data": s_details, "form1": form1, "form2": form2},
            )

        elif user == "admin":

            entries2 = INSTITUTE_ADMITTED.objects.filter(roll_no=roll_num)
            entries1 = ()
            entries3 = ()
            entries4 = ()
            filter_dict = {"name": "", "roll_no": roll_num, "batch": "", "branch": ""}

            return render(
                request,
                "DATA/students_data.html",
                {
                    "entries1": entries1,
                    "entries2": entries2,
                    "entries3": entries3,
                    "entries4": entries4,
                    "filter_dict": filter_dict,
                },
            )

    else:
        form1 = AddInstituteAdmittedDetailsForm()
        form2 = AddNIPDetailsForm()
        return render(request, "GUARDS/guard.html", {"form1": form1, "form2": form2})


def add_student_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddInstituteAdmittedDetailsForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added Successfully...")
                return redirect("add_student_record")
        else:
            form1 = AddInstituteAdmittedDetailsForm()
            form2 = AddNIPDetailsForm()
        return render(request, "GUARDS/guard.html", {"form1": form1, "form2": form2})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")


def add_non_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddNIPDetailsForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added Successfully...")
                return redirect("add_non_record")
        else:
            form1 = AddInstituteAdmittedDetailsForm()
            form2 = AddNIPDetailsForm()
        return render(request, "GUARDS/guard.html", {"form1": form1, "form2": form2})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")


def new_user(request):
    if request.user.is_authenticated:
        form = SignUpForm()
        return render(request, "BASE/register.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            form.save_m2m()
            group = form.cleaned_data["group"]
            group.user_set.add(user)
            messages.success(request, "The user was successfully created.")
            redirect("new_user")
    else:
        form = SignUpForm(request.POST)
    return render(request, "BASE/register.html", {"form": form})


def get_students_data(request):
    entries1 = INSTITUTE_ADMITTED.objects.filter(batch="First Year")
    entries2 = INSTITUTE_ADMITTED.objects.filter(batch="Second Year")
    entries3 = INSTITUTE_ADMITTED.objects.filter(batch="Third Year")
    entries4 = INSTITUTE_ADMITTED.objects.filter(batch="Fourth Year")
    entries5 = INSTITUTE_ADMITTED.objects.filter(batch="M.Tech")
    entries6 = INSTITUTE_ADMITTED.objects.filter(batch="PhD")
    data = (entries1, entries2, entries3, entries4, entries5, entries6)

    return render(request, "DATA/students_data.html", {"data": data})


def filter_student_records(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll_no = request.POST.get("roll_no")
        if roll_no == "":
            roll_no = None
        batch = request.POST.get("batch")
        branch = request.POST.get("branch")

        entries1 = ()
        entries2 = ()
        entries3 = ()
        entries4 = ()

        if name is not None:
            entries1 = INSTITUTE_ADMITTED.objects.filter(name=name)
        if roll_no is not None:
            entries2 = INSTITUTE_ADMITTED.objects.filter(roll_no=roll_no)
        if batch is not None:
            entries3 = INSTITUTE_ADMITTED.objects.filter(batch=batch)
        if branch is not None:
            entries4 = INSTITUTE_ADMITTED.objects.filter(branch=branch)

        filter_dict = {
            "name": name,
            "roll_no": roll_no,
            "batch": batch,
            "branch": branch,
        }

        if name is None and roll_no is None and batch is None:
            return redirect("get_students_data")

        return render(
            request,
            "DATA/students_data.html",
            {
                "entries1": entries1,
                "entries2": entries2,
                "entries3": entries3,
                "entries4": entries4,
                "filter_dict": filter_dict,
            },
        )
    else:
        return redirect("get_students_data")


def get_details(request):
    entries = NON_INSTITUTE_ADMITTED.objects.all()
    return render(request, "DATA/details.html", {"entries": entries})


def student_management(request):
    if request.user.is_authenticated:
        return render(request, "ADMINS/admin_choice.html", {})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")


def new_student(request):
    if request.user.is_authenticated:
        form = AddStudentDetailsForm()
        return render(request, "STUDENTS/student_management.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")


def add_student_details(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddStudentDetailsForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "The student was successfully created.")
                return redirect("new_student")
            else:
                messages.success(request, "The student was not created.")
                return redirect("new_student")

        else:
            form = AddStudentDetailsForm(request.POST)
            return render(request, "STUDENTS/student_management.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")


def update_student(request):
    if request.user.is_authenticated:
        form = UpdateStudentForm()
        return render(request, "STUDENTS/roll.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")


def check(request):
    if request.method == "POST":
        roll_no = request.POST.get("roll_no")
        if roll_no == "":
            roll_no = None
            messages.success(request, "There was an error in you roll number.")
            return redirect("update_student")
        entries = STUDENTS_DATA.objects.filter(roll_no=roll_no)
        form1 = AddStudentDetailsForm()
        return render(
            request,
            "STUDENTS/update_student.html",
            {"entries": entries, "roll": roll_no, "form1": form1},
        )
    else:
        form = UpdateStudentForm()
        return render(request, "STUDENTS/roll.html", {"form": form})


def update_student_details(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            roll_num = request.POST.get("roll_no")
            s_det = STUDENTS_DATA.objects.get(roll_no=roll_num)

            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            room_no = request.POST.get("room_no")
            batch = request.POST.get("batch")
            branch = request.POST.get("branch")

            data_dict = {
                "roll_no": roll_num,
                "name": s_det.name,
                "email": s_det.email,
                "phone": s_det.phone,
                "room_no": s_det.room_no,
                "batch": s_det.batch,
                "branch": s_det.branch,
            }

            student = STUDENTS_DATA.objects.get(roll_no=roll_num)
            student.name = name
            student.email = email
            student.phone = phone
            student.room_no = room_no
            student.batch = batch
            student.branch = branch
            student.roll_no = roll_num
            student.save()

            messages.success(request, "The student was successfully updated.")
            entries1 = STUDENTS_DATA.objects.filter(roll_no=roll_num)

            return render(
                request,
                "STUDENTS/update_student.html",
                {"entries0": data_dict, "roll": roll_num, "entries1": entries1},
            )
        else:
            form = UpdateStudentForm()
            return render(request, "STUDENTS/update_student.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")


def delete_student(request):
    if request.user.is_authenticated:
        form = UpdateStudentForm()
        return render(request, "STUDENTS/roll_d.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")


def check_r(request):
    if request.method == "POST":
        roll_no = request.POST.get("roll_no")
        if roll_no == "":
            roll_no = None
            messages.success(request, "There was an error in you roll number.")
            return redirect("delete_student")
        entries = STUDENTS_DATA.objects.filter(roll_no=roll_no)
        l_entries = INSTITUTE_ADMITTED.objects.filter(roll_no=roll_no)
        return render(
            request,
            "STUDENTS/delete.html",
            {
                "entries": entries,
                "l_entries": l_entries,
                "roll": roll_no,
            },
        )
    else:
        form = UpdateStudentForm()
        return render(request, "STUDENTS/roll_d.html", {"form": form})


def confirm_delete(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            response = request.POST.get("response")
            roll_num = request.POST.get("roll_no")
            if response == "YES":
                student = STUDENTS_DATA.objects.get(roll_no=roll_num)
                student.delete()
                messages.success(request, "The student was successfully deleted.")
                return redirect("delete_student")
            else:
                messages.success(
                    request,
                    "The student was not deleted as the operation was cancelled.",
                )
                return redirect("delete_student")
        else:
            form = UpdateStudentForm()
            return render(request, "STUDENTS/roll_d.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")


def analytics(request):
    if request.user.is_authenticated:
        return render(request, "DATA/analytics.html", {})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")

def chart_data(request):
    
    fy = INSTITUTE_ADMITTED.objects.filter(batch="First Year").count()
    sy = INSTITUTE_ADMITTED.objects.filter(batch="Second Year").count()
    ty = INSTITUTE_ADMITTED.objects.filter(batch="Third Year").count()
    foy = INSTITUTE_ADMITTED.objects.filter(batch="Fourth Year").count()
    mtech = INSTITUTE_ADMITTED.objects.filter(batch="M.Tech").count()
    phd = INSTITUTE_ADMITTED.objects.filter(batch="PhD").count()
    data = {
        'firstYear': fy,
        'secondYear': sy,
        'thirdYear': ty,
        'fourthYear': foy,
        'mTech': mtech,
        'phd': phd
    }
    return JsonResponse(data)
    

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")
