import os
uim_username = "administrator"
uim_password = "interOP@123"
uimserver = "10.17.166.9"
vm_username = "root"
vm_password = "interOP@123sys"
domain = r"/c74ser_domain/c74ser_hub/c74ser"
uimpath = r"/opt/nimsoft"
uimapi_version = "9.02"
ump_robot_path = r"/c74ser_domain/c74ser_hub/c74ump"
probe_status = r"""{}/bin/pu -u {} -p {} {}/controller probe_status automated_deployment_engine""".format(uimpath, uim_username, uim_password, domain)
probe_deactivate = r"""{}/bin/pu -u {} -p {} {}/controller probe_deactivate automated_deployment_engine""".format(uimpath, uim_username, uim_password, domain)
probe_activate = r"""{}/bin/pu -u {} -p {} {}/controller probe_activate automated_deployment_engine""".format(uimpath, uim_username, uim_password, domain)
probe_deploy = r"""{}/bin/pu -u {} -p {} {}/automated_deployment_engine deploy_probe probename""".format(uimpath, uim_username, uim_password, domain)
ump_uimapi_deploy = r"""{}/bin/pu -u {} -p {} {}/automated_deployment_engine deploy_probe uimapi {} {}""".format(uimpath, uim_username, uim_password, domain, uimapi_version, ump_robot_path)
uim_https_port = r"""{}/bin/pu -u {} -p {} {}/controller probe_config_set wasp setup https_port 8084""".format(uimpath, uim_username, uim_password, domain)
uim_contact_origins_enabled = r"""{}/bin/pu -u {} -p {} {}/controller probe_config_set wasp setup contact_origins_enabled true""".format(uimpath, uim_username, uim_password, domain)
ump_https_port = r"""{}/bin/pu -u {} -p {} {}/controller probe_config_set wasp setup https_port 8084""".format(uimpath, uim_username, uim_password, ump_robot_path)
ump_contact_origins_enabled = r"""{}/bin/pu -u {} -p {} {}/controller probe_config_set wasp setup contact_origins_enabled true""".format(uimpath, uim_username, uim_password, ump_robot_path)
uimversion = "902"
port = 22