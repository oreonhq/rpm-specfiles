%global source0_hash none

%define libmatchbox_devel_ver 1.9-2
%define alphatag 20070628svn

%define _legacy_common_support 1

Summary:       Window manager for the Matchbox Desktop
Name:          matchbox-window-manager
Version:       1.2
Release:       40.%{alphatag}%{?dist}
Url:           http://matchbox-project.org/
License:       GPL-2.0-or-later
Source0:       https://deb.debian.org/debian/pool/main/m/matchbox-window-manager/matchbox-window-manager_1.2.2%2Bgit20200512.orig.tar.xz#/matchbox-window-manager-%{version}-%{alphatag}.tar.gz

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
_tar="matchbox-window-manager-%{version}-%{alphatag}.tar.gz"
if test ! -f "$_tar"; then
  curl -sfL -o _mbw.tar.xz "https://deb.debian.org/debian/pool/main/m/matchbox-window-manager/matchbox-window-manager_1.2.2%2Bgit20200512.orig.tar.xz"
  rm -rf _mbw && mkdir _mbw && tar xJf _mbw.tar.xz -C _mbw --strip-components=1
  tar czf "$_tar" -C _mbw .
  rm -rf _mbw _mbw.tar.xz
fi
test "%{source0_hash}" = "none" || { f="$_tar"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P1 -p1

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
