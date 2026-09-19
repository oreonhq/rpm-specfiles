%global source0_hash ef87ee7e06970d35a32b94207f1f7fb7689c12918ce6d4591dff756985f994dc

%global collection_namespace kubernetes
%global collection_name core
%global forgeurl https://github.com/ansible-collections/%{collection_namespace}.%{collection_name}

# Only run tests where %%generate_buildrequires and test deps are available.
%if 0%{?fedora} || 0%{?rhel} >= 9
%bcond_without     tests
%else
%bcond_with        tests
%endif

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        2.3.2
%global tag     %{version}
%forgemeta
Release:        13%{?dist}
Summary:        Ansible content for working with Kubernetes and OpenShift clusters

# All files are GPL-3.0-or-later (GPLv3+) except:
# ./plugins/module_utils/apply.py: Apache License 2.0
# ./plugins/module_utils/copy.py: Apache License 2.0
# ./plugins/module_utils/exceptions.py: Apache License 2.0
# ./plugins/module_utils/hashes.py: Apache License 2.0
# ./plugins/module_utils/k8sdynamicclient.py: Apache License 2.0
# ./plugins/module_utils/selector.py: Apache License 2.0
# ./plugins/module_utils/client/discovery.py: Apache License 2.0
# ./plugins/module_utils/client/resource.py: Apache License 2.0
# ./plugins/module_utils/_version.py: PSF-2.0

# SPDX-License-Identifier: GPL-3.0-or-later AND Apache-2.0 AND PSF-2.0
# Automatically converted from old format: GPLv3+ and ASL 2.0 and Python - review is highly recommended.
License:        GPL-3.0-or-later AND Apache-2.0 AND LicenseRef-Callaway-Python
URL:            %{ansible_collection_url}
Source0:        %{forgesource}

BuildArch:      noarch

# Needed for %%pyroject_buildrequires
Buildrequires:  python3-devel

BuildRequires:  ansible-packaging
# The new ansible-core, specifically, is required for the `build_ignore:` patch and ansible-test to work properly.
# Therefore, we cannot rely on ansible-packaging which might pull in ansible 2.9.
BuildRequires:  ansible-core
%if %{with tests}
BuildRequires:  ansible-packaging-tests
%endif

%global _description %{expand:
%{name} provides the %{collection_namespace}.%{collection_name} (formerly known as community.kubernetes) Ansible collection.

The collection includes a variety of Ansible content to help automate the management of applications in Kubernetes and OpenShift clusters, as well as the provisioning and maintenance of clusters themselves.}

%description
%wordwrap -v _description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
# Exclude some files from being installed
cat << EOF >> galaxy.yml
  - .github
  - .package_note-%{name}*
  - .pyproject-builddir
  - .gitignore
  - .yamllint
  - setup.cfg
  - codecov.yml
  - tox.ini
  - Makefile
  - tests
# These files are installed into /usr/share/doc and /usr/share/license.
# We don't want to duplicate them in %%{ansible_collection_files}.
  - LICENSE
  - PSF-license.txt
  - README.md
  - CONTRIBUTING.md
  - CHANGELOG.rst
  - docs
EOF

%if %{with tests}
%generate_buildrequires
%pyproject_buildrequires -N tests/unit/requirements.txt
%endif

%build
%ansible_collection_build

%install
%ansible_collection_install

%check
%if %{with tests}
mkdir -p ../ansible_collections/%{collection_namespace}
cp -a $(pwd) ../ansible_collections/%{collection_namespace}/%{collection_name}
pushd ../ansible_collections/%{collection_namespace}/%{collection_name}
ansible-test units --python-interpreter %{python3} --local
popd
%endif

%files
%license LICENSE PSF-license.txt
%doc README.md CHANGELOG.rst CONTRIBUTING.md docs
%{ansible_collection_files}

%changelog
%autochangelog
