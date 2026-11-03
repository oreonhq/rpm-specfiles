%global source0_hash aad782c23d3f01bd4bb52c8bac7a553b631ef8115fd1612703df6183449fef19
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: nghttp3
Version: 1.18.0
Release: 4%{?dist}
Summary: HTTP/3 library
License: MIT
URL: https://github.com/ngtcp2/nghttp3
Source0: https://github.com/ngtcp2/nghttp3/releases/download/v%{version}/nghttp3-%{version}.tar.xz
Source1: nghttp3-%{version}.tar.xz.asc
Source2: nghttp3-key.asc

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: patchelf
BuildRequires: pkgconf

%description
nghttp3 implements HTTP/3 mapping over QUIC and QPACK (RFC 9204).

%package -n libnghttp3
Summary: nghttp3 library
Obsoletes: nghttp3 < 1.18.0-4

%description -n libnghttp3
Shared nghttp3 library.

%package -n libnghttp3-devel
Summary: Development files for libnghttp3
Requires: libnghttp3%{?_isa} = %{version}-%{release}
Obsoletes: nghttp3-devel < 1.18.0-4

%description -n libnghttp3-devel
Headers and development library for libnghttp3.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n nghttp3-%{version} -p1

%build
%oreon_configure --disable-static --enable-lib-only
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_docdir}
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%ldconfig_scriptlets -n libnghttp3

%files -n libnghttp3
%license COPYING
%{_libdir}/libnghttp3.so.9
%{_libdir}/libnghttp3.so.9.*

%files -n libnghttp3-devel
%{_includedir}/nghttp3/
%{_libdir}/libnghttp3.so
%{_libdir}/pkgconfig/libnghttp3.pc
