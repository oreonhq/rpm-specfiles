# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 38b4ee1924f8bd1ec0f6b2ec147e4c54c6deac132db5f90b4214b43ccd32fdd6

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global libname solv

%bcond_without python_bindings
%bcond_without perl_bindings
%bcond_without ruby_bindings
# Creates special prefixed pseudo-packages from appdata metadata
%bcond_without appdata
# Creates special prefixed "group:", "category:" pseudo-packages
%bcond_without comps
%bcond_without conda
# For rich dependencies
%bcond_without complex_deps
%bcond_without helix_repo
%bcond_without suse_repo
%bcond_without debian_repo
%bcond_without arch_repo
%bcond_without apk_repo
# For handling deb + rpm at the same time
%bcond_without multi_semantics
%bcond_without openssl
%bcond_without zchunk
%bcond_without zstd

%define __cmake_switch(b:) %[%{expand:%%{?with_%{-b*}}} ? "ON" : "OFF"]

Name:           lib%{libname}
Version:        0.7.41
Release:        1%{?dist}
Summary:        Package dependency solver

# LICENSE.BSD:      BSD-3-Clause text
# other files:      "read LICENSE.BSD"
# src/sha2.c:       BSD-3-Clause
# src/sha2.h:       BSD-3-Clause
## Used at build time but not in any binary package
# cmake/modules/_CMakeParseArguments.cmake:             BSD-3-Clause
# cmake/modules/FindPackageHandleStandardArgs.cmake:    BSD-3-Clause
# cmake/modules/FindRuby.cmake:                         BSD-3-Clause
# package/libsolv.spec.in:  (project's license IF open-source) XOR (MIT IF not in open-source project)
## Not used at build time and not in any binary package
# src/qsort_r.c:    BSD-3-Clause
# win32/LICENSE:    MIT text AND BSD-2-Clause text
# win32/regcomp.c:  BSD-2-Clause
# win32/regexec.c:  BSD-2-Clause
# win32/tre.h:      BSD-2-Clause
# win32/tre-mem.c:  BSD-2-Clause
License:        BSD-3-Clause
SourceLicense:  %{license} AND BSD-2-Clause AND MIT
URL:            https://github.com/openSUSE/libsolv
Source0:        https://github.com/openSUSE/libsolv/archive/%{version}/libsolv-%{version}.tar.gz
# Provides: python3dist(solv) in python3-solv
# https://github.com/openSUSE/libsolv/pull/602
Patch:        0001-Python-Provide-dist-info-metadata.patch
# Add "rpm" INSTALLER to Python metadata, not suitable for upstream.
# Requires Python-Provide-dist-info-metadata.patch.
Patch:        0002-Add-INSTALLER-to-Python-metadata.patch
# Fix a buffer overflow when decompressing solv pages (CVE-2026-48864),
# rejected by upstream, <https://github.com/openSUSE/libsolv/pull/622>.
Patch:        0003-Fix-a-buffer-overflow-when-decompressing-solv-pages.patch

BuildRequires:  cmake >= 3.5
BuildRequires:  gdb
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(rpm)
BuildRequires:  zlib-devel
# -DWITH_LIBXML2=ON
BuildRequires:  libxml2-devel
%if %{with openssl}
# -DWITH_OPENSSL=ON
BuildRequires:  coreutils
BuildRequires:  openssl-devel >= 3.1.0
%endif
# -DENABLE_LZMA_COMPRESSION=ON
BuildRequires:  xz-devel
# -DENABLE_BZIP2_COMPRESSION=ON
BuildRequires:  bzip2-devel
%if %{with zchunk} || %{with zstd} || %{with apk}
# -DENABLE_ZSTD_COMPRESSION=ON
BuildRequires:  libzstd-devel
%endif
%if %{with zchunk}
# -DENABLE_ZCHUNK_COMPRESSION=ON
BuildRequires:  pkgconfig(zck)
%endif

%description
A free package dependency solver using a satisfiability algorithm. The
library is based on two major, but independent, blocks:

- Using a dictionary approach to store and retrieve package
  and dependency information.

- Using satisfiability, a well known and researched topic, for
  resolving package dependencies.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       rpm-devel%{?_isa}

%description devel
Development files for %{name}.

%package tools-base
Summary:        Utilities used by libzypp to manage .solv files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libsolv-tools:%{_bindir}/repo2solv
Conflicts:      libsolv-tools < %{version}

%description tools-base
This subpackage contains utilities used by libzypp to manage solv files.

%package tools
Summary:        Package dependency solver tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
# repo2solv dependencies. Used as execl()
Requires:       libsolv-tools-base = %{version}-%{release}

%description tools
Package dependency solver tools.

%package demo
Summary:        Applications demoing the %{name} library
Requires:       %{name}%{?_isa} = %{version}-%{release}
# solv dependencies. Used as execlp() and system()
Requires:       /usr/bin/curl
Requires:       /usr/bin/gpg2

