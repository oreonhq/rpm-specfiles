%global source0_hash 5a2f477e6268630f6e2829c7bb3e442017549798a4122635817934eaa0c6ac10
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: systemd
Version: 257.10
Release: 1%{?dist}
Summary: System and service manager
License: LGPL-2.1-or-later AND GPL-2.0-or-later
URL: https://systemd.io/
Source0: https://github.com/systemd/systemd/archive/refs/tags/v%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: gperf
BuildRequires: python3
BuildRequires: libcap-devel
BuildRequires: libxcrypt-devel
BuildRequires: libmount-devel
BuildRequires: libblkid-devel
BuildRequires: libselinux-devel
BuildRequires: libacl-devel
BuildRequires: openssl-devel
BuildRequires: zlib-ng-compat-devel
BuildRequires: bzip2-devel
BuildRequires: xz-devel
BuildRequires: lz4-devel
BuildRequires: libzstd-devel
BuildRequires: libarchive-devel
BuildRequires: dbus-devel
BuildRequires: glib2-devel
BuildRequires: pcre2-devel
BuildRequires: kmod-devel
BuildRequires: patchelf
%endif

%description
systemd is the system and service manager.

%package devel
Summary: System and service manager
Requires: systemd%{?_isa} = %{version}-%{release}

%description devel
systemd is the system and service manager.

%prep
%oreon_sha256
%autosetup -n systemd-%{version} -p1

%build
%oreon_meson \
  -Dauto_features=disabled \
  -Dmode=release \
  -Dtests=false \
  -Dfuzz-tests=false \
  -Dinstall-tests=false \
  -Dtranslations=false \
  -Defi=false \
  -Dtpm=false \
  -Dstatic-libsystemd=false \
  -Dstatic-libudev=false \
  -Dbpf-framework=disabled \
  -Dapparmor=disabled \
  -Daudit=disabled \
  -Dlibcryptsetup=disabled \
  -Dlibcryptsetup-plugins=disabled \
  -Dmicrohttpd=disabled \
  -Dlibcurl=disabled \
  -Dlibidn2=disabled \
  -Dlibidn=disabled \
  -Dlibiptc=disabled \
  -Dqrencode=disabled \
  -Dgcrypt=disabled \
  -Dgnutls=disabled \
  -Dp11kit=disabled \
  -Dlibfido2=disabled \
  -Dtpm2=disabled \
  -Delfutils=disabled \
  -Dxkbcommon=disabled \
  -Dbootloader=disabled \
  -Dukify=disabled \
  -Dhomed=disabled \
  -Dremote=disabled \
  -Dimportd=disabled \
  -Dvmspawn=disabled \
  -Drepart=disabled \
  -Dsysupdate=disabled \
  -Dpolkit=disabled \
  -Dseccomp=disabled \
  -Dfdisk=disabled \
  -Dxenctrl=disabled \
  -Dpwquality=disabled \
  -Dpasswdqc=disabled \
  -Dpam=disabled \
  -Dsmack=false \
  -Dima=false \
  -Dipe=false \
  -Didn=false \
  -Dsysupdated=disabled \
  -Dcryptolib=openssl \
  -Ddns-over-tls=openssl \
  -Dnss-mymachines=disabled \
  -Dnss-resolve=disabled \
  -Dresolve=false \
  -Dselinux=enabled \
  -Dacl=enabled \
  -Dopenssl=enabled \
  -Dzlib=enabled \
  -Dbzip2=enabled \
  -Dxz=enabled \
  -Dlz4=enabled \
  -Dzstd=enabled \
  -Dlibarchive=enabled \
  -Ddbus=enabled \
  -Dglib=enabled \
  -Dpcre2=enabled \
  -Dblkid=enabled \
  -Dkmod=enabled
%oreon_meson_build

%install
%oreon_meson_install
rm -f %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
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
%license LICENSE.GPL2 LICENSE.LGPL2.1

%files devel -f %{_builddir}/%{name}-devel.files
