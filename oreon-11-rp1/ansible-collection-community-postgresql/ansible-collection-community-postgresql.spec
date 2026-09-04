%global source0_hash 1727285652fe0231f64fa43800d07c9151a361223a003c5d302772057aa619bb

%bcond tests %{undefined rhel}

Name:           ansible-collection-community-postgresql
Version:        4.2.0
Release:        1%{?dist}
Summary:        Manage PostgreSQL with Ansible

# See the license files in the repo root and file headers
License:        GPL-3.0-or-later AND BSD-2-Clause AND PSF-2.0
URL:            %{ansible_collection_url community postgresql}
Source:         https://github.com/ansible-collections/community.postgresql/archive/%{version}/community.postgresql-%{version}.tar.gz
# build_ignore development files, tests, and docs
Patch:          build_ignore.patch

BuildArch:      noarch

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
BuildRequires:  %{py3_dist psycopg}
%endif

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

%check
%if %{with tests}
%ansible_test_unit
%endif

%files -f %{ansible_collection_filelist}
%license COPYING PSF-license.txt simplified_bsd.txt
%doc README.md CHANGELOG.rst

%changelog
%autochangelog
