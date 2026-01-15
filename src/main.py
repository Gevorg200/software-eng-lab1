import ab12345_config as config
import ab12345_data as data
import ab12345_utils as utils
import ab12345_calc as calc

def main():
    utils.print_header()
    calc.start_calculator()
    
    students = data.get_all_students()
    
    for s in students:
        total = sum(s["grades"]) # You can replace this with calc.add_grades later
        print(utils.format_result(s["name"], total))

if __name__ == "__main__":
    main()
