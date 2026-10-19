%global source0_hash 4f112fea59e0c65f0fffe30a4957f8d66cf41528c21dd9903e6d7550022c794e
%global _bundled_pcre2_version 10.44
%global libversion 111
%bcond check 0
%bcond_without samples
%ifarch aarch64 %{arm} %{ix86} x86_64 ppc64le
%bcond_without mongodb
%endif
Name:           poco
Version:        1.15.3
Release:        1%{?dist}
Summary:        C++ class libraries for network-centric applications
License:        BSL-1.0
URL:            https://pocoproject.org
Source0:        https://github.com/pocoproject/poco/archive/poco-%{version}-release/poco-%{version}.tar.gz
Provides:       bundled(pcre2) = %{_bundled_pcre2_version}
# oreon:deps
BuildRequires:  apr-devel
BuildRequires:  apr-util-devel
BuildRequires:  cmake
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  httpd-devel
BuildRequires:  libatomic
BuildRequires:  libiodbc-devel
BuildRequires:  libpng-devel
BuildRequires:  libpq-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  sqlite-devel
BuildRequires:  utf8proc-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The POCO C++ Libraries (POCO stands for POrtable COmponents)
are open source C++ class libraries that simplify and accelerate the
development of network-centric, portable applications in C++. The
POCO C++ Libraries are built strictly on standard ANSI/ISO C++,
including the standard library.

%package        foundation
Summary:        The Foundation POCO component
%description    foundation
This package contains the Foundation component of POCO library.

%package        encodings
Summary:        The Encodings POCO component
%description    encodings
This package contains the Encodings component of POCO library.

%package        xml
Summary:        The XML POCO component
%description    xml
This package contains the XML component of POCO library.

%package        json
Summary:        The JSON POCO component
%description    json
This package contains the JSON component of POCO library.

%package        util
Summary:        The Util POCO component
%description    util
This package contains the Util component of POCO library.

%package        net
Summary:        The Net POCO component
%description    net
This package contains the Net component of POCO library.

%if %{with mongodb}
%package        mongodb
Summary:        The MongoDB POCO component
%description    mongodb
This package contains the MongoDB component of POCO library.
%endif

%package        redis
Summary:        The Redis POCO component
%description    redis
This package contains the Redis component of POCO library.

%package        prometheus
Summary:        The Prometheus POCO component
%description    prometheus
This package contains the Prometheus component of POCO library.

%package        pdf
Summary:        The PDF POCO component
%description    pdf
This package contains the PDF component of POCO library.

%package        jwt
Summary:        The JWT POCO component
%description    jwt
This package contains the JWT component of POCO library.

%package        netssl
Summary:        The NetSSL POCO component
%description    netssl
This package contains the NetSSL component of POCO library.

%package        crypto
Summary:        The Crypto POCO component
%description    crypto
This package contains the Crypto component of POCO library.

%package        data
Summary:        The Data POCO component
%description    data
This package contains the Data component of POCO library.

%package        odbc
Summary:        The Data/ODBC POCO component
%description    odbc
This package contains the Data/ODBC component of POCO library.

%package        sqlite
Summary:        The Data/SQLite POCO component
%description    sqlite
This package contains the Data/SQLite component of POCO library.

%package        mysql
Summary:        The Data/MySQL POCO component
%description    mysql
This package contains the Data/MySQL component of POCO library.

%package        postgresql
Summary:        The Data/PostgreSQL POCO component
%description    postgresql
This package contains the Data/PostgreSQL component of POCO library.

%package        zip
Summary:        The Zip POCO component
%description    zip
This package contains the Zip component of POCO library.

%package        cppparser
Summary:        The CppParser POCO component
%description    cppparser
This package contains the CppParser component of POCO library.

%package        activerecord
Summary:        The ActiveRecord POCO component
%description    activerecord
This package contains the ActiveRecord component of POCO library.

%package        devel
Summary:        Development files for %{name}
Requires:       poco-foundation%{?_isa} = %{version}-%{release}
Requires:       poco-encodings%{?_isa} = %{version}-%{release}
Requires:       poco-xml%{?_isa} = %{version}-%{release}
Requires:       poco-json%{?_isa} = %{version}-%{release}
Requires:       poco-util%{?_isa} = %{version}-%{release}
Requires:       poco-net%{?_isa} = %{version}-%{release}
%if %{with mongodb}
Requires:       poco-mongodb%{?_isa} = %{version}-%{release}
%endif
Requires:       poco-redis%{?_isa} = %{version}-%{release}
Requires:       poco-prometheus%{?_isa} = %{version}-%{release}
Requires:       poco-pdf%{?_isa} = %{version}-%{release}
Requires:       poco-jwt%{?_isa} = %{version}-%{release}
Requires:       poco-netssl%{?_isa} = %{version}-%{release}
Requires:       poco-crypto%{?_isa} = %{version}-%{release}
Requires:       poco-data%{?_isa} = %{version}-%{release}
Requires:       poco-odbc%{?_isa} = %{version}-%{release}
Requires:       poco-sqlite%{?_isa} = %{version}-%{release}
Requires:       poco-mysql%{?_isa} = %{version}-%{release}
Requires:       poco-postgresql%{?_isa} = %{version}-%{release}
Requires:       poco-zip%{?_isa} = %{version}-%{release}
Requires:       poco-cppparser%{?_isa} = %{version}-%{release}
Requires:       poco-activerecord%{?_isa} = %{version}-%{release}
Requires:       zlib-devel
Requires:       pcre2-devel
Requires:       expat-devel
Requires:       openssl-devel
Requires:       utf8proc-devel
%description    devel
This package contains development files for %{name}.

%package        doc
Summary:        Documentation for %{name}
%description    doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{name}-%{version}-release

