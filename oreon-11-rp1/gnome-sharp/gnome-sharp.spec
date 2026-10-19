%global source0_hash 122b1e03966d63ec3389decf5440fb94285907d1b6be48352dcf6aca292cf7b0
Name:           gnome-sharp
Version:        2.24.2
Release:        40%{?dist}
Summary:        GTK+ and GNOME bindings for Mono
License:        LicenseRef-Callaway-LGPLv2+
URL:            ftp://ftp.gnome.org/pub/gnome/sources/gnome-sharp/2.24/
Source0:        ftp://ftp.gnome.org/pub/gnome/sources/gnome-sharp/2.24/gnome-sharp-%{version}.tar.bz2
Patch0: %{name}-2241-getopts.patch
Patch2: gnome-sharp-gconf-init.patch
Patch3: gnome-sharp-2.24.2-dbus-thread-fix.patch
Patch4: gnome-sharp-2.24.2-canvaspathdef.patch
Patch5: gnome-sharp-2.24.2-gconf-path.patch
ExclusiveArch: %mono_arches
# oreon:deps
BuildRequires:  automake
BuildRequires:  gnome-vfs2-devel
BuildRequires:  gtk-sharp2-devel
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  gtk2-devel
BuildRequires:  libart_lgpl-devel
BuildRequires:  libgnomecanvas-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mono-devel
BuildRequires:  vte291-devel
# /oreon:deps
%description
This package provides a library that allows you to build
fully native graphical GNOME applications using Mono. gnome-sharp
extends gtk-sharp2 and adds bindings for gconf, libgnome, gnome-vfs,
libart, librsvg, and vte291.

%package devel
Summary: Files needed for developing with gnome-sharp
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
%description devel
This package provides the necessary development libraries and headers
for writing gnome-sharp2 applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .getopts
%patch -P2 -p1 -b .gconf-init
%patch -P3 -p1 -b .threadfix
%patch -P4 -p1 -b .canvaspathdef
%patch -P5 -p1 -b .gconfpath

%build

autoreconf --force --install
aclocal
export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}
%configure
make
%install
export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.*a
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gnome-sharp-devel -f %{oreon_filedir}/gnome-sharp-devel.list

%changelog

%autochangelog
