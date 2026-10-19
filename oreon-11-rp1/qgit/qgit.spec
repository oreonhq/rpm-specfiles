%global source0_hash 9fa64b011963b7b876b8634b140ec5339a81a422317df71b619fcee5740a364a
Name:           qgit
Version:        2.13
Release:        1%{?dist}
Summary:        GUI browser for git repositories
License:        GPL-2.0-only
URL:            https://github.com/tibirna/qgit
Source0:        https://github.com/tibirna/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Requires:       git-core >= 1.4.0
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  libappstream-glib
# /oreon:deps
%description
With qgit you are able to browse revisions history, view patch content
and changed files, graphically following different development branches.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{name}-%{version}

%build

%cmake
%cmake_build
%install
%cmake_install
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
