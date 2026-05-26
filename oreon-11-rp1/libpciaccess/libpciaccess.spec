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
# oreon url source checksums begin
%global source0_sha256 214c9d0d884fdd7375ec8da8dcb91a8d3169f263294c9a90c575bf1938b9f489
%global source0_file libpciaccess-0.16.tar.bz2
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libpciaccess-0.16.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "214c9d0d884fdd7375ec8da8dcb91a8d3169f263294c9a90c575bf1938b9f489" || { echo "oreon: Source0 SHA256 mismatch for libpciaccess-0.16.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
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
