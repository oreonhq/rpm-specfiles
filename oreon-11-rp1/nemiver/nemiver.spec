%global source0_hash 331ae34f2d18166199a7012dc777fbc5899e01f3e28909502957fcb6bef6963f

Name:		nemiver
Version:	0.9.6
Release:	28%{?dist}
Summary:	A GNOME C/C++ Debugger

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://projects.gnome.org/nemiver

Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.9/%{name}-%{version}.tar.xz
# Backported from upstream
Patch0:		0001-Fix-compiliation-warnings-errors.patch
Patch1:		0001-Use-RefPtr-bool-operator-in-the-conditions.patch

## The glibmm bits would normally be part of the dependency tree for
## gtksourceviewmm; but we're using GIO here (F9+) so we need to ensure that the
## the Glib/glibmm we're depending on also includes it (e.g., 2.16+)
##
## We specify the minimum version of gtkmm24 because we are now using
## the tooltip and treeview APIs of gtkmm 2.12.7.
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:	boost-devel
BuildRequires:	boost-static
BuildRequires:	desktop-file-utils
BuildRequires:	gdb
BuildRequires:	gettext
#This is useful to get m4 macros from gsettings.m4, like GLIB_GSETTING
# Requiring glib2-devel >= 2.28 is equivalent to requiring the
# glib2-devel of Fedora 15.
BuildRequires:  glib2-devel >= 2.28
BuildRequires:	ghex-devel >= 3.10
BuildRequires:	glibmm24-devel >= 2.46
BuildRequires:	gtkmm30-devel >= 3.18
BuildRequires:	gdlmm-devel >= 3.2.1
BuildRequires:	yelp-tools >= 3.2.0
BuildRequires:	gtksourceviewmm3-devel >= 3.0.0
BuildRequires:	libgtop2-devel >= 2.14
BuildRequires:	libtool
BuildRequires:	perl(XML::Parser)
BuildRequires:	sqlite-devel >= 3.0
BuildRequires:	vte291-devel >= 0.41
BuildRequires:	intltool
BuildRequires:	libxml2-devel >= 2.6.22
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  dconf

Requires: gsettings-desktop-schemas

## Needs hicolor-icon-theme so that the parent %%_datadir/icons/hicolor
## and its subtree directories are properly owned.
Requires:	hicolor-icon-theme
Requires:	gdb
Provides: %{name}-devel = %{version}-%{release}
Provides: %{name}-headers = %{version}-%{release}

Obsoletes:	%{name}-devel < 0.5.4-1
Obsoletes:	%{name}-headers < 0.6.5-2

## Mostly taken from its site index... :]
%description
Nemiver is an ongoing effort to write a standalone graphical debugger that
integrates well in the GNOME desktop environment. It currently features a
backend which uses the well known GNU Debugger (gdb) to debug C/C++ programs.

The yelp package must be installed to make use of Nemiver's documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%configure --disable-static --disable-schemas-install  --disable-scrollkeeper 
# Use system libtool to prevent build scripts from using RPATH hacks.
make %{?_smp_mflags} LIBTOOL=%{_bindir}/libtool

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
desktop-file-install                                    \
	--dir %{buildroot}%{_datadir}/applications	\
	--remove-category=Application			\
	--delete-original				\
	%{buildroot}/%{_datadir}/applications/%{name}.desktop

# # Register as an application to be visible in the software center
# #
# # NOTE: It would be *awesome* if this file was maintained by the upstream
# # project, translated and installed into the right place during `make install`.
# #
# # See http://www.freedesktop.org/software/appstream/docs/ for more details.
# #
# mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
# cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
# <?xml version="1.0" encoding="UTF-8"?>
# <!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
# <!--
# BugReportURL: https://bugzilla.gnome.org/show_bug.cgi?id=708754
# SentUpstream: 2014-09-22
# -->
# <application>
#   <id type="desktop">nemiver.desktop</id>
#   <metadata_license>CC0-1.0</metadata_license>
#   <description>
#     <p>
#       Nemiver is an on-going effort to write a standalone graphical debugger that
#       integrates well in the GNOME desktop environment.
#       It currently features a backend which uses the well known GNU Debugger gdb
#       to debug C / C++ programs.
#     </p>
#     <p>
#       We believe that Nemiver is mature and robust enough to just let you debug
#       your favorite C or C++ application in a pleasant way, as we use it daily
#       for our own debugging purposes.
#     </p>
#   </description>
#   <screenshots>
#     <screenshot type="default">https://projects.gnome.org/nemiver/images/nemiver-main-page.png</screenshot>
#   </screenshots>
#   <url type="homepage">https://projects.gnome.org/nemiver/</url>
#   <updatecontact>nemiver-list@gnome.org</updatecontact>
# </application>
# EOF

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING COPYRIGHT NEWS README TODO 
%exclude %{_includedir}/%{name}
%exclude %{_libdir}/%{name}/*.a
%exclude %{_libdir}/%{name}/*.la
%exclude %{_libdir}/%{name}/modules/*.a
%exclude %{_libdir}/%{name}/modules/*.la
%exclude %{_libdir}/%{name}/plugins/*/*.la
%exclude %{_libdir}/%{name}/plugins/*/*.a
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/glib-2.0/schemas/org.nemiver.gschema.xml
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%{_datadir}/%{name}/
%{_datadir}/help/*
%{_mandir}/man?/%{name}.*

%changelog
%autochangelog
