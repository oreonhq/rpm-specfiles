%global source0_hash 15b680abca6c773ecb85253521fa100dd3b8549befeecc7595b10209d62d66b5

Summary:        Theme engines for GTK+ 2.0
Name:           gtk2-engines
Version:        2.20.2
Release:        34%{?dist}
# This release of gtk-engines is now solely LGPL 2.1 or any later version.
License:        LGPL-2.1-or-later
#VCS: git:git://git.gnome.org/gtk-engines
Source:         http://download.gnome.org/sources/gtk-engines/2.20/gtk-engines-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires: make

URL:            http://download.gnome.org/sources/gtk-engines

# Fedora-specific tweaks
# http://bugzilla.gnome.org/show_bug.cgi?id=593030
Patch0: gtk-engines-2.18.2-change-bullet.patch
# turn on new tooltips look
Patch1: tooltips.patch
# enable automatic mnemonics
Patch2: auto-mnemonics.patch
# allow dragging on empty areas in menubars
Patch3: window-dragging.patch

%description
The gtk2-engines package contains shared objects and configuration
files that implement a number of GTK+ theme engines. Theme engines
provide different looks for GTK+, some of which resemble other
toolkits or operating systems.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The gtk2-engines-devel package contains files needed to develop
software that uses the theme engines in the gtk2-engines package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gtk-engines-%{version}

%patch -P0 -p1 -b .bullet
%patch -P1 -p1 -b .tooltips
%patch -P2 -p1 -b .mnemonics
%patch -P3 -p1 -b .window-dragging

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# no thanks
rm -rf $RPM_BUILD_ROOT%{_datadir}/themes/Redmond
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.4.0/engines/libredmond95.so

%find_lang gtk-engines

%files -f gtk-engines.lang
%doc README AUTHORS NEWS COPYING
%{_libdir}/gtk-2.0/2.10.0/engines/*.so
%{_datadir}/themes/*
%{_datadir}/gtk-engines

%files devel
%{_libdir}/pkgconfig/gtk-engines-2.pc

%changelog
%autochangelog
