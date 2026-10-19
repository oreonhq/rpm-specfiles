%global source0_hash 6e1ce7eedae713b11db82f11434d455d8a1379f783a79812cd2e05fc024a8d9f
Summary:        A library of handy utility functions
Name:		glib
Epoch:		1
Version:	1.2.10
Release:        77%{?dist}
License:	LGPL-2.0-or-later
URL:		http://www.gtk.org/
Source0:        https://ftp.gnome.org/pub/gnome/sources/glib/1.2/glib-%{version}.tar.gz
Source1:	config.guess
Source2:	config.sub
Patch1: glib-1.2.10-isowarning.patch
Patch2: glib-1.2.10-gcc34.patch
Patch3: glib-1.2.10-underquoted.patch
Patch4: glib-1.2.10-no_undefined.patch
Patch5: glib-1.2.10-multilib.patch
Patch6: glib-1.2.10-unused-dep.patch
Patch7: glib-1.2.10-autotools.patch
Patch8: glib-1.2.10-format.patch
Patch9: glib-1.2.10-gcc5.patch
Patch10: glib-1.2.10-gcc9.patch
Patch11: glib-1.2.10-c99.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
GLib is a handy library of utility functions. This C library is
designed to solve some portability problems and provide other useful
functionality that most programs require.

%package devel
Summary: Libraries and header files for %{name} development 
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: pkgconfig
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 

%patch -P  1 -p1 -b .isowarning
%patch -P  2 -p1 -b .gcc34
%patch -P  3 -p1 -b .underquoted
%patch -P  4 -p1 -b .no_undefined
%patch -P  5 -p1 -b .multilib
%patch -P  6 -p1 -b .unused-dep
%patch -P  7 -p0 -b .autotools
%patch -P  8 -p0 -b .format
%patch -P  9 -p0 -b .gcc5
%patch -P 10 -p0 -b .gcc9
%patch -P 11 -p1 -b .c99

# The original config.{guess,sub} do not work on x86_64, aarch64 etc.
#
cp -p %{SOURCE1} %{SOURCE2} .
chmod -c +x config.{guess,sub}

%build

%if 0%{?set_build_flags:1}
%global build_type_safety_c 0
%set_build_flags
%endif
LIBTOOL=%{_bindir}/libtool \
%configure --disable-static
%make_build LIBTOOL=%{_bindir}/libtool
%install
%make_install \
	INSTALL="install -p" \
	LIBTOOL=%{_bindir}/libtool
chmod -c a+x %{buildroot}%{_libdir}/lib*.so*
rm -rf %{buildroot}%{_infodir}
rm -rf %{buildroot}%{_libdir}/lib*.la
rm -rf %{buildroot}%{_libdir}/lib*.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check LIBTOOL=%{_bindir}/libtool
%files -f %{oreon_filedir}/main.list
%files -n glib-devel -f %{oreon_filedir}/glib-devel.list

%changelog

%autochangelog
