%global source0_hash cb0cd67e225b9f0f3c50da36e3c4a79f7f4afdde14a94cd54e567210183e6a9f

# ansible-core is built for alternative Python stacks in RHEL which do not have
# the necessary test deps packaged.
%if %{defined fedora}
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           ansible-collection-community-docker
Version:        5.0.6
Release:        1%{?dist}
Summary:        Ansible modules and plugins for working with Docker

# All files are GPL-3.0-or-later, except the following files, which are originally
# from the Docker Python SDK.
# rg --pcre2 -g '!tests/sanity/extra/licenses.py' 'SPDX-License-Identifier: (?!GPL-3\.0-or-later)' | sort | sed 's|^|# |'
#
# plugins/module_utils/_api/api/client.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/api/daemon.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/auth.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/constants.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/credentials/constants.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/credentials/errors.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/credentials/store.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/credentials/utils.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/errors.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/_import_helper.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/tls.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/transport/basehttpadapter.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/transport/npipeconn.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/transport/npipesocket.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/transport/sshconn.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/transport/ssladapter.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/transport/unixconn.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/types/daemon.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/build.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/config.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/decorators.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/fnmatch.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/json_stream.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/ports.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/proxy.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/socket.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/utils.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/api/test_client.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/fake_api.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/fake_stat.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/test_auth.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/test_errors.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/transport/test_sshconn.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/transport/test_ssladapter.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/test_build.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/test_config.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/testdata/certs/ca.pem:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/testdata/certs/cert.pem:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/testdata/certs/key.pem:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/test_decorators.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/test_json_stream.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/test_ports.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/test_proxy.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/test_utils.py:# SPDX-License-Identifier: Apache-2.0
License:        GPL-3.0-or-later AND Apache-2.0
URL:            %{ansible_collection_url community docker}
%global forgeurl https://github.com/ansible-collections/community.docker
Source0:        %{forgeurl}/archive/%{version}/community.docker-%{version}.tar.gz
Patch0:         build_ignore-unnecessary-files.patch

BuildArch:      noarch

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
BuildRequires:  ansible-collection(community.library_inventory_filtering_v1)
BuildRequires:  ansible-collection(community.internal_test_tools)
BuildRequires:  %{py3_dist requests}
%endif

# This collection contains vendored code from the Docker Python SDK.
Provides:       bundled(python3dist(docker))

%description
ansible-collection-community-docker provides the community.docker Ansible
collection. The collection includes Ansible modules and plugins for working
with Docker.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n community.docker-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%build
%ansible_collection_build

%install
%ansible_collection_install

%check
%if %{with tests}
%ansible_test_unit -c community.library_inventory_filtering_v1 -c community.internal_test_tools
%endif

%files -f %{ansible_collection_filelist}
%license COPYING LICENSES REUSE.toml
%doc README.md CHANGELOG.rst*

%changelog
%autochangelog
