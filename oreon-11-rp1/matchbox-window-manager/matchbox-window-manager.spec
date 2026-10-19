%define libmatchbox_devel_ver 1.9-2
%define alphatag 20070628svn
%define _legacy_common_support 1
Summary:        Window manager for the Matchbox Desktop
Name:          matchbox-window-manager
Version:       1.2
Release:        1%{?dist}
Url:           http://matchbox-project.org/
License:       GPL-2.0-or-later
Source0:        %{name}-%{version}-%{alphatag}.tar.gz
Patch1: matchbox-window-manager-1.2-keysyms.patch
Requires:       filesystem
# oreon:deps
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  libXcomposite-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXrender-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmatchbox-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  pango-devel
BuildRequires:  pkgconfig
BuildRequires:  startup-notification-devel
# /oreon:deps
%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains the window manager from Matchbox.

%prep
%oreon_prep
%build

%configure
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
