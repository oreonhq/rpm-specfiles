%global source0_hash 692708cd047c7a552f2f85fe2ee32f19c7d5be5bf695d0288e8cadf50289db06
%global minor_version 0.6
%global thunar_version 4.20.0
%global xfceversion 4.20
Name:           thunar-archive-plugin
Version:        0.6.0
Release:        1%{?dist}
Summary:        Archive plugin for the Thunar file manager
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:        http://archive.xfce.org/src/thunar-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.xz
Requires:       Thunar >= %{thunar_version}
# oreon:deps
BuildRequires:  Thunar-devel
BuildRequires:  exo
BuildRequires:  gcc-c++
BuildRequires:  libxfce4util-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  meson
# /oreon:deps
%description
The Thunar Archive Plugin allows you to create and extract archive files using 
the file context menus in the Thunar file manager. Starting with version 0.2.0, 
the plugin provides a generic scripting interface for archive managers. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
