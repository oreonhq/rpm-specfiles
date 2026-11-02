%global source0_hash 8dadd7d2536a314f982ad05a651b713f426bf7d02cc2c76cffb9796f2218e6c5
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: curl
Version: 8.23.0
Release: 2%{?dist}
Summary: HTTP client and library
License: curl
URL: https://curl.se/
Source0: https://curl.se/download/curl-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: openssl-devel
BuildRequires: libnghttp2-devel
BuildRequires: zlib-devel
BuildRequires: python3
BuildRequires: libzstd-devel
BuildRequires: pkgconfig(libpsl)
BuildRequires: pkgconfig(libssh)
BuildRequires: pkgconfig(libbrotlidec)
BuildRequires: pkgconfig(libnghttp3)
BuildRequires: pkgconfig(libngtcp2)
BuildRequires: pkgconfig(libngtcp2_crypto_ossl)
BuildRequires: pkgconfig(libidn2)
BuildRequires: patchelf

Obsoletes: libcurl < 9
Provides: libcurl = %{version}-%{release}

%description
curl is an HTTP client and libcurl.

%package devel
Summary: HTTP client and library
Requires: curl%{?_isa} = %{version}-%{release}
Obsoletes: libcurl-devel < 9
Provides: libcurl-devel = %{version}-%{release}
Provides: pkgconfig(libcurl) = %{version}

%description devel
curl is an HTTP client and libcurl.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure \
  --disable-static \
  --with-openssl \
  --with-nghttp2 \
  --with-zlib \
  --with-zstd \
  --disable-ldap \
  --disable-ldaps \
  --disable-manual \
  --with-libpsl \
  --without-libssh2 \
  --with-libssh \
  --with-brotli \
  --with-libidn2 \
  --with-ngtcp2 \
  --with-nghttp3
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel
python3 - %{_builddir}/%{name}.files %{_builddir}/%{name}-devel.files << 'PY'
import sys
from pathlib import Path
main, devel = Path(sys.argv[1]), Path(sys.argv[2])
m = main.read_text().splitlines()
d = devel.read_text().splitlines()
keep, move = [], []
for line in d:
    path = line.split()[-1] if line.startswith("%") else line
    if path.endswith(".so") and path.count("/") > 3:
        move.append(line)
    else:
        keep.append(line)
text = "\n".join(m + move)
main.write_text(text + ("\n" if text else ""))
text = "\n".join(keep)
devel.write_text(text + ("\n" if text else ""))
PY

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