%description demo
Applications demoing the %{name} library.

%if %{with perl_bindings}
%package -n perl-%{libname}
Summary:        Perl bindings for the %{name} library
BuildRequires:  swig
BuildRequires:  perl-devel
BuildRequires:  perl-generators
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n perl-%{libname}
Perl bindings for the %{name} library.
%endif

%if %{with ruby_bindings}
%package -n ruby-%{libname}
Summary:        Ruby bindings for the %{name} library
BuildRequires:  swig
BuildRequires:  ruby-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ruby-%{libname}
Ruby bindings for the %{name} library.
%endif

%if %{with python_bindings}
%package -n python3-%{libname}
Summary:        Python bindings for the %{name} library
%{?python_provide:%python_provide python3-%{libname}}
BuildRequires:  swig
BuildRequires:  python3-devel
BuildRequires:  oreon-rpm-macros
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{libname}
Python bindings for the %{name} library.

Python 3 version.
%endif

%prep
%oreon_sha256

%autosetup -p1
%if %{with openssl}
# Unbundle private cryptography
rm src/chksum_impl.c src/md5.{c,h} src/sha1.{c,h} src/sha2.{c,h}
%endif

%build
specdir=$PWD/oreon-specs
wrapdir=$PWD/oreon-cc
mkdir -p "$specdir" "$wrapdir"
cp -L %{_rpmconfigdir}/oreon/oreon-hardened-cc1 "$specdir/hardened-cc1"
cp -L %{_rpmconfigdir}/oreon/oreon-hardened-ld "$specdir/hardened-ld"
cp -L %{_rpmconfigdir}/oreon/oreon-hardened-ld-errors "$specdir/hardened-ld-errors"
plugindir=$(/usr/bin/gcc -print-file-name=plugin)
plugin=
for cand in "$plugindir/gcc-annobin.so" "$plugindir/annobin.so"; do
  if [ -e "$cand" ]; then
    plugin=$cand
    break
  fi
done
if [ -n "$plugin" ]; then
  printf '%s\n' '*cc1_options:' "+ -fplugin=$plugin" > "$specdir/annobin-cc1"
else
  cp -L %{_rpmconfigdir}/oreon/oreon-annobin-cc1 "$specdir/annobin-cc1"
fi
cat > "$wrapdir/ccwrap.py" << 'PY'
import os, sys
specdir = os.environ["OREON_SPECDIR"]
rpm = os.environ["OREON_RPMCONFIG"]
repl = {
    rpm + "/redhat/redhat-hardened-cc1": specdir + "/hardened-cc1",
    rpm + "/oreon/oreon-annobin-cc1": specdir + "/annobin-cc1",
    rpm + "/redhat/redhat-hardened-ld": specdir + "/hardened-ld",
    rpm + "/redhat/redhat-hardened-ld-errors": specdir + "/hardened-ld-errors",
}
args = []
for a in sys.argv[1:]:
    if a.startswith("-specs="):
        path = a[len("-specs="):]
        if "annobin-cc1" in path:
            path = specdir + "/annobin-cc1"
        else:
            path = repl.get(path, path)
        if "/redhat/" in path and not os.path.exists(path):
            continue
        a = "-specs=" + path
    elif a == "-fplugin=annobin" or a.startswith("-fplugin=annobin"):
        plug = os.environ.get("OREON_ANNOBIN")
        if plug:
            a = "-fplugin=" + plug
    args.append(a)
