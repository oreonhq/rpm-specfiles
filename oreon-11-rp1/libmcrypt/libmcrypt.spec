%global source0_hash e4eb6c074bbab168ac47b947c195ff8cef9d51a211cdd18ca9c9ef34d27a373e

Name:		libmcrypt
Version:	2.5.8
Release:	43%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
Summary:	Encryption algorithms library
URL:		http://mcrypt.sourceforge.net/
Source0:	http://downloads.sourceforge.net/mcrypt/libmcrypt-%{version}.tar.gz
Patch0:		libmcrypt-2.5.8-nolibltdl.patch
# Upstream:
# http://sourceforge.net/tracker/index.php?func=detail&aid=1872801&group_id=87941&atid=584895
Patch1:		libmcrypt-2.5.8-uninitialized.patch
# Upstream:
# http://sourceforge.net/tracker/index.php?func=detail&aid=1872799&group_id=87941&atid=584895
Patch2:		libmcrypt-2.5.8-prototypes.patch
Patch3: libmcrypt-configure-c99.patch
Patch4: libmcrypt-c99.patch
Patch5: libmcrypt-configure-c99-2.patch
BuildRequires:	libtool-ltdl-devel
BuildRequires:	gcc-c++
BuildRequires: make

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

# Multilib fix
sed -i 's|-L%{_libdir}||g' $RPM_BUILD_ROOT%{_bindir}/libmcrypt-config
touch -r NEWS $RPM_BUILD_ROOT%{_bindir}/libmcrypt-config

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING.LIB ChangeLog KNOWN-BUGS README NEWS THANKS TODO
%{_libdir}/*.so.*
%{_mandir}/man3/*

%files devel
%doc doc/README.key doc/README.xtea doc/example.c
%{_bindir}/libmcrypt-config
%{_includedir}/mutils/
%{_includedir}/mcrypt.h
%{_libdir}/*.so
%{_datadir}/aclocal/libmcrypt.m4

%changelog
%autochangelog
