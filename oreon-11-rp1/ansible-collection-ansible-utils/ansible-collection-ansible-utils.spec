%global source0_hash d815f05b8173a4cbc9a043bed698434baef3e32a4159e4fb38c3d4127b02ce24

%global collection_namespace ansible
%global collection_name utils

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        6.0.1
Release:        1%{?dist}
Summary:        Ansible Network Collection for Common Code

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            %{ansible_collection_url}
Source:         https://github.com/ansible-collections/ansible.utils/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible-packaging

BuildArch:      noarch

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

%files
%license LICENSE
%doc README.md
%{ansible_collection_files}

%changelog
%autochangelog
