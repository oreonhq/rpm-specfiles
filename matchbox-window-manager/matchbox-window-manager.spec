%define libmatchbox_devel_ver 1.9-2
%define alphatag 20070628svn

# https://src.fedoraproject.org/rpms/redhat-rpm-config/blob/master/f/buildflags.md#legacy-fcommon
%define _legacy_common_support 1

Summary:       Window manager for the Matchbox Desktop
Name:          matchbox-window-manager
Version:       1.2
Release:       40.%{alphatag}%{?dist}
Url:           http://matchbox-project.org/
# svn checkout http://svn.o-hand.com/repos/matchbox/trunk/matchbox-window-manager
License:       GPL-2.0-or-later
Source0:       %{name}-%{version}-%{alphatag}.tar.gz

Patch1: matchbox-window-manager-1.2-keysyms.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig 
BuildRequires:  expat-devel
BuildRequires:  libmatchbox-devel >= %{libmatchbox_devel_ver}
BuildRequires:  startup-notification-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pango-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXcursor-devel
Requires:       filesystem

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains the window manager from Matchbox.

%prep
%autosetup -p 2

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS README ChangeLog COPYING
%{_bindir}/*
%dir %{_sysconfdir}/matchbox
%config(noreplace) %{_sysconfdir}/matchbox/kbdconfig
%dir %{_datadir}/matchbox
%{_datadir}/matchbox/*
%{_datadir}/themes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2-40.
- Prepare for Oreon 11 (RP1)
