%global source0_hash f9a3f1e21e4dd78717bad0888638954467a55d73cab44a2c7a75c5bed47ef814
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: systemd
Version: 259.10
Release: 2%{?dist}
Provides: systemd-libs = %{version}-%{release}
Provides: systemd-libs%{_isa} = %{version}-%{release}
Obsoletes: systemd-libs < 260
Summary: System and service manager
License: LGPL-2.1-or-later AND GPL-2.0-or-later
URL: https://systemd.io/
Source0: https://github.com/systemd/systemd/archive/refs/tags/v%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: patchelf
BuildRequires: gperf
BuildRequires: python3
BuildRequires: libcap-devel
BuildRequires: libxcrypt-devel
BuildRequires: libmount-devel
BuildRequires: libblkid-devel
BuildRequires: libselinux-devel
BuildRequires: libacl-devel
BuildRequires: openssl-devel
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: xz-devel
BuildRequires: lz4-devel
BuildRequires: libzstd-devel
BuildRequires: libarchive-devel
BuildRequires: pcre2-devel
BuildRequires: libseccomp-devel
BuildRequires: audit-libs-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: libcurl-devel
BuildRequires: libidn2-devel
BuildRequires: libgcrypt-devel
BuildRequires: gnutls-devel
BuildRequires: p11-kit-devel
BuildRequires: elfutils-devel
BuildRequires: python3-jinja2
BuildRequires: libfdisk-devel
BuildRequires: gettext
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: dbus-devel
BuildRequires: glib2-devel
BuildRequires: cryptsetup-devel
BuildRequires: pam-devel
BuildRequires: libpwquality-devel
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
sed -i 's/EDEADLOCK|EWOULDBLOCK|ENOTSUP/EDEADLOCK|EWOULDBLOCK|ENOTSUP|EFSBADCRC|EFSCORRUPTED/' src/basic/errno-to-name.awk
sed -i "s#command : \[ bpftool, 'btf', 'dump', 'file', '/sys/kernel/btf/vmlinux', 'format', 'c' \],#command : [ 'sh', '-c', '\"\$1\" btf dump file /sys/kernel/btf/vmlinux format c | sed \"/bpf_stream_vprintk/d\"', 'gen-vmlinux', bpftool ],#" meson.build

%build
%global sd_cyc %[(%{with bootstrap} || 0%{?bootstrap}) ? "disabled" : "enabled"]
%oreon_meson \
  -Dmode=release \
  -Dlog-message-verification=disabled \
  -Dtests=false \
  -Dfuzz-tests=false \
  -Dinstall-tests=false \
  -Dtranslations=true \
  -Defi=true \
  -Dtpm=false \
  -Dstatic-libsystemd=false \
  -Dstatic-libudev=false \
  -Dbpf-framework=disabled \
  -Dapparmor=disabled \
  -Daudit=enabled \
  -Dlibcryptsetup=%{sd_cyc} \
  -Dlibcryptsetup-plugins=%{sd_cyc} \
  -Dmicrohttpd=enabled \
  -Dlibcurl=enabled \
  -Dlibidn2=enabled \
  -Dlibiptc=disabled \
  -Dqrencode=disabled \
  -Dgcrypt=enabled \
  -Dgnutls=enabled \
  -Dp11kit=enabled \
  -Dlibfido2=disabled \
  -Dtpm2=disabled \
  -Delfutils=enabled \
  -Dxkbcommon=disabled \
  -Dbootloader=disabled \
  -Dukify=disabled \
  -Dhomed=%{sd_cyc} \
  -Dremote=enabled \
  -Dimportd=enabled \
  -Dvmspawn=enabled \
  -Drepart=enabled \
  -Dsysupdate=enabled \
  -Dpolkit=disabled \
  -Dseccomp=enabled \
  -Dfdisk=enabled \
  -Dxenctrl=disabled \
  -Dpwquality=%{sd_cyc} \
  -Dpasswdqc=disabled \
  -Dpam=%{sd_cyc} \
  -Dsysupdated=enabled \
  -Dcryptolib=openssl \
  -Ddns-over-tls=openssl \
  -Dnss-mymachines=enabled \
  -Dnss-resolve=enabled \
  -Dresolve=true \
  -Dselinux=enabled \
  -Dacl=enabled \
  -Dopenssl=enabled \
  -Dzlib=enabled \
  -Dbzip2=enabled \
  -Dxz=enabled \
  -Dlz4=enabled \
  -Dzstd=enabled \
  -Dlibarchive=enabled \
  -Ddbus=%{sd_cyc} \
  -Dglib=%{sd_cyc} \
  -Dpcre2=enabled \
  -Dblkid=enabled \
  -Dkmod=disabled
%oreon_meson_build

%install
%oreon_meson_install
rm -f %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  [ -n "$r" ] || continue
  keep=
  oldifs=$IFS
  IFS=:
  for p in $r; do
    case "$p" in
      /usr/lib64/systemd|/usr/lib/systemd) keep="${keep:+$keep:}$p" ;;
    esac
  done
  IFS=$oldifs
  [ "$keep" = "$r" ] && continue
  chmod u+w "$f"
  if [ -n "$keep" ]; then
    patchelf --set-rpath "$keep" "$f"
  else
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

%changelog
* Tue Oct 27 2026 Oreon Packaging Team <packaging@oreonhq.com> - 259.10-1
- 259.10
