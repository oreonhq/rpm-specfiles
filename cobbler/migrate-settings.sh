#!/bin/bash
sed -i -e 's,^default_kickstart: */var/lib/cobbler/kickstarts,default_autoinstall: /var/lib/cobbler/templates,' \
       -e '/^\(consoles\|func_\|kernel_options_s390x\|power_template_dir\|pxe_template_dir\|redhat_management_type\|snippetsdir\|template_remote_kickstarts\):/s/^/# REMOVED: /' \
       -e '$a#ADDED:' -e '$acache_enabled: true' -e '$areposync_rsync_flags: "-rltDv --copy-unsafe-links"' /etc/cobbler/settings.yaml
