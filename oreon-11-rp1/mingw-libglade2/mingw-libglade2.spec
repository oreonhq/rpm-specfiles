%global source0_hash 64361e7647839d36ed8336d992fd210d3e8139882269bed47dc4674980165dec
%?mingw_package_header
Name:           mingw-libglade2
Version:        2.6.4
Release:        43%{?dist}
Summary:        MinGW Windows Libglade2 library
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/libglade/2.6/libglade-%{version}.tar.bz2
Patch1:         libglade-2.0.1-nowarning.patch
Patch2:         libglade-secondary.patch
Patch3:         libglade-link-against-gmodule.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  gtk2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-fontconfig
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-gtk2
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-pango
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-fontconfig
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-gtk2
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-pango
# /oreon:deps
%description
MinGW Windows Libglade2 library.

# Win32
%package -n mingw32-libglade2
Summary:        MinGW Windows Libglade2 library
Requires:       pkgconfig
%description -n mingw32-libglade2
MinGW Windows Libglade2 library.

%package -n mingw32-libglade2-static
Summary:        Static MinGW Windows Libglade2 library
Requires:       mingw32-libglade2 = %{version}-%{release}
%description -n mingw32-libglade2-static
Static MinGW Windows Libglade2 library.

# Win64
%package -n mingw64-libglade2
Summary:        MinGW Windows Libglade2 library
Requires:       pkgconfig
%description -n mingw64-libglade2
MinGW Windows Libglade2 library.

%package -n mingw64-libglade2-static
Summary:        Static MinGW Windows Libglade2 library
Requires:       mingw64-libglade2 = %{version}-%{release}
%description -n mingw64-libglade2-static
Static MinGW Windows Libglade2 library.

%?mingw_debug_package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libglade-%{version}
%patch -P1 -p1 -b .nowarning
%patch -P2 -p1 -b .secondary
%patch -P3 -p0 -b .gmodule

autoreconf --install --force

%build

%mingw_configure --disable-gtk-doc
cp glade/glade.def build_win32/glade
cp glade/glade.def build_win64/glade
%mingw_make %{?_smp_mflags}
%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT/%{mingw32_datadir}/gtk-doc/html/libglade
rm -rf $RPM_BUILD_ROOT/%{mingw64_datadir}/gtk-doc/html/libglade
find $RPM_BUILD_ROOT -name "*.la" -delete
%oreon_autofiles mingw32-libglade2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libglade2-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libglade2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libglade2-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libglade2 -f %{oreon_filedir}/mingw32-libglade2.list
%files -n mingw32-libglade2-static -f %{oreon_filedir}/mingw32-libglade2-static.list
%files -n mingw64-libglade2 -f %{oreon_filedir}/mingw64-libglade2.list
%files -n mingw64-libglade2-static -f %{oreon_filedir}/mingw64-libglade2-static.list

%changelog

%autochangelog
