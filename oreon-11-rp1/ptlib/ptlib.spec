%global source0_hash 3a17f01d66301663f76130b425d93c2730f2a33df666982165166ff4653dc2c9
Name:		ptlib
Summary:        Portable Tools Library
Version:	2.10.11
Release:        1%{?dist}
URL:		http://www.opalvoip.org/
License:	MPLv1.0
Source0:        https://download.gnome.org/sources/%{name}/2.10/%{name}-%{version}.tar.xz
Patch1:		ptlib-2.10.10-mga-bison-parameter.patch
Patch2:		ptlib-gcc5.patch
Patch3:		ptlib-gcc8.patch
Patch4:		ptlib-2.10.11-signed_int_overflow.patch
Patch5:		ptlib-2.10.11-openssl11.patch
Patch6:		ptlib-2.10.11-make43.patch
Patch7:		ptlib-pkgconf-no-ldflags.patch
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  expat-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libv4l-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
PTLib (Portable Tools Library) is a moderately large class library that 
has it's genesis many years ago as PWLib (portable Windows Library), a 
method to product applications to run on both Microsoft Windows and Unix 
systems. It has also been ported to other systems such as Mac OSX, VxWorks 
and other embedded systems.

It is supplied mainly to support the OPAL project, but that shouldn't stop
you from using it in whatever project you have in mind if you so desire. 

%package devel
Summary:	Development package for ptlib
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
%description devel
The ptlib-devel package includes the libraries and header files for ptlib.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 
%patch -P1 -p1 -b .bison
%patch -P2 -p1 -b .gcc5
%patch -P3 -p1 -b .gcc8
%patch -P4 -p1 -b .signed_int_overflow
%patch -P5 -p1 -b .openssl11
%patch -P7 -p1

sed -i 's#bits/atomicity.h#ext/atomicity.h#g' configure*
sed -i 's#bits/atomicity.h#ext/atomicity.h#g' include/ptlib/critsec.h

%build

export CFLAGS="%{optflags} -DLDAP_DEPRECATED"
export CXXFLAGS="%{optflags} -std=gnu++98"
export STDCXXFLAGS="%{optflags} -std=gnu++98"
%configure --prefix=%{_prefix} --disable-static --enable-plugins --disable-oss --enable-v4l2 --disable-avc --disable-v4l --enable-pulse --enable-ipv6
%make_build
%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
perl -pi -e 's@PTLIBDIR.*=.*@PTLIBDIR = /usr/share/ptlib@' %{buildroot}%{_datadir}/ptlib/make/ptbuildopts.mak
find %{buildroot}%{_libdir} -name '*.so*' -type f -exec chmod +x {} \;
find %{buildroot} -name '*.a' -delete
chmod -R u+w %{buildroot}/*
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ptlib-devel -f %{oreon_filedir}/ptlib-devel.list

%changelog

%autochangelog
