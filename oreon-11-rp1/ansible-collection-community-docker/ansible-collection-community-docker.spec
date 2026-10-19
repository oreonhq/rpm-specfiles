%global source0_hash cb0cd67e225b9f0f3c50da36e3c4a79f7f4afdde14a94cd54e567210183e6a9f
%bcond_with tests
Name:           ansible-collection-community-docker
Version:        5.3.0
Release:        1%{?dist}
Summary:        Ansible modules and plugins for working with Docker
License:        GPL-3.0-or-later AND Apache-2.0
URL:            %{ansible_collection_url community docker}
%global forgeurl https://github.com/ansible-collections/community.docker
Source0:        %{forgeurl}/archive/%{version}/community.docker-%{version}.tar.gz
Patch0:         build_ignore-unnecessary-files.patch
BuildArch:      noarch
%if %{with tests}
%endif
Provides:       bundled(python3dist(docker))
# oreon:deps
BuildRequires:  ansible-collection(community.internal_test_tools)
BuildRequires:  ansible-collection(community.library_inventory_filtering_v1)
BuildRequires:  ansible-packaging
BuildRequires:  ansible-packaging-tests
BuildRequires:  python3dist(requests)
# /oreon:deps
%description
ansible-collection-community-docker provides the community.docker Ansible
collection. The collection includes Ansible modules and plugins for working
with Docker.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n community.docker-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%build

%ansible_collection_build
%install
%ansible_collection_install
%oreon_autofiles main

%check

%if %{with tests}
%ansible_test_unit -c community.library_inventory_filtering_v1 -c community.internal_test_tools
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
