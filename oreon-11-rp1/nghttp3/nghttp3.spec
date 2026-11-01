%global source0_hash aad782c23d3f01bd4bb52c8bac7a553b631ef8115fd1612703df6183449fef19
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: nghttp3
Version: 1.18.0
Release: 2%{?dist}
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

%package devel
Summary: Development files for nghttp3
Requires: nghttp3%{?_isa} = %{version}-%{release}
Provides: libnghttp3-devel = %{version}-%{release}
Provides: pkgconfig(libnghttp3) = %{version}

%description devel
Headers and libraries for developing against nghttp3.

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
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
