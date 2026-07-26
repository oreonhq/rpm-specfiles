%global source0_hash 122b1e03966d63ec3389decf5440fb94285907d1b6be48352dcf6aca292cf7b0

Name:           gnome-sharp
Version:        2.24.2
Release:        40%{?dist}
Summary:        GTK+ and GNOME bindings for Mono

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            ftp://ftp.gnome.org/pub/gnome/sources/gnome-sharp/2.24/
Source0:        ftp://ftp.gnome.org/pub/gnome/sources/gnome-sharp/2.24/gnome-sharp-%{version}.tar.bz2

Patch0: %{name}-2241-getopts.patch
# init gtype before using gconf
Patch2: gnome-sharp-gconf-init.patch
# https://github.com/meebey/gnome-sharp/commit/e9d06b56a54dcd399d1d3eaaf62bdacb7e07084d
Patch3: gnome-sharp-2.24.2-dbus-thread-fix.patch
# https://github.com/mono/gnome-sharp/commit/d797ce61a18f8238acd2f9a7bf97b157ae70b443
Patch4: gnome-sharp-2.24.2-canvaspathdef.patch
# https://github.com/mono/gnome-sharp/commit/cfabe1b0a581f8cd10ec75d347a93ebc1c365ac7
Patch5: gnome-sharp-2.24.2-gconf-path.patch

BuildRequires:  mono-devel gtk2-devel libart_lgpl-devel gnome-vfs2-devel libgnomecanvas-devel libgnomeui-devel
BuildRequires:  gtk-sharp2-devel >= 2.12.7
BuildRequires:  gtk-sharp2-gapi >= 2.12.7
BuildRequires:  librsvg2-devel vte291-devel
BuildRequires:  automake, libtool
BuildRequires: make

# Mono only available on these:
ExclusiveArch: %mono_arches

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
#sed -i -e 's!-r:Mono.GetOptions.dll! !' sample/gnomevfs/Makefile.in
export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}
%configure
make

%install
export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.*a

%ldconfig_scriptlets

%files
%doc COPYING ChangeLog README
%{_bindir}/gconfsharp2-schemagen
%{_prefix}/lib/gtk-sharp-2.0/gconfsharp-schemagen.exe
%{_libdir}/*.so
%{_prefix}/lib/mono/gac
%{_prefix}/lib/mono/gtk-sharp-2.0/*.dll
%{_datadir}/gapi-2.0/*

%files devel
%{_libdir}/pkgconfig/*-sharp-2.0.pc
%{_libdir}/pkgconfig/gconf-sharp-peditors-2.0.pc

%changelog
%autochangelog
