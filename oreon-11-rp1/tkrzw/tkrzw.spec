%global source0_hash d3404dfac6898632b69780c0f0994c5f6ba962191a61c9b0f4b53ba8bb27731c

%global _lto_cflags %{nil}
%global _lib_min_ver 75

Name:		tkrzw
Version:	1.0.32
Release:	3%{?dist}
Summary:	A straightforward implementation of DBM
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0
URL:		https://dbmx.net/%{name}/
Source0:	https://dbmx.net/%{name}/pkg/%{name}-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	help2man
# zlib-devel
BuildRequires:	pkgconfig(zlib)
# libzstd-devel
BuildRequires:	pkgconfig(libzstd)
# lz4-devel
BuildRequires:	pkgconfig(liblz4)
# xz-devel
BuildRequires:	pkgconfig(liblzma)
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description
Tkrzw is a C++ library implementing DBM with various algorithms. It features
high degrees of performance, concurrency and durability.

%package	libs
Summary:	Libraries for applications using Tkrzw

%description	libs
This package provides the essential shared libraries
for any Tkrzw client program or interface.

%package	devel
Summary:	Development files for Tkrzw
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description	devel
This package contains libraries and header files for
developing applications that use Tkrzw.

%package	doc
Summary:	Tkrzw API documentation
BuildArch:	noarch

%description	doc
This package contains API documentation for developing
applications that use Tkrzw.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# https://github.com/estraier/tkrzw/issues/41
sed -i 's/MYLIBREV=66/MYLIBREV=69/g' configure.in

%build
autoreconf -vif
%configure  --enable-zlib --enable-lz4 --enable-lzma --enable-zstd
%make_build apidoc all
for bin in \
  tkrzw_build_util tkrzw_str_perf tkrzw_file_perf tkrzw_dbm_perf tkrzw_dbm_util
do
  LD_LIBRARY_PATH=$PWD help2man --no-info --no-discard-stderr \
    --version-string='%{version}' --output="${bin}.1" \
    "./${bin}"
done

%install
%make_install
# Remove static .a file
rm -f %{buildroot}%{_libdir}/lib%{name}.a
# mans
install -d %{buildroot}%{_mandir}/man1
install -t %{buildroot}%{_mandir}/man1 -m 0644 -p tkrzw_*.1

%check
%make_build check-light

%if 0%{?el8}
%ldconfig_scriptlets libs
%endif

%files
%{_bindir}/%{name}_*
%{_mandir}/man1/%{name}_*.1*

%files	libs
%license COPYING
%doc CONTRIBUTING.md
%{_libdir}/lib%{name}.so.{1,1.%{_lib_min_ver}.0}

%files	devel
%doc example
%{_includedir}/%{name}_*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files	doc
%license COPYING
%doc doc api-doc

%changelog
%autochangelog
