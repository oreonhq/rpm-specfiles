%global source0_hash 11356e4242151b9014fa6209c1f0360b699b72ef8ab47dbeb81cc23be7db9049

%global	mainver	2.2.3
%global	minorver	1

Name:		uget
Version:	%{mainver}
Release:	16%{?minorver:.respin%minorver}%{?dist}
Summary:	Download manager using GTK+ and libcurl

# Overall		LGPL-2.1-or-later
# uget/pwmd.c	GPL-2.0-or-later (unused)
# SPDX confirmed
License:	LGPL-2.1-or-later
URL:		http://ugetdm.com/
Source0:	http://downloads.sourceforge.net/urlget/%{name}-%{mainver}%{?minorver:-%minorver}.tar.gz
Patch0:		uget-2.2.3-gcc10-fno-common.patch
Patch1:		uget-2.2.3-c23-function-proto.patch

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(appindicator3-0.1)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	intltool
BuildRequires:	libcurl-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	pkgconfig(libnotify)

Obsoletes:	urlgfe < 1.0.4
Provides:	urlgfe = %{version}

%description
uGet is a download manager with downloads queue, pause/resume, 
clipboard monitor, batch downloads, browser integration (Firefox & Chrome), 
multiple connections, speed limit controls, powerful category based control
and much more. Each Category has an independent configuration that can
be inherited by each download in that category.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{mainver}
%patch -P0 -p1 -b .gcc10
%patch -P1 -p1 -b .c23

%global optflags_orig %optflags
%global optflags %optflags -Werror=implicit-function-declaration

%build
%configure \
	--with-gnutls \
	--without-openssl

%make_build

%install
%make_install
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--delete-original \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}-gtk.desktop

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc	AUTHORS
%license	COPYING
%doc	ChangeLog
%doc	README
%{_bindir}/%{name}-gtk
%{_bindir}/%{name}-gtk-1to2

%{_datadir}/applications/%{name}-gtk.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%{_datadir}/sounds/%{name}/
%dir	%{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}/logo.png

%changelog
%autochangelog
