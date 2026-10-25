%global source0_hash b6a5f44b7eb69e3fa35dbf15524405b44837a481d43d81daddde3ff21fcbb8e9
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: openssl
Version: 3.6.0
Release: 1%{?dist}
Summary: OpenSSL TLS library
License: Apache-2.0
URL: https://www.openssl.org/
Source0: https://github.com/openssl/openssl/releases/download/openssl-%{version}/openssl-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: perl
BuildRequires: zlib-ng-compat-devel
BuildRequires: python3
BuildRequires: patchelf
%endif

%description
OpenSSL is a TLS and crypto library.

%package devel
Summary: OpenSSL TLS library
Requires: openssl%{?_isa} = %{version}-%{release}

%description devel
OpenSSL is a TLS and crypto library.

%prep
%oreon_sha256
%autosetup -p1

%build
./Configure \
  --prefix=%{_prefix} \
  --libdir=%{_lib} \
  --openssldir=%{_sysconfdir}/pki/tls \
  shared \
  zlib \
  no-docs \
  -Wl,-z,relro,-z,now
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install_sw install_ssldirs
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
%license LICENSE.txt

%files devel -f %{_builddir}/%{name}-devel.files
