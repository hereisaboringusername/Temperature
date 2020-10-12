Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #conditions.py
temp = input("Please enter the current temperature: ")

if temperature >=90:
        print("Wear Shorts")
elif temperature >=70:
        print("Short sleeves are fine")
elif temperature >=50:
        print("Wear a jacket")
elif temperature >=32:
        print("Wear a heavy coat")
else:
        print("Stay Inside")
