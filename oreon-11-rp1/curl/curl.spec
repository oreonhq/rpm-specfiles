%global source0_hash 40c8cddbcb6cc6251c03dea423a472a6cea4037be654ba5cf5dec6eb2d22ff1d
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: curl
Version: 8.16.0
Release: 1%{?dist}
Summary: HTTP client and library
License: curl
URL: https://curl.se/
Source0: https://curl.se/download/curl-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: openssl-devel
BuildRequires: nghttp2-devel
BuildRequires: zlib-ng-compat-devel
BuildRequires: python3
BuildRequires: libzstd-devel
BuildRequires: patchelf
%endif

%description
curl is an HTTP client and libcurl.

%package devel
Summary: HTTP client and library
Requires: curl%{?_isa} = %{version}-%{release}

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
  --without-libpsl \
  --without-libssh2 \
  --without-libssh \
  --without-brotli \
  --without-libidn2 \
  --without-nghttp3
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
