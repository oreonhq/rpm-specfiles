%global source0_hash 3a081805979bfa54b7443cbbd03e42ce5a3770e12088c1d828185a343f9e0286
%global _docdir_fmt %{name}
Name:           ansible-collection-ansible-netcommon
Version:        8.7.1
Release:        1%{?dist}
Summary:        Ansible Network Collection for Common Code
License:        GPL-3.0-or-later AND BSD-2-Clause
URL:            %{ansible_collection_url ansible netcommon}
Source0:        https://github.com/ansible-collections/ansible.netcommon/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  ansible-packaging
BuildRequires:  python3dist(pyyaml)
# /oreon:deps
%description
The Ansible ansible.netcommon collection includes common content to help
automate the management of network, security, and cloud devices. This includes
connection plugins, such as network_cli, httpapi, and netconf.

%package        doc
Summary:        %{summary} - Docs
%description    doc
The Ansible ansible.netcommon collection includes common content to help
automate the management of network, security, and cloud devices. This includes
connection plugins, such as network_cli, httpapi, and netconf.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ansible.netcommon-%{version} -p1
find -type f ! -executable -type f -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

# Patch galaxy.yml to exclude unnecessary files from the built collection.
# This is a downstream only patch.
%{python3} - <<EOF
import yaml

build_ignores = """
- .pre-commit-config.yaml
- .gitignore
- .yamllint
- .github
- .flake8
- .isort.cfg
- .prettierignore
- tests
- changelogs/fragments/
- requirements.txt
- test-requirements.txt
- tox.ini
# We install these files with %%doc/%%license. We don't want them duplicated.
- CHANGELOG.rst
- README.md
- LICENSE
- LICENSES
- docs
"""
ignores = yaml.safe_load(build_ignores)
with open("galaxy.yml") as fp:
    data = yaml.safe_load(fp)
data.setdefault("build_ignore", []).extend(ignores)
with open("galaxy.yml", "w") as fp2:
    yaml.safe_dump(data, fp2)
EOF

%build

%ansible_collection_build
%install
%ansible_collection_install
%oreon_autofiles ansible-collection-ansible-netcommon-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ansible-collection-ansible-netcommon-doc -f %{oreon_filedir}/ansible-collection-ansible-netcommon-doc.list

%changelog

%autochangelog
