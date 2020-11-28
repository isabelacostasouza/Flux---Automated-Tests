# -*- coding: utf-8 -*-

import scrapper.api

def main():
    automator = scrapper.api.FluxTester()

    username = ''
    password = ''
    workflow_name = 'DAF'

    automator.login_on_dev(username, password)
    automator.select_workflow(workflow_name)
    automator.create_instance()

    automator.select_first_radiobox_option('ensaioTA')
    automator.select_first_dropdown_option('j_id__v_11_j_id8', 'tipoEns_panel')
    automator.select_first_dropdown_option('j_id__v_19_j_id16', 'regOrganismo_panel')
    automator.insert_text_on_input('numEnsaio', '4')
    automator.insert_text_on_input('iniEnsaio_input', '27/11/2020 09:44')
    automator.insert_text_on_input('fimEnsaio_input', '28/11/2020 10:17')
    automator.select_first_dropdown_option('j_id__v_45_j_id41', 'operador_panel')

    automator.send_instance()

    automator.time_sleep(60)

main()
