%global source0_hash ca7d929194959d905f3a18f1ae25ed2d911af6bf1194c917a3215402ec33ff4f

%if %{undefined rhel}
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           ansible-collection-ansible-posix
Version:        2.2.2
Release:        1%{?dist}
Summary:        Ansible Collection targeting POSIX and POSIX-ish platforms

# plugins/module_utils/mount.py: Python Software Foundation License version 2
License:        GPL-3.0-or-later AND PSF-2.0
URL:            %{ansible_collection_url ansible posix}
Source:         https://github.com/ansible-collections/ansible.posix/archive/%{version}/%{name}-%{version}.tar.gz
# Exclude unneceesary development files and duplicate docs from the built
# collection. This is a downstream only patch. Upstreams include these files
# for reasons that are irrelevant to Fedora.
Patch0:         0001-Exclude-unnecessary-files-from-built-collection.patch
BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
%endif

BuildArch:      noarch

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

%check
%if %{with tests}
%ansible_test_unit
%endif

%files -f %{ansible_collection_filelist}
%license COPYING PSF-license.txt
%doc README.md CHANGELOG.rst

%changelog
%autochangelog
