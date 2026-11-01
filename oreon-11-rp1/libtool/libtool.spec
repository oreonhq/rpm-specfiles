%global source0_hash f81f5860666b0bc7d84baddefa60d1cb9fa6fceb2398cc3baca6afaa60266675

Name: libtool
Version: 2.5.4
Release: 1%{?dist}
Summary: Generic shared library support script
License: GPL-2.0-or-later AND LGPL-2.0-or-later
URL: https://www.gnu.org/software/libtool/
Source0: https://ftp.gnu.org/gnu/libtool/libtool-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: make
BuildRequires: m4
BuildRequires: oreon-rpm-macros

%description
The libtool scripts and the libltdl library.

%package ltdl
Summary: Runtime library for libtool modules
Provides: libtool-ltdl = %{version}-%{release}

%description ltdl
The libltdl library that loads libtool modules.

%package ltdl-devel
Summary: Development files for libltdl
Requires: libtool-ltdl%{?_isa} = %{version}-%{release}
Provides: libtool-ltdl-devel = %{version}-%{release}

%description ltdl-devel
Headers and the pkgconfig file for libltdl.

%prep
%autosetup -n libtool-%{version} -p1
%oreon_sha256

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
find %{buildroot} -name '*.la' -delete
rm -rf %{buildroot}%{_infodir}
%oreon_filelist
python3 - %{buildroot} %{_builddir}/%{name}.files %{_builddir}/%{name}-ltdl.files %{_builddir}/%{name}-ltdl-devel.files <<'PY'
import sys
root, src, ltdl, devel = sys.argv[1:]
main, l, d = [], [], []
for line in open(src):
    path = line.strip()
    if not path or path.startswith("%"):
        main.append(line)
        continue
    bare = path.split()[-1]
    if (bare.endswith(".pc") and "ltdl" in bare) or bare.endswith("ltdl.h") or bare.endswith("libltdl.so"):
        d.append(line)
    elif "libltdl.so" in bare:
        l.append(line)
    else:
        main.append(line)
open(src, "w").writelines(main)
open(ltdl, "w").writelines(l)
open(devel, "w").writelines(d)
PY

%files -f %{_builddir}/%{name}.files
%license COPYING

%files ltdl -f %{_builddir}/%{name}-ltdl.files
%license libltdl/COPYING.LIB

%files ltdl-devel -f %{_builddir}/%{name}-ltdl-devel.files
