import os
uimUsername = "administrator"
uimPassword = "interOP@123"
uimServer = "10.74.34.24"
uimServerLoginName = "administrator"
uimServerLoginPassword = "interOP@019066"
fileShareIP = "10.17.172.178"
fileShareUserName = "administrator"
fileSharePassword = "interOP@123"
hostName = "lvnqa019066"
domain = r"/lvnqa019066_domain/lvnqa019066_hub/lvnqa019066"
uimPath = r"C:\PROGRA~1\Nimsoft"
uimapi_version = "9.02"
ump_robot_path = r"/lvnqa019066_domain/lvnqa019066_hub/lvnqa019199"
probe_status = r"""{}\bin\pu -u {} -p {} {}/controller probe_status automated_deployment_engine""".format(uimPath, uimUsername, uimPassword, domain)
probe_deactivate = r"""{}\bin\pu -u {} -p {} {}/controller probe_deactivate automated_deployment_engine""".format(uimPath, uimUsername, uimPassword, domain)
probe_activate = r"""{}\bin\pu -u {} -p {} {}/controller probe_activate automated_deployment_engine""".format(uimPath, uimUsername, uimPassword, domain)
probe_deploy = r"""{}\bin\pu -u {} -p {} {}/automated_deployment_engine deploy_probe probename""".format(uimPath, uimUsername, uimPassword, domain)
ump_uimapi_deploy = r"""{}\bin\pu -u {} -p {} {}/automated_deployment_engine deploy_probe uimapi {} {}""".format(uimPath, uimUsername, uimPassword, domain, uimapi_version, ump_robot_path)
uim_https_port = r"""{}\bin\pu -u {} -p {} {}/controller probe_config_set wasp setup https_port 8084""".format(uimPath, uimUsername, uimPassword, domain)
uim_contact_origins_enabled = r"""{}\bin\pu -u {} -p {} {}/controller probe_config_set wasp setup contact_origins_enabled true""".format(uimPath, uimUsername, uimPassword, domain)
ump_https_port = r"""{}\bin\pu -u {} -p {} {}/controller probe_config_set wasp setup https_port 8084""".format(uimPath, uimUsername, uimPassword, ump_robot_path)
ump_contact_origins_enabled = r"""{}\bin\pu -u {} -p {} {}/controller probe_config_set wasp setup contact_origins_enabled true""".format(uimPath, uimUsername, uimPassword, ump_robot_path)
uimVersion = "902"