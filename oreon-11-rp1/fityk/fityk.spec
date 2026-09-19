%global source0_hash 6da5eb6279d90b241108e36c2d4880cafec82d7225a5d49a28675a07b4360f0b

Name:           fityk
Version:        1.3.2
Release:        12%{?dist}
Summary:        Non-linear curve fitting and data analysis
License:        GPL-2.0-or-later
URL:            http://fityk.nieto.pl/

Source0:        https://github.com/wojdyr/%{name}/archive/v%{version}/%{name}-%{version}.tar.bz2
# patch to check for cmpfit dependency
Patch0:         cmpfit_config.patch

BuildRequires:  boost-devel
BuildRequires:  cmpfit-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
#BuildRequires:  python-sphinx
BuildRequires:  readline-devel
BuildRequires:  swig
BuildRequires:  wxGTK-devel
BuildRequires:  xylib-devel
BuildRequires:  zlib-devel

Requires:       gnuplot

%description
Fityk is a program for nonlinear curve-fitting of analytical
functions (especially peak-shaped) to data (usually experimental
data). It can also be used for visualization of x-y data only.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs that make
use of %{name}, you will need to install %{name}-devel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0

#mv {S:1} doc/
#tar xf {S:2}
#mv img doc/

# remove pre-built documentation
rm -fr doc/html

# change lua version in configure file
sed -i 's/AX_PROG_LUA(5.1, 5.4)/AX_PROG_LUA(5.1, 5.5)/' configure.ac

#unbundle cmpfit
rm -fr fityk/cmpfit
sed -i 's|#include "cmpfit/mpfit.h"|#include "mpfit.h"|' fityk/CMPfit.h
#sed -i 's/swig\/luarun.h \\/swig\/luarun.h/' fityk/Makefile.am
sed -i 's|cmpfit/mpfit.c cmpfit/mpfit.h|mpfit.h|' fityk/Makefile.am

%build
export CFLAGS="%{optflags}" CXXFLAGS="%{optflags} -std=c++14" LDFLAGS="%{optflags} -lmpfit"
autoreconf -iv
%configure

# remove rpath
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

# Temporarily disable building documentation
# needs python-sphinx >=1.5

# build html documentation
#pushd doc
#make pdf
#popd

%install
make install DESTDIR=%{buildroot}
# get rid of libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

#rm -f $RPM_BUILD_ROOT%%{_libdir}/*.la

# SWIG bindings are not packaged, remove samples
rm -f %{buildroot}%{_datadir}/%{name}/samples/*.py*
rm -f %{buildroot}%{_datadir}/%{name}/samples/*.lua
rm -f %{buildroot}%{_datadir}/%{name}/samples/*.pl

#ln -s fityk.1.gz $RPM_BUILD_ROOT%%{_mandir}/man1/cfityk.1.gz

mkdir -p %{buildroot}%{_metainfodir}
cp -p %{buildroot}/usr/share/appdata/%{name}.appdata.xml %{buildroot}%{_metainfodir}/%{name}.appdata.xml
rm -rf %{buildroot}/usr/share/appdata

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/fityk.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%doc NEWS
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/*
%{_libdir}/*.so.*
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{name}.appdata.xml

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/%{name}/samples/*.cc

%changelog
%autochangelog
