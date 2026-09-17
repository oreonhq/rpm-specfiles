%global source0_hash none

Name: gtk-gnutella
Summary: GUI based Gnutella Client
Version: 1.2.3
Release: 5%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://gtk-gnutella.sourceforge.net
Source0: http://sourceforge.net/projects/gtk-gnutella/files/gtk-gnutella-%{version}.tar.xz
Source1: gtk-gnutella-recalculate-sha1.sh
Patch0: gtk-gnutella-configure-c99.patch

BuildRequires: gcc

%if 0%{!?_with_gtk1:1}
BuildRequires: gtk2-devel, libglade2-devel
%else
BuildRequires: gtk+-devel, libglade-devel
%endif
BuildRequires: libxml2-devel, byacc, groff, gettext

BuildRequires: gnutls-devel >= 1.0.16, dbus-devel >= 0.35.2

BuildRequires: desktop-file-utils >= 0.2.90
BuildRequires: make

%description
Gtk-Gnutella is a GUI based Gnutella p2p servent. It's a fully featured  
servent designed to share any type of file.  Gtk-gnutella implements 
compressed gnutella net connections, ultrapeer and leaf nodes and uses 
Passive/Active Remote Queuing (PARQ), and other modern gnutella network 
features.

%prep
%autosetup -p1

%build
./Configure -O -Dprefix=%{_prefix} -Dbindir=%{_bindir} \
	-Dglibpth="/%{_lib} %{_libdir}" \
	-Dprivlib=%{_datadir}/%{name} -Dsysman=%{_mandir}/man1 \
	-Dccflags="%{optflags} -std=gnu99" -Dcc="%{__cc}" -Dyacc="byacc" \
	-Dgtkversion=%{?_with_gtk1:1}%{!?_with_gtk1:2} \
	-Dofficial=true -ders
make #%{?_smp_mflags}

%install

%global	__os_install_post	%__os_install_post\
	%{SOURCE1} %{buildroot}%{_bindir}/%{name} %{buildroot}/%{_datadir}/%{name}/*-linux/%{name}.nm\
%{nil}

make install INSTALL_PREFIX=$RPM_BUILD_ROOT
make install.man INSTALL_PREFIX=$RPM_BUILD_ROOT

chmod 0755 $RPM_BUILD_ROOT%{_bindir}/*

rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/*.svg
install -D -m 644 extra_files/gtk-gnutella.16.png \
	$RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/16x16/apps/gtk-gnutella.png
install -D -m 644 extra_files/gtk-gnutella.32.png \
	$RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/gtk-gnutella.png
install -D -m 644 extra_files/gtk-gnutella.png \
	$RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/gtk-gnutella.png
install -D -m 644 extra_files/gtk-gnutella.svg \
	$RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/scalable/apps/gtk-gnutella.svg

desktop-file-install --delete-original	\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	$RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/gtk-gnutella
%{_datadir}/appdata/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*

%doc README TODO AUTHORS LICENSE GEO_LICENSE doc/other/shell.txt

%changelog
%autochangelog
