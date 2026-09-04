%global source0_hash b8d3eed58eb99d949a1d92a24b116c2e0e14a8760083fe10f88bbcf041bbff04

Name:           ansible-collection-community-general
Version:        12.4.0
Release:        1%{?dist}
Summary:        Modules and plugins supported by Ansible community

# rg --pcre2 -g '!tests/sanity/extra/licenses.py' 'SPDX-License-Identifier: (?!GPL-3\.0-or-later)' | sort | sed 's|^|# |'
#
# plugins/doc_fragments/lxca_common.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/alicloud_ecs.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/database.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/deps.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/_filelock.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/gandi_livedns_api.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/heroku.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/hwc_utils.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/ibm_sa_utils.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/identity/keycloak/keycloak.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/influxdb.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/ipa.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/known_hosts.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/linode.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/lxd.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/manageiq.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/memset.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/base.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/deco.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/exceptions.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/mixins/deprecate_attrs.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/mixins/deps.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/mixins/state.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/mixins/vars.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/module_helper.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/module_helper.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/_mount.py:# SPDX-License-Identifier: PSF-2.0
# plugins/module_utils/oneandone.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/onepassword.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/oneview.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/online.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/opennebula.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/pure.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/rax.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/redhat.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/remote_management/lxca/common.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/saslprep.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/source_control/bitbucket.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/storage/emc/emc_vnx.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/storage/hpe3par/hpe3par.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/_stormssh.py:# SPDX-License-Identifier: MIT
# plugins/module_utils/univention_umc.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/utm_utils.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/vardict.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/vexata.py:# SPDX-License-Identifier: BSD-2-Clause
# tests/unit/plugins/modules/test_gem.py:# SPDX-License-Identifier: MIT
# tests/unit/plugins/module_utils/test_utm_utils.py:# SPDX-License-Identifier: BSD-2-Clause
License:        GPL-3.0-or-later AND BSD-2-Clause AND MIT AND PSF-2.0
URL:            %{ansible_collection_url community general}
%global furl    https://github.com/ansible-collections/community.general
Source:         %{furl}/archive/%{version}/%{name}-%{version}.tar.gz
# Remove unnecessary/development files from the built collection.
# Docs and licenses that are already installed to the standard locations are
# also removed.
# This is a downstream only patch.
Patch:          build_ignore.patch

BuildRequires:  ansible-packaging
# Version 5 specifically requires ansible-core 2.11 or above
Requires:       ansible-core > 2.11

BuildArch:      noarch

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n community.general-%{version} -p1
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%build
%ansible_collection_build

%install
%ansible_collection_install

%files -f %{ansible_collection_filelist}
%license COPYING LICENSES REUSE.toml *.license
%doc README.md CHANGELOG.rst CHANGELOG.md

%changelog
%autochangelog
