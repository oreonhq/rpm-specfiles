%global source0_hash ca7d929194959d905f3a18f1ae25ed2d911af6bf1194c917a3215402ec33ff4f
%bcond_with tests
Name:           ansible-collection-ansible-posix
Version:        2.2.2
Release:        1%{?dist}
Summary:        Ansible Collection targeting POSIX and POSIX-ish platforms
License:        GPL-3.0-or-later AND PSF-2.0
URL:            %{ansible_collection_url ansible posix}
Source0:        https://github.com/ansible-collections/ansible.posix/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Exclude-unnecessary-files-from-built-collection.patch
%if %{with tests}
%endif
BuildArch:      noarch
# oreon:deps
BuildRequires:  ansible-packaging
BuildRequires:  ansible-packaging-tests
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ansible.posix-%{version} -p1
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%build

%ansible_collection_build
%install
%ansible_collection_install
%oreon_autofiles main

%check

%if %{with tests}
%ansible_test_unit
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
