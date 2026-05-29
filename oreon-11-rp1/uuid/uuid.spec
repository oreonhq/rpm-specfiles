%global source0_hash 11a615225baa5f8bb686824423f50e4427acd3f70d394765bdff32801f0fd5b0

%if 0%{?fedora} < 20 && 0%{?rhel} < 7
# Private libraries are not be exposed globally by RPM
%{?filter_provides_in: %filter_provides_in %{php_extdir}/.*\.so$}
%{?filter_setup}
%endif

Name:           uuid
Version:        1.6.2
Release:        68%{?dist}
Summary:        Universally Unique Identifier library
License:        MIT
URL:            http://www.ossp.org/pkg/lib/uuid/
Source0:        https://deb.debian.org/debian/pool/main/o/ossp-uuid/ossp-uuid_1.6.2.orig.tar.gz#/uuid-1.6.2.tar.gz
Patch0:         uuid-1.6.1-ossp.patch
Patch1:         uuid-1.6.1-mkdir.patch
Patch2:         uuid-1.6.2-php54.patch

# rhbz#829532
Patch3:         uuid-1.6.2-hwaddr.patch

# do not strip binaries
Patch4:         uuid-1.6.2-nostrip.patch
Patch5:         uuid-1.6.2-manfix.patch
Patch6:         uuid-aarch64.patch

# use ldflags for libs too
Patch7:	        uuid-1.6.2-ldflags.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libtool

Obsoletes:      %{name}-pgsql < 1.6.2-24

%description
OSSP uuid is a ISO-C:1999 application programming interface (API)
and corresponding command line interface (CLI) for the generation
of DCE 1.1, ISO/IEC 11578:1996 and RFC 4122 compliant Universally
Unique Identifier (UUID). It supports DCE 1.1 variant UUIDs of version
1 (time and node based), version 3 (name based, MD5), version 4
(random number based) and version 5 (name based, SHA-1). Additional
API bindings are provided for the languages ISO-C++:1998 and Perl:5 
Optional backward compatibility exists for the ISO-C DCE-1.1 and Perl
Data::UUID APIs.

%package devel
Summary:        Development support for Universally Unique Identifier library
Requires:       pkgconfig
Requires:       %{name} = %{version}-%{release}

%description devel
Development headers and libraries for OSSP uuid.

%package c++
Summary:        C++ support for Universally Unique Identifier library
Requires:       %{name} = %{version}-%{release}

%description c++
C++ libraries for OSSP uuid.

%package c++-devel
Summary:        C++ development support for Universally Unique Identifier library
Requires:       %{name}-c++ = %{version}-%{release}
Requires:       %{name}-devel = %{version}-%{release}

%description c++-devel
C++ development headers and libraries for OSSP uuid.

%package perl
Summary:        Perl support for Universally Unique Identifier library
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
Requires:       %{name} = %{version}-%{release}
Requires:       perl(Data::UUID)

%description perl
Perl OSSP uuid module.

%package dce
Summary:        DCE support for Universally Unique Identifier library
Requires:       %{name} = %{version}-%{release}

%description dce
DCE OSSP uuid library.

%package dce-devel
Summary:        DCE development support for Universally Unique Identifier library
Requires:       %{name}-dce = %{version}-%{release}
Requires:       %{name}-devel = %{version}-%{release}

%description dce-devel
DCE development headers and libraries for OSSP uuid.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1 -b .php54
%patch -P3 -p1 -b .hwaddr
%patch -P4 -p1 -b .nostrip
%patch -P5 -p1 -b .manfix
%patch -P6 -p1 -b .aarch64
%patch -P7 -p1 -b .ldflags

%build
# Build the library.
export LIB_NAME=libossp-uuid.la
export DCE_NAME=libossp-uuid_dce.la
export CXX_NAME=libossp-uuid++.la
export PHP_NAME=$(pwd)/php/modules/ossp-uuid.so
export PGSQL_NAME=$(pwd)/pgsql/libossp-uuid.so

%configure \
    --disable-static \
    --without-perl \
    --without-php \
    --with-dce \
    --with-cxx \
    --without-pgsql

make LIBTOOL=/usr/bin/libtool CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" LDFLAGS="%{build_ldflags}" %{?_smp_mflags}

# Build the Perl module.
pushd perl
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" COMPAT=0
%{__perl} -pi -e 's/^\tLD_RUN_PATH=[^\s]+\s*/\t/' Makefile
make %{?_smp_mflags}
popd

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la $RPM_BUILD_ROOT%{_libdir}/*.a
chmod 755 $RPM_BUILD_ROOT%{_libdir}/*.so.*.*.*

# Install the Perl modules.
pushd perl
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*
popd

%check
make check

pushd perl
LD_LIBRARY_PATH=../.libs make test
# Check that current Data::UUID is compatible with old compat layer
perl -MData::UUID -e 'print "Testing compatibility of Data::UUID version $Data::UUID::VERSION\n";'
LD_LIBRARY_PATH=../.libs make test TEST_FILES=uuid_compat.ts
popd

%ldconfig_scriptlets
%ldconfig_scriptlets c++
%ldconfig_scriptlets dce

%files
%doc AUTHORS ChangeLog HISTORY NEWS PORTING README SEEALSO THANKS TODO USERS
%{_bindir}/uuid
%{_libdir}/libossp-uuid.so.*
%{_mandir}/man1/*
%exclude %{_mandir}/man1/uuid-config.*

%files devel
%{_bindir}/uuid-config
%{_includedir}/uuid.h
%{_libdir}/libossp-uuid.so
%{_libdir}/pkgconfig/ossp-uuid.pc
%{_mandir}/man3/ossp-uuid.3*
%{_mandir}/man1/uuid-config.*

%files c++
%{_libdir}/libossp-uuid++.so.*

%files c++-devel
%{_includedir}/uuid++.hh
%{_libdir}/libossp-uuid++.so
%{_mandir}/man3/uuid++.3*

%files perl
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/OSSP*
%{_mandir}/man3/OSSP::uuid.3*

%files dce
%{_libdir}/libossp-uuid_dce.so.*

%files dce-devel
%{_includedir}/uuid_dce.h
%{_libdir}/libossp-uuid_dce.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.2-68
- Prepare for Oreon 11 (RP1)