rm -v Foundation/src/MSG00001.bin
rm -v Foundation/include/Poco/zconf.h
rm -v Foundation/include/Poco/zlib.h
rm -v Foundation/src/adler32.c
rm -v Foundation/src/compress.c
rm -v Foundation/src/crc32.c
rm -v Foundation/src/crc32.h
rm -v Foundation/src/deflate.c
rm -v Foundation/src/deflate.h
rm -v Foundation/src/gzguts.h
rm -v Foundation/src/infback.c
rm -v Foundation/src/inffast.c
rm -v Foundation/src/inffast.h
rm -v Foundation/src/inffixed.h
rm -v Foundation/src/inflate.c
rm -v Foundation/src/inflate.h
rm -v Foundation/src/inftrees.c
rm -v Foundation/src/inftrees.h
rm -v Foundation/src/trees.c
rm -v Foundation/src/trees.h
rm -v Foundation/src/zconf.h
rm -v Foundation/src/zlib.h
rm -v Foundation/src/zutil.c
rm -v Foundation/src/zutil.h

rm -v Foundation/src/pcre2_auto_possess.c
rm -v Foundation/src/pcre2_chartables.c
rm -v Foundation/src/pcre2_compile.c
rm -v Foundation/src/pcre2_config.c
rm -v Foundation/src/pcre2_context.c
rm -v Foundation/src/pcre2_convert.c
rm -v Foundation/src/pcre2_dfa_match.c
rm -v Foundation/src/pcre2_error.c
rm -v Foundation/src/pcre2_extuni.c
rm -v Foundation/src/pcre2_find_bracket.c
rm -v Foundation/src/pcre2_jit_compile.c
rm -v Foundation/src/pcre2_maketables.c
rm -v Foundation/src/pcre2_match.c
rm -v Foundation/src/pcre2_match_data.c
rm -v Foundation/src/pcre2_newline.c
rm -v Foundation/src/pcre2_ord2utf.c
rm -v Foundation/src/pcre2_pattern_info.c
rm -v Foundation/src/pcre2_script_run.c
rm -v Foundation/src/pcre2_serialize.c
rm -v Foundation/src/pcre2_string_utils.c
rm -v Foundation/src/pcre2_study.c
rm -v Foundation/src/pcre2_substitute.c
rm -v Foundation/src/pcre2_substring.c
# Unicode.cpp requires functions from these two files. The can't be taken from the library
# rm -v Foundation/src/pcre2_tables.c
# rm -v Foundation/src/pcre2_ucd.c
rm -v Foundation/src/pcre2_valid_utf.c
rm -v Foundation/src/pcre2_xclass.c

rm -v Data/SQLite/src/sqlite3.h
rm -v Data/SQLite/src/sqlite3.c
rm -v XML/src/ascii.h
rm -v XML/src/asciitab.h
rm -v XML/src/expat_config.h
rm -v XML/src/iasciitab.h
rm -v XML/src/internal.h
rm -v XML/src/latin1tab.h
rm -v XML/src/nametab.h
rm -v XML/src/utf8tab.h
rm -v XML/src/xmlparse.cpp
rm -v XML/src/xmlrole.c
rm -v XML/src/xmlrole.h
rm -v XML/src/xmltok.c
rm -v XML/src/xmltok.h
rm -v XML/src/xmltok_impl.c
rm -v XML/src/xmltok_impl.h
rm -v XML/src/xmltok_ns.c

%build

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DPOCO_UNBUNDLED=ON \
%if %{with check}
    -DENABLE_TESTS=ON \
%endif
%if %{without mongodb}
    -DENABLE_MONGODB=OFF \
%endif
    -DENABLE_PDF=ON \
    -DENABLE_CPPPARSER=ON \
    -DENABLE_ENCODINGS_COMPILER=ON \
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with check}
%ifarch s390x
%ctest -E "Redis|NetSSL|DataMySQL|DataPostgreSQL|DataODBC|Data"
%else
%ctest -E "MongoDB|Redis|NetSSL|DataMySQL|DataPostgreSQL|DataODBC|Data"
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n poco-foundation -f %{oreon_filedir}/poco-foundation.list
%files -n poco-encodings -f %{oreon_filedir}/poco-encodings.list
%files -n poco-xml -f %{oreon_filedir}/poco-xml.list
%files -n poco-json -f %{oreon_filedir}/poco-json.list
%files -n poco-util -f %{oreon_filedir}/poco-util.list
%files -n poco-net -f %{oreon_filedir}/poco-net.list
%files -n poco-redis -f %{oreon_filedir}/poco-redis.list
%files -n poco-prometheus -f %{oreon_filedir}/poco-prometheus.list
%files -n poco-pdf -f %{oreon_filedir}/poco-pdf.list
%files -n poco-jwt -f %{oreon_filedir}/poco-jwt.list
%files -n poco-netssl -f %{oreon_filedir}/poco-netssl.list
%files -n poco-crypto -f %{oreon_filedir}/poco-crypto.list
%files -n poco-data -f %{oreon_filedir}/poco-data.list
%files -n poco-odbc -f %{oreon_filedir}/poco-odbc.list
%files -n poco-sqlite -f %{oreon_filedir}/poco-sqlite.list
%files -n poco-mysql -f %{oreon_filedir}/poco-mysql.list
%files -n poco-postgresql -f %{oreon_filedir}/poco-postgresql.list
%files -n poco-zip -f %{oreon_filedir}/poco-zip.list
%files -n poco-cppparser -f %{oreon_filedir}/poco-cppparser.list
%files -n poco-activerecord -f %{oreon_filedir}/poco-activerecord.list
%files -n poco-devel -f %{oreon_filedir}/poco-devel.list
%files -n poco-doc -f %{oreon_filedir}/poco-doc.list

%changelog

%autochangelog
