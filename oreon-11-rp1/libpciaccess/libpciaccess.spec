Name:           libpciaccess
Version:        0.16
Release:        17%{?dist}
Summary:        PCI access library

License:        HPND AND MIT
URL:            https://www.x.org/

# git snapshot.  To recreate, run
# % ./make-libpciaccess-snapshot.sh %{gitrev}
#Source0:        libpciaccess-%{gitdate}.tar.bz2
Source0:	https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.bz2
Source1:        make-libpciaccess-snapshot.sh

Patch2:		libpciaccess-rom-size.patch

BuildRequires:  autoconf automake libtool pkgconfig xorg-x11-util-macros
BuildRequires: make
Requires:       hwdata

%description
libpciaccess is a library for portable PCI access routines across multiple
operating systems.

%package devel
Summary:        PCI access library development package
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development package for libpciaccess.

%prep
%autosetup -p1

%build
autoreconf -v --install
%configure --disable-static
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS
%{_libdir}/libpciaccess.so.0
%{_libdir}/libpciaccess.so.0.11.*

%files devel
%{_includedir}/pciaccess.h
%{_libdir}/libpciaccess.so
%{_libdir}/pkgconfig/pciaccess.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16-17
- Prepare for Oreon 11 (RP1)
