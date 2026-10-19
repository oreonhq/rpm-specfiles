%global source0_hash 98a911d85cae9651081994ba9ac6b6e9a3131c72e3dd368d227a1ada9bbfc4a0
Name:      gnome-app-list
Version:   3.0
Release:        1%{?dist}
BuildArch: noarch
Summary:        A curated list of apps to feature or highlight in GNOME
License:   LGPL-2.1-or-later
URL:       https://gitlab.gnome.org/GNOME/gnome-app-list/
Source0:        https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  /usr/bin/python3
BuildRequires:  /usr/bin/xmllint
BuildRequires:  meson
# /oreon:deps
%description
The %{name} provides an AppStream data, which marks
some apps as featured or highlighted in GNOME.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
