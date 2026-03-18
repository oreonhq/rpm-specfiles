Summary:        Tar file manipulation API
Name:           libtar
Version:        1.2.20
Release:        35%{?dist}
License:        MIT
URL:            http://repo.or.cz/libtar.git
Source:         http://repo.or.cz/libtar.git/snapshot/refs/tags/v1.2.20.tar.gz#/libtar-v1.2.20.tar.gz
Patch1:         libtar-1.2.11-missing-protos.patch
Patch4:         libtar-1.2.11-mem-deref.patch
Patch5:         libtar-1.2.20-fix-resource-leaks.patch
Patch6:         libtar-1.2.11-bz729009.patch
Patch7:         libtar-1.2.20-no-static-buffer.patch

# fix programming mistakes detected by static analysis
Patch8:         libtar-1.2.20-static-analysis.patch

# fix out-of-bounds read in gnu_long{name,link} (CVE-2021-33643 CVE-2021-33644)
Patch9:         libtar-1.2.20-CVE-2021-33643-CVE-2021-33644.patch

# fix memory leaks through gnu_long{name,link} (CVE-2021-33645 CVE-2021-33646)
Patch10:        libtar-1.2.20-CVE-2021-33645-CVE-2021-33646.patch
Patch11: libtar-configure-c99.patch

BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  zlib-devel

%description
libtar is a C library for manipulating tar archives. It supports both
the strict POSIX tar format and many of the commonly-used GNU
extensions.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n libtar-v%{version} -p1

# set correct version for .so build
%global ltversion %(echo %{version} | tr '.' ':')
sed -i 's/-rpath $(libdir)/-rpath $(libdir) -version-number %{ltversion}/' \
  lib/Makefile.in

autoreconf -iv


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
# Without this we get no debuginfo and stripping
chmod +x $RPM_BUILD_ROOT%{_libdir}/libtar.so.%{version}
rm $RPM_BUILD_ROOT%{_libdir}/*.la


%ldconfig_scriptlets


%files
%doc COPYRIGHT TODO README ChangeLog*
%{_bindir}/%{name}
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/libtar.h
%{_includedir}/libtar_listhash.h
%{_libdir}/lib*.so
%{_mandir}/man3/*.3*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.20-35
- Prepare for Oreon 11 (RP1)
