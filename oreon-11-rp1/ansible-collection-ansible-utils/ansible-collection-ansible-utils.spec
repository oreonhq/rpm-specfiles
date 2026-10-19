%global source0_hash 07726b6653d77cf45cad24b73d5799d2ac62c21e2c455b056296b69027426506
%global collection_namespace ansible
%global collection_name utils
Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        6.1.1
Release:        1%{?dist}
Summary:        Ansible Network Collection for Common Code
License:        GPL-3.0-or-later
URL:            %{ansible_collection_url}
Source0:        https://github.com/ansible-collections/ansible.utils/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  ansible-packaging
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ansible.utils-%{version}
sed -i -e '/version:/s/null/%{version}/' galaxy.yml
find -type f ! -executable -type f -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
rm -fvr tests/integration tests/unit bindep.txt .pre-commit-config.yaml .yamllint changelogs/fragments/.keep
find -type f -name '.gitignore' -print -delete

%build

%ansible_collection_build
%install
%ansible_collection_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
