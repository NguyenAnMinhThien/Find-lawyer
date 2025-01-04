import sys
import utils
import os
import driver


# count = 0
def welcome():
    print("Welcome.")



if __name__ == '__main__':
    total_result, member_urls = driver.get_member_urls()
    my_df = driver.get_dataframe(member_urls,total_result)
    # Save file
    filename, filepath = utils.get_file_name()
    if os.name == "nt":
        # window
        my_df.to_csv(f".\\output\\{filename}")
    else:
        # other
        my_df.to_csv(f"./output/{filename}")

    print(my_df)
    print(f"The file has been saved at: \n{filepath}")
    print(f"The Find Lawyer job has been finished.\n Output file here:\n {filepath}")

