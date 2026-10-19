%global source0_hash aad4c1acd767b2df2f8aecf4c8fe9c58aafe6c4cd0dbf6d7d2e164c4be24964d
%global forgeurl https://github.com/ansible-collections/community.library_inventory_filtering
%bcond tests 1
Name:           ansible-collection-community-library_inventory_filtering_v1
Version:        1.1.5
%global tag     %{version}
%forgemeta
Release:        1%{?dist}
Summary:        Library collection with helpers for inventory plugins
License:        GPL-3.0-or-later
URL:            %{ansible_collection_url community library_inventory_filtering_v1}
Source0:        %{forgeurl}/archive/%{version}/community.library_inventory_filtering-%{version}.tar.gz
Patch:          0001-galaxy.yml-add-unnecessary-files-to-build_ignore.patch
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ansible-collection(community.internal_test_tools)
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

%build

%ansible_collection_build
%install
%ansible_collection_install
%oreon_autofiles main

%check

%if %{with tests}
%ansible_test_unit -c community.internal_test_tools
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
