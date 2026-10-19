%global source0_hash b0dad852959b515b8fbfd1ed552e362340347d26d5246e7f1b973027131eb1da
%global xfceversion 4.20
%global _hardened_build 1
%global debug_package %{nil}
Name:           thunar-volman
Version:        4.20.0
Release:        1%{?dist}
Summary:        Automatic management of removable drives and media for Thunar
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
Requires:       Thunar >= %{xfceversion}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  exo-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libgudev1-devel
BuildRequires:  libnotify-devel
BuildRequires:  libxfce4ui-devel
BuildRequires:  make
BuildRequires:  xfconf
# /oreon:deps
%description
The Thunar Volume Manager is an extension for the Thunar file manager, which 
enables automatic management of removable drives and media. For example, if 
thunar-volman is installed and configured properly, and you plug in your 
digital camera, it will automatically launch your preferred photo application 
and import the new pictures from the camera into your photo collection.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup

sed -i 's/XFCE;//' thunar-volman-settings/thunar-volman-settings.desktop.in.in

%build

%configure
%make_build
%install
%make_install
%find_lang %{name}
desktop-file-install \
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
    --add-only-show-in=XFCE                                 \
    --delete-original                                       \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}-settings.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
