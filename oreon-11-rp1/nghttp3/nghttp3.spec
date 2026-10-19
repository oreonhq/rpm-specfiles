%global source1_hash 152a1d3c6a84968e2361698b5e72724220a771b3335017b6450eb658592e13d3
%global source0_hash aad782c23d3f01bd4bb52c8bac7a553b631ef8115fd1612703df6183449fef19
%global abi_ver 9
Name:           nghttp3
Version:        1.18.0
Release:        1%{?dist}
Summary:        HTTP/3 library written in C
License:        MIT
URL:            https://github.com/ngtcp2/nghttp3
Source0:        https://github.com/ngtcp2/nghttp3/releases/download/v%{version}/nghttp3-%{version}.tar.xz
Source1:        https://github.com/ngtcp2/nghttp3/releases/download/v%{version}/nghttp3-%{version}.tar.xz.asc
Source2:        tatsuhiro-t.pgp
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  gpgverify
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description

%package -n     libnghttp3
Summary:        HTTP/3 library written in C
%description -n libnghttp3

%package -n     libnghttp3-devel
Summary:        Development files for libnghttp3
Requires:       libnghttp3%{?_isa} = %{version}-%{release}
%description -n libnghttp3-devel

The libnghttp3-devel package contains libraries and header files for
developing applications that use libnghttp3.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

autoreconf -fiv
%configure --disable-static
%{__make} %{?_smp_mflags}
%install
%{__make} install DESTDIR=%{buildroot} INSTALL='install -p'
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_docdir}/nghttp3/README.rst
%oreon_autofiles libnghttp3 usr/*/lib*.so.*
%oreon_autofiles libnghttp3-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{__make} check
%files -f %{oreon_filedir}/main.list
%files -n libnghttp3 -f %{oreon_filedir}/libnghttp3.list
%files -n libnghttp3-devel -f %{oreon_filedir}/libnghttp3-devel.list

%changelog

%autochangelog
