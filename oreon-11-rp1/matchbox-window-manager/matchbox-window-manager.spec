%global source0_hash a0d869dd182b8e31cd67bd4425db48f66ada4f4163e57b9b796304f5a022abcd

%define libmatchbox_devel_ver 1.9-2
%define alphatag 20070628svn

%define _legacy_common_support 1

Summary:       Window manager for the Matchbox Desktop
Name:          matchbox-window-manager
Version:       1.2
Release:       40.%{alphatag}%{?dist}
Url:           http://matchbox-project.org/
License:       GPL-2.0-or-later
Source0:       https://deb.debian.org/debian/pool/main/m/matchbox-window-manager/matchbox-window-manager_1.2.2%2Bgit20200512.orig.tar.xz

Patch1:        matchbox-window-manager-1.2-keysyms.patch

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n matchbox-window-manager
%patch1 -p1

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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2-40.20070628svn
- Import
