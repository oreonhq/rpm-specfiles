%global source0_hash d04e826c494c176d1a9563a4f55de84568492281d68030b262acb2ab83296d8c
%bcond_with tests
Name:           ansible-collection-community-mysql
Version:        5.0.2
Release:        1%{?dist}
Summary:        MySQL collection for Ansible
License:        GPL-3.0-or-later AND PSF-2.0 AND BSD-2-Clause
URL:            %{ansible_collection_url community mysql}
Source0:        https://github.com/ansible-collections/community.mysql/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          build_ignore.patch
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

%autosetup -n community.mysql-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%build

%ansible_collection_build
%install
%ansible_collection_install
%oreon_autofiles main
%if %{with tests}
%check

%ansible_test_unit
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
