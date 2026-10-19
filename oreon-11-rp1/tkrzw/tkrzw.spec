%global source0_hash d3404dfac6898632b69780c0f0994c5f6ba962191a61c9b0f4b53ba8bb27731c
%global _lto_cflags %{nil}
%global _lib_min_ver 75
Name:		tkrzw
Version:	1.0.32
Release:        3%{?dist}
Summary:        A straightforward implementation of DBM
License:	Apache-2.0
URL:		https://dbmx.net/%{name}/
Source0:        https://dbmx.net/%{name}/pkg/%{name}-%{version}.tar.gz
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
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
rm -f %{buildroot}%{_libdir}/lib%{name}.a
install -d %{buildroot}%{_mandir}/man1
install -t %{buildroot}%{_mandir}/man1 -m 0644 -p tkrzw_*.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build check-light
%if 0%{?el8}
%ldconfig_scriptlets libs
%endif
%files -f %{oreon_filedir}/main.list
%files -n tkrzw-libs -f %{oreon_filedir}/tkrzw-libs.list
%files -n tkrzw-devel -f %{oreon_filedir}/tkrzw-devel.list
%files -n tkrzw-doc -f %{oreon_filedir}/tkrzw-doc.list

%changelog

%autochangelog
