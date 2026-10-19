%global source0_hash b8d3eed58eb99d949a1d92a24b116c2e0e14a8760083fe10f88bbcf041bbff04
Name:           ansible-collection-community-general
Version:        13.4.0
Release:        1%{?dist}
Summary:        Modules and plugins supported by Ansible community
License:        GPL-3.0-or-later AND BSD-2-Clause AND MIT AND PSF-2.0
URL:            %{ansible_collection_url community general}
%global furl    https://github.com/ansible-collections/community.general
Source0:        %{furl}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          build_ignore.patch
Requires:       ansible-core > 2.11
BuildArch:      noarch
# oreon:deps
BuildRequires:  ansible-packaging
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n community.general-%{version} -p1
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%build

%ansible_collection_build
%install
%ansible_collection_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
