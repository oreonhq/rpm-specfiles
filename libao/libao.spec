Name:           libao
Version:        1.2.0
Release:        31%{?dist}
Summary:        Cross Platform Audio Output Library
License:        GPL-2.0-or-later
URL:            http://xiph.org/ao/
Source0:        http://downloads.xiph.org/releases/ao/%{name}-%{version}.tar.gz
Patch1:         0001-ao_pulse.c-fix-latency-calculation.patch
# https://gitlab.xiph.org/xiph/libao/commit/d5221655dfd1a2156aa6be83b5aadea7c1e0f5bd.diff
# CVE 2017-11548
Patch2:         d5221655dfd1a2156aa6be83b5aadea7c1e0f5bd.diff
Patch3:         libao-nanosleep.patch
BuildRequires:  gcc
BuildRequires:  alsa-lib-devel
BuildRequires:  pkgconfig(libpulse)
BuildRequires: make

%description
Libao is a cross-platform audio library that allows programs to output audio
using a simple API on a wide variety of platforms.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
sed -i "s/-O20 -ffast-math//" configure


%build
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
%make_install INSTALL="install -p"
# remove unpackaged files from the buildroot
find $RPM_BUILD_ROOT -name '*.la' -exec rm -rf {} \;
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}*


%ldconfig_scriptlets


%files
%doc AUTHORS CHANGES COPYING README
%{_libdir}/libao.so.*
%{_libdir}/ao
%{_mandir}/man5/*

%files devel
%doc doc/*.html doc/*.c doc/*.css
%{_includedir}/ao
%{_libdir}/ckport
%{_libdir}/libao.so
%{_libdir}/pkgconfig/ao.pc
%{_datadir}/aclocal/ao.m4


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-31
- Prepare for Oreon 11 (RP1)
