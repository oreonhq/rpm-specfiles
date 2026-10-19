%global source0_hash 04a836033aa582da30a5f1afb917d7dacfa0e11043a910fb2886dc72e5a56e6b
%bcond tests %{undefined rhel}
Name:           ansible-collection-community-crypto
Version:        3.4.0
Release:        1%{?dist}
Summary:        The community.crypto collection for Ansible
License:        GPL-3.0-or-later AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND PSF-2.0
URL:            %{ansible_collection_url community crypto}
Source0:        https://github.com/ansible-collections/community.crypto/archive/%{version}/community.crypto-%{version}.tar.gz
Patch:          build_ignore.patch
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ansible-collection-community-crypto = %{version}-%{release}
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n community.crypto-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%if %{with tests}
%build

%ansible_collection_build
%install
%ansible_collection_install
%oreon_autofiles main

%check

%if %{with tests}
%ansible_test_unit
%endif
%files

%changelog

%autochangelog
%endif
