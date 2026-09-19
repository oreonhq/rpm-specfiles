%global source0_hash a1e9d45a0d4dd367f1371dd477e30ecaa95e59b9fb8635dc9e7f26e4eb231d90

Name:           libwiimote
Version:        0.4
Release:        41%{?dist}
Summary:        Simple Wiimote Library for Linux

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://libwiimote.sf.net/
Source0:        http://downloads.sf.net/%{name}/%{name}-%{version}.tgz

Patch0:		libwiimote-0.4-fpic.patch
Patch1:		libwiimote-0.4-includedir.patch
Patch2:		libwiimote-0.4-dso-symlinks.patch
Patch3:		libwiimote-0.4-soname.patch
Patch4:		libwiimote-0.4-bluez4.patch

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  bluez-libs-devel
BuildRequires: make

%description
Libwiimote is a C-library that provides a simple API for communicating with
the Nintendo Wii Remote (aka. wiimote) on a Linux system. The goal of this
library is to be a complete and easy to use framework for interfacing
applications with the wiimote.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .fpic
%patch -P1 -p1 -b .includedir
%patch -P2 -p1 -b .dso-symlinks
%patch -P3 -p1 -b .soname
%patch -P4 -p1 -b .bluez4

%build
autoconf
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' | xargs rm -f
# boo static libraries.  hooray beer!
rm $RPM_BUILD_ROOT%{_libdir}/*.a

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
#%doc
%{_includedir}/*
%{_libdir}/*.so

%changelog
%autochangelog
