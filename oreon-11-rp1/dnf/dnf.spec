%global source0_hash fabdc4436e9a8a152d38060602f491bee4245ad54656f01991f33d511c87bfb1
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: dnf
Version: 4.24.0
Release: 1%{?dist}
Summary: Package manager
License: GPL-2.0-or-later
URL: https://github.com/rpm-software-management/dnf
Source0: https://github.com/rpm-software-management/dnf/releases/download/%{version}/dnf-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: python3-devel
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
%endif

Requires: python3-dnf = %{version}-%{release}

%description
dnf is the package manager.

%package -n python3-dnf
Summary: Package manager
Requires: python3
Requires: python3-libdnf
Requires: python3-hawkey
Requires: python3-libcomps
Requires: python3-librepo
Requires: python3-rpm
Requires: python3-dbus

%description -n python3-dnf
dnf is the package manager.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_cmake -DPYTHON_DESIRED=3 -DWITH_MAN=1
%oreon_cmake_build
cmake --build %{_oreon_builddir} --target doc-man

%install
%oreon_cmake_install
%oreon_filelist
mv %{_builddir}/%{name}.files %{_builddir}/python3-dnf.files
python3 - %{_builddir}/python3-dnf.files << 'PY'
import os
import sys
from pathlib import Path
p = Path(sys.argv[1])
lines = p.read_text().splitlines()
seen = set(lines)
extra = []
for line in lines:
    path = line.strip().strip('"')
    if not path.endswith(".py"):
        continue
    if "/lib/python3." not in path and "/lib64/python3." not in path:
        continue
    glob = os.path.dirname(path) + "/__pycache__/*"
    if glob not in seen:
        seen.add(glob)
        extra.append(glob)
text = "\n".join(lines + extra)
p.write_text(text + ("\n" if text else ""))
PY

%files
%license COPYING

%files -n python3-dnf -f %{_builddir}/python3-dnf.files
