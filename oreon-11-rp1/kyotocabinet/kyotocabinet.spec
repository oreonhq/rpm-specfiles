%global source0_hash 4c85d736668d82920bfdbdb92ac3d66b7db1108f09581a769dd9160a02def349
Summary:        A straightforward implementation of DBM
Name:           kyotocabinet
Version:        1.2.80
Release:        9%{?dist}
License:        GPL-3.0-only
URL:            https://dbmx.net/%{name}/
Source0:        https://dbmx.net/%{name}/pkg/%{name}-%{version}.tar.gz
Patch0:        kyotocabinet-1.2.76-cflags.patch
Patch1:        kyotocabinet-1.2.76-8-byte-atomics.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  lzo-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir kyotocabinet-1.2.80
%oreon_prep
%build

%configure --disable-opt --enable-lzo --enable-lzma
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/libkyotocabinet.a
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n kyotocabinet-libs -f %{oreon_filedir}/kyotocabinet-libs.list
%files -n kyotocabinet-devel -f %{oreon_filedir}/kyotocabinet-devel.list
%files -n kyotocabinet-apidocs -f %{oreon_filedir}/kyotocabinet-apidocs.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.80-9
- Import