os.execv(os.environ["OREON_REAL_CC"], [os.environ["OREON_REAL_CC"], *args])
PY
for pair in "gcc:/usr/bin/gcc" "cc:/usr/bin/gcc" "g++:/usr/bin/g++" "c++:/usr/bin/c++"; do
  name=${pair%%:*}
  real=${pair#*:}
  cat > "$wrapdir/$name" << EOF
#!/bin/sh
export OREON_SPECDIR="$specdir"
export OREON_RPMCONFIG="%{_rpmconfigdir}"
export OREON_ANNOBIN="$plugin"
export OREON_REAL_CC=$real
exec /usr/bin/python3 "$wrapdir/ccwrap.py" "\$@"
EOF
  chmod +x "$wrapdir/$name"
done
export PATH="$wrapdir:$PATH"
export CC="$wrapdir/gcc"
export CXX="$wrapdir/g++"
%cmake -GNinja                                            \
  -DFEDORA=1                                              \
  -DENABLE_RPMDB=ON                                       \
  -DENABLE_RPMDB_BYRPMHEADER=ON                           \
  -DENABLE_RPMDB_LIBRPM=ON                                \
  -DENABLE_RPMPKG_LIBRPM=ON                               \
  -DENABLE_RPMMD=ON                                       \
  -DENABLE_STATIC_BINDINGS=OFF                            \
  -DENABLE_STATIC_TOOLS=OFF                               \
  -DENABLE_COMPS=%{__cmake_switch -b comps}               \
  -DENABLE_APPDATA=%{__cmake_switch -b appdata}           \
  -DUSE_VENDORDIRS=ON                                     \
  -DWITH_LIBXML2=ON                                       \
  -DENABLE_LZMA_COMPRESSION=ON                            \
  -DENABLE_BZIP2_COMPRESSION=ON                           \
  -DWITH_OPENSSL=%{__cmake_switch -b openssl}             \
  -DENABLE_ZSTD_COMPRESSION=%{__cmake_switch -b zstd}     \
  -DENABLE_ZCHUNK_COMPRESSION=%{__cmake_switch -b zchunk} \
%if %{with zchunk}
  -DWITH_SYSTEM_ZCHUNK=ON                                 \
%endif
  -DENABLE_HELIXREPO=%{__cmake_switch -b helix_repo}      \
  -DENABLE_SUSEREPO=%{__cmake_switch -b suse_repo}        \
  -DENABLE_DEBIAN=%{__cmake_switch -b debian_repo}        \
  -DENABLE_ARCHREPO=%{__cmake_switch -b arch_repo}        \
  -DENABLE_APK=%{__cmake_switch -b apk_repo}              \
  -DMULTI_SEMANTICS=%{__cmake_switch -b multi_semantics}  \
  -DENABLE_COMPLEX_DEPS=%{__cmake_switch -b complex_deps} \
  -DENABLE_CONDA=%{__cmake_switch -b conda}               \
  -DENABLE_PERL=%{__cmake_switch -b perl_bindings}        \
  -DENABLE_RUBY=%{__cmake_switch -b ruby_bindings}        \
  -DENABLE_PYTHON=%{__cmake_switch -b python_bindings}    \
%if %{with python_bindings}
  -DPYTHON_EXECUTABLE=%{python3}                          \
%endif
  %{nil}
%cmake_build

%install
%cmake_install
%if %{with python_bindings}
: > python3-solv.files
find %{buildroot} -path '*/site-packages/*' | while read -r f; do
  b=${f#%{buildroot}}
  case $b in
    */site-packages/_solv.so)
      echo "$b" >> python3-solv.files
      echo "${b%%/_solv.so}/__pycache__/solv.*" >> python3-solv.files
      ;;
    */site-packages/solv.py|*/site-packages/__pycache__/solv.*|*/site-packages/solv-*.dist-info|*/site-packages/solv-*.dist-info/*)
      echo "$b" >> python3-solv.files
      ;;
  esac
done
%endif

%check
%ctest

# Python smoke test (not tested in %%ctest):
pyplat=$(%{python3} -c "import sysconfig; print(sysconfig.get_path('platlib'))")
export PYTHONPATH="%{buildroot}$pyplat"
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%python3 -c 'import solv'

%files
%license LICENSE*
%doc NEWS README TODO
%{_libdir}/%{name}.so.*
%{_libdir}/%{name}ext.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/%{name}ext.so
%{_includedir}/%{libname}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}ext.pc
# Own directory because we don't want to depend on cmake
%dir %{_datadir}/cmake/Modules/
%{_datadir}/cmake/Modules/FindLibSolv.cmake
%{_mandir}/man3/%{name}*.3*

# Some small macro to list tools with mans
%global solv_tool() \
%{_bindir}/%{1}\
%{_mandir}/man1/%{1}.1*

%files tools-base
%solv_tool repo2solv
%solv_tool rpmdb2solv

%files tools
%solv_tool deltainfoxml2solv
%solv_tool dumpsolv
%solv_tool installcheck
%solv_tool mergesolv
%solv_tool repomdxml2solv
%solv_tool rpmmd2solv
%solv_tool rpms2solv
%solv_tool testsolv
%solv_tool updateinfoxml2solv
%if %{with comps}
  %solv_tool comps2solv
%endif
%if %{with appdata}
  %solv_tool appdata2solv
%endif
%if %{with debian_repo}
  %solv_tool deb2solv
%endif
%if %{with arch_repo}
  %solv_tool archpkgs2solv
  %solv_tool archrepo2solv
%endif
%if %{with apk_repo}
  %solv_tool apk2solv
%endif
%if %{with helix_repo}
  %solv_tool helix2solv
%endif
%if %{with suse_repo}
  %solv_tool susetags2solv
%endif
%if %{with conda}
  %{_bindir}/conda2solv
%endif

%files demo
%solv_tool solv

%if %{with perl_bindings}
%files -n perl-%{libname}
%{perl_vendorarch}/%{libname}.pm
%{perl_vendorarch}/%{libname}.so
%endif

%if %{with ruby_bindings}
%files -n ruby-%{libname}
%{ruby_vendorarchdir}/%{libname}.so
%endif

%if %{with python_bindings}
%files -n python3-%{libname} -f python3-solv.files
%endif

