# Find-Lawyer-Scraper
# How to use:
Clone the repository and navigate to working dir:
```
mkdir Find-lawyer
git clone https://github.com/NguyenAnMinhThien/Find-lawyer.git Find-lawyer
```
```
cd Find-lawyer
```
If you want to use virtual env, follow these steps:
  
  1. Create virtual env
  ```
  python -m venv venv
  ```
  2. Activate the venv:

  - For WindowPowerShell terminal:

  ```
  .\venv\Scripts\activate.ps1
  ```
> [!NOTE]
> If you can not excute the script, it may dueto you still not change the excution policy. Reference [about_Execution_Policies](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4) to know more.
  - Or Bash terminal:
  ```
  source venv/bin/activate
  ```
  3. Install the required packages:
   ```
     pip install -r requirement.txt
   ```
   
Run the code:
```
python main.py
```

Get the result at output folder.
