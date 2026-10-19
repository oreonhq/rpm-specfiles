%global source0_hash 965bcbf2fade34bd621c8eb5c8044278b33c85779473e550834e2bcb828ba6e6
%bcond tests %{undefined rhel}
Name:           ansible-collection-community-postgresql
Version:        5.0.0
Release:        1%{?dist}
Summary:        Manage PostgreSQL with Ansible
License:        GPL-3.0-or-later AND BSD-2-Clause AND PSF-2.0
URL:            %{ansible_collection_url community postgresql}
Source0:        https://github.com/ansible-collections/community.postgresql/archive/%{version}/community.postgresql-%{version}.tar.gz
Patch:          build_ignore.patch
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ansible-packaging
BuildRequires:  ansible-packaging-tests
BuildRequires:  python3dist(psycopg)
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n community.postgresql-%{version}
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
