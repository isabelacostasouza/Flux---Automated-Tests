# -*- coding: utf-8 -*-

import sys
import json
import scrapper.api

def main():
    automator = scrapper.api.FluxTester()

    with open(sys.argv[1]) as f:
        data = json.load(f)
    
    workflows = data['workflows']
    automator.login_on_dev(data['username'], data['password'])

    for workflow in workflows:
        automator.select_workflow(workflow['name'])
        automator.create_instance()

        for date_input in workflow['date_input']:
            automator.insert_text_on_input(date_input['input_id'], date_input['value'], True)

        for text_input in workflow['text_input']:
            automator.insert_text_on_input(text_input['input_id'], text_input['value'])
        
        for radiobox_item in workflow['radiobox_item']:
            automator.select_first_radiobox_option(radiobox_item['radiobox_id'])

        for register_option in workflow['register_option']:
            automator.select_first_register_option(register_option['register_id'], register_option['register_panel_id'])
        
        for dropdown_option in workflow['dropdown_option']:
            automator.select_first_dropdown_option(dropdown_option['dropdown_id'], dropdown_option['dropdown_panel_id'])
        
        automator.send_instance()
        automator.time_sleep(3)

        activity_counter = 0

        for activity in workflow['activities']:
            automator.select_new_activity(activity_counter)

            for date_input in activity['date_input']:
                automator.insert_text_on_input(date_input['input_id'], date_input['value'], True)

            for text_input in activity['text_input']:
                automator.insert_text_on_input(text_input['input_id'], text_input['value'])
            
            for radiobox_item in activity['radiobox_item']:
                automator.select_first_radiobox_option(radiobox_item['radiobox_id'])

            for register_option in activity['register_option']:
                automator.select_first_register_option(register_option['register_id'], register_option['register_panel_id'])
            
            for dropdown_option in activity['dropdown_option']:
                automator.select_first_dropdown_option(dropdown_option['dropdown_id'], dropdown_option['dropdown_panel_id'])
            
            automator.send_instance()
        
            activity_counter += 1

    automator.time_sleep(1000)

main()