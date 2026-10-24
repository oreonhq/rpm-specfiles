%global source0_hash 73d419c6e20e874adaa4019372cbd097eecf4d276e13f27ec5e67d35c0bd203c
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libselinux
Version: 3.11
Release: 1%{?dist}
Summary: SELinux runtime library
License: LicenseRef-Public-Domain
URL: https://github.com/SELinuxProject/selinux
Source0: https://github.com/SELinuxProject/selinux/releases/download/%{version}/libselinux-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: pcre2-devel
BuildRequires: libsepol-devel
BuildRequires: patchelf
%endif

%description
libselinux is the SELinux runtime library.

%package devel
Summary: SELinux runtime library
Requires: libselinux%{?_isa} = %{version}-%{release}

%description devel
libselinux is the SELinux runtime library.

%prep
%oreon_sha256
%autosetup -p1

%build
export CFLAGS="%{_oreon_cflags} -fPIC"
export LDFLAGS="%{_oreon_ldflags}"
make %{?_smp_mflags} PREFIX=%{_prefix} LIBDIR=%{_libdir} SHLIBDIR=%{_libdir} DISABLE_RPM=y USE_PCRE2=y

%install
export CFLAGS="%{_oreon_cflags} -fPIC"
export LDFLAGS="%{_oreon_ldflags}"
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} SHLIBDIR=%{_libdir} DISABLE_RPM=y USE_PCRE2=y
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
%license LICENSE

%files devel -f %{_builddir}/%{name}-devel.files
