%global source0_hash b2f63f229274437a043c9454f18e82c46d8bcaefdf943305f4e9fcb7eec1a634

Name:           zmat
Version:        0.9.8
Release:        17%{?dist}
Summary:        An easy-to-use data compression library
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/fangq/%{name}
Source0:        https://github.com/fangq/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc-c++ zlib-devel

%description
ZMat is a portable C library to enable easy-to-use data compression
and decompression (such as zlib/gzip/lzma/lzip/lz4/lz4hc algorithms)
and base64 encoding/decoding in an application.
It is fast and compact, can process a large array within a fraction
of a second. Among the supported compression methods, lz4 is the
fastest for compression/decompression; lzma is the slowest but has
the highest compression ratio; zlib/gzip have the best balance
between speed and compression time.

%package devel
Summary:        Development files for zmat - an easy-to-use data compression library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zlib-devel

%description devel
The %{name}-devel package provides the headers files and tools you may need to
develop applications using zmat.

%package static
Summary:        Static library for zmat - an easy-to-use data compression library
Requires:       %{name}-devel

%description static
The %{name}-static package provides the static library you may need to
develop applications using zmat.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}
chmod a-x src/easylzma/pavlov/*
mv test examples

%build
%set_build_flags
mv fortran90/%{name}lib.f90 include/

pushd src
%make_build clean
%make_build lib CPPOPT="%{optflags} -fPIC"
mv ../lib/lib%{name}.a ../
%make_build clean
%make_build dll CPPOPT="%{optflags} -fPIC"
mv ../lib/lib%{name}.so ../lib/lib%{name}.so.%{version}
mv ../lib%{name}.a ../lib
popd

%install
install -m 755 -pd %{buildroot}/%{_includedir}/
install -m 644 -pt %{buildroot}/%{_includedir}/ include/%{name}lib.h
install -m 644 -pt %{buildroot}/%{_includedir}/ include/%{name}lib.f90

install -m 755 -pd %{buildroot}/%{_libdir}/
install -m 755 -pt %{buildroot}/%{_libdir}/ lib/lib%{name}.so.%{version}
install -m 644 -pt %{buildroot}/%{_libdir}/ lib/lib%{name}.a
pushd %{buildroot}/%{_libdir}
    ln -s lib%{name}.so.%{version} lib%{name}.so
popd

%files
%license LICENSE.txt
%doc README.rst
%doc AUTHORS.txt
%doc ChangeLog.txt
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.1

%files devel
%doc examples
%{_includedir}/%{name}lib.h
%{_includedir}/%{name}lib.f90
%{_libdir}/lib%{name}.so

%files static
%{_libdir}/lib%{name}.a

%changelog
%autochangelog
