%global source0_hash 2af4e38b33ecf129d0d32e5c7c77f5d162caaca29367ccab101c7c24142eb4cb
%global forgeurl https://github.com/ansible-collections/community.internal_test_tools
%bcond tests 1
Name:           ansible-collection-community-internal_test_tools
Version:        0.19.0
%global tag     %{version}
%forgemeta
Release:        1%{?dist}
Summary:        Internal test tools for other collections
License:        GPL-3.0-or-later
URL:            %{ansible_collection_url community internal_test_tools}
Source0:        %{forgeurl}/archive/%{version}/community.internal_test_tools-%{version}.tar.gz
Patch:          build_ignore.patch
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ansible-packaging
BuildRequires:  ansible-packaging-tests
# /oreon:deps
%description
The community.library_inventory_filtering_v1 collection includes helpers for
use with other collections that allow inventory plugins to offer common
filtering functionality.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 %{forgesetupargs}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
sed -i 's|^#!/usr/bin/env python|#!%{python3}|' \
    tests/sanity/extra/*.py

%build

%ansible_collection_build
%install
%ansible_collection_install
%oreon_autofiles main

%check

%ansible_test_unit
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
