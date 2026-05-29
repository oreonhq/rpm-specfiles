%global source0_hash 4c85d736668d82920bfdbdb92ac3d66b7db1108f09581a769dd9160a02def349

Summary:        A straightforward implementation of DBM
Name:           kyotocabinet
Version:        1.2.80
Release:        9%{?dist}
License:        GPL-3.0-only
URL:            https://dbmx.net/%{name}/
Source:        https://dbmx.net/kyotocabinet/pkg/kyotocabinet-1.2.80.tar.gz
Patch0:         kyotocabinet-1.2.76-cflags.patch
Patch1:         kyotocabinet-1.2.76-8-byte-atomics.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires:  gcc-c++, zlib-devel, lzo-devel, xz-devel

%description
Kyoto Cabinet is a library of routines for managing a database. The
database is a simple data file containing records, each is a pair of
a key and a value. Every key and value is serial bytes with variable
length. Both binary data and character string can be used as a key
and a value. Each key must be unique within a database. And there is
neither concept of data tables nor data types. Records are organized
in hash table or B+ tree.

%package libs
Summary:        Libraries for applications using Kyoto Cabinet
Provides:       %{name}-lib = %{version}-%{release}
Provides:       %{name}-lib%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-lib < 1.2.76-3

%description libs
The kyotocabinet-libs package provides the essential shared libraries
for any Kyoto Cabinet client program or interface.

%package        devel
Summary:        Development files for Kyoto Cabinet
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}, pkgconfig

%description devel
The kyotocabinet-devel package contains libraries and header files for
developing applications that use Kyoto Cabinet.

%package apidocs
Summary:        API documentation for Kyoto Cabinet library
BuildArch:      noarch
Provides:       %{name}-api-doc = %{version}-%{release}
Obsoletes:      %{name}-api-doc < 1.2.76-3

%description apidocs
The kyotocabinet-apidocs package contains API documentation for developing
applications that use Kyoto Cabinet.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%configure --disable-opt --enable-lzo --enable-lzma
%make_build

%install
%make_install

# Don't install any static .a file
rm -f $RPM_BUILD_ROOT%{_libdir}/libkyotocabinet.a

# Clean up for later usage in documentation
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}

%check
make check

%ldconfig_scriptlets libs

%files
%doc doc/{command.html,common.css,icon16.png}
%{_bindir}/kccachetest
%{_bindir}/kcdirmgr
%{_bindir}/kcdirtest
%{_bindir}/kcforestmgr
%{_bindir}/kcforesttest
%{_bindir}/kcgrasstest
%{_bindir}/kchashmgr
%{_bindir}/kchashtest
%{_bindir}/kclangctest
%{_bindir}/kcpolymgr
%{_bindir}/kcpolytest
%{_bindir}/kcprototest
%{_bindir}/kcstashtest
%{_bindir}/kctreemgr
%{_bindir}/kctreetest
%{_bindir}/kcutilmgr
%{_bindir}/kcutiltest
%{_mandir}/man1/kccachetest.1*
%{_mandir}/man1/kcdirmgr.1*
%{_mandir}/man1/kcdirtest.1*
%{_mandir}/man1/kcforestmgr.1*
%{_mandir}/man1/kcforesttest.1*
%{_mandir}/man1/kcgrasstest.1*
%{_mandir}/man1/kchashmgr.1*
%{_mandir}/man1/kchashtest.1*
%{_mandir}/man1/kclangctest.1*
%{_mandir}/man1/kcpolymgr.1*
%{_mandir}/man1/kcpolytest.1*
%{_mandir}/man1/kcprototest.1*
%{_mandir}/man1/kcstashtest.1*
%{_mandir}/man1/kctreemgr.1*
%{_mandir}/man1/kctreetest.1*
%{_mandir}/man1/kcutilmgr.1*
%{_mandir}/man1/kcutiltest.1*

%files libs
%{!?_licensedir:%global license %%doc}
%license COPYING FOSSEXCEPTION LINKEXCEPTION
%doc ChangeLog
%{_libdir}/libkyotocabinet.so.*

%files devel
%{_includedir}/kccachedb.h
%{_includedir}/kccommon.h
%{_includedir}/kccompare.h
%{_includedir}/kccompress.h
%{_includedir}/kcdb.h
%{_includedir}/kcdbext.h
%{_includedir}/kcdirdb.h
%{_includedir}/kcfile.h
%{_includedir}/kchashdb.h
%{_includedir}/kclangc.h
%{_includedir}/kcmap.h
%{_includedir}/kcplantdb.h
%{_includedir}/kcpolydb.h
%{_includedir}/kcprotodb.h
%{_includedir}/kcregex.h
%{_includedir}/kcstashdb.h
%{_includedir}/kctextdb.h
%{_includedir}/kcthread.h
%{_includedir}/kcutil.h
%{_libdir}/libkyotocabinet.so
%{_libdir}/pkgconfig/kyotocabinet.pc

%files apidocs
%doc COPYING doc/api/* kyotocabinet.idl

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.80-9
- Import
