%global source0_hash e4eb6c074bbab168ac47b947c195ff8cef9d51a211cdd18ca9c9ef34d27a373e
Name:		libmcrypt
Version:	2.5.8
Release:        43%{?dist}
License:	LicenseRef-Callaway-LGPLv2+
Summary:        Encryption algorithms library
URL:		http://mcrypt.sourceforge.net/
Source0:        http://downloads.sourceforge.net/mcrypt/libmcrypt-%{version}.tar.gz
Patch0:		libmcrypt-2.5.8-nolibltdl.patch
Patch1:		libmcrypt-2.5.8-uninitialized.patch
Patch2:		libmcrypt-2.5.8-prototypes.patch
Patch3: libmcrypt-configure-c99.patch
Patch4: libmcrypt-c99.patch
Patch5: libmcrypt-configure-c99-2.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
# /oreon:deps
%description
Libmcrypt is a thread-safe library providing a uniform interface
to access several block and stream encryption algorithms.

%package devel
Summary:	Development libraries and headers for libmcrypt
Requires:	%{name} = %{version}-%{release}
%description devel
Development libraries and headers for use in building applications that
use libmcrypt.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1 -b .uninitialized
%patch -P2 -p1 -b .prototypes
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build

%configure
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -type f -name '*.la' -exec rm -f {} \;
sed -i 's|-L%{_libdir}||g' $RPM_BUILD_ROOT%{_bindir}/libmcrypt-config
touch -r NEWS $RPM_BUILD_ROOT%{_bindir}/libmcrypt-config
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmcrypt-devel -f %{oreon_filedir}/libmcrypt-devel.list

%changelog

%autochangelog
