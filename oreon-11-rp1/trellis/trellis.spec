%global source1_hash bbf219d49d89b9e22b5cd0f5c5b7fb33a8dbd77e5f4c54669709a6e4789dab87
%global source0_hash d6474805bc0f998a5b78767d5a0464e244e4b5d7e2420271d9adb031d848fd48
%global commit0 92345b77edf775fe5668700dd9931e19db2d36b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commit1 015e0330630d7c238c0e4f2cdd9c8157eb78c54a
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})
%global snapdate 20251010
%global __python %{__python3}
Name:          trellis
Version:       1.2.1
Release:        1%{?dist}
Summary:        Lattice ECP5 FPGA bitstream creation/analysis/programming tools
License:       ISC
URL:           https://github.com/YosysHQ/prj%{name}
Source0:        https://github.com/YosysHQ/prj%{name}/archive/%{commit0}/prj%{name}-%{shortcommit0}.tar.gz
Source1:       https://github.com/YosysHQ/prj%{name}-db/archive/%{commit1}/prj%{name}-db-%{shortcommit1}.tar.gz
Requires:      %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  boost-python3-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  latexmk
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-recommonmark
BuildRequires:  python3-sphinx-latex
# /oreon:deps
%description
Project Trellis enables a fully open-source flow for ECP5 FPGAs using
Yosys for Verilog synthesis and nextpnr for place and route. Project
Trellis provides the device database and tools for bitstream creation.

%package devel
Summary:       Development files for Project Trellis
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      %{name}-data = %{version}-%{release}
%if "%{?python3_version}" != ""
Requires:      python(abi) = %{python3_version}
%endif
%description devel
Development files to build packages using Project Trellis

%package data
Summary:       Project Trellis - Lattice ECP5 Bitstream Database
BuildArch:     noarch
%description data
This package contains the bitstream documentation database for
Lattice ECP5 FPGA devices.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n prj%{name}-%{commit0} -a 1
rm -rf database
mv prj%{name}-db-%{commit1} database
# add "-fPIC -g1" to CMAKE_CXX_FLAGS:
# (NOTE: "-g1" reduces debuginfo verbosity over "-g", which helps on armv7hl)
sed -i '/CMAKE_CXX_FLAGS/s/-O3/-O3 -fPIC -g1/' libtrellis/CMakeLists.txt
# prevent "lib64" false positive (e.g., on i386):
sed -i 's/"lib64"/"lib${LIB_SUFFIX}"/' libtrellis/CMakeLists.txt
# fix shebang lines in Python scripts:
find . -name \*.py -exec sed -i 's|/usr/bin/env python3|/usr/bin/python3|' {} \;
# remove .gitignore files in examples:
find . -name \.gitignore -delete

%build

%define __cmake_in_source_build 1
%define _lto_cflags %{nil}
%cmake libtrellis \
	-DCURRENT_GIT_VERSION=%{version}-%{release}
%cmake_build
%make_build -C docs latexpdf
mkdir man1
for f in ecp*
do
  [ -x $f ] || continue
  LD_PRELOAD=./libtrellis.so \
    help2man --no-discard-stderr --version-string %{version} -N \
             -o man1/$f.1 ./$f
  sed -i '/required but missing/d' man1/$f.1
done
%install
%cmake_install
install -Dpm644 -t %{buildroot}%{_mandir}/man1 man1/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n trellis-devel -f %{oreon_filedir}/trellis-devel.list
%files -n trellis-data -f %{oreon_filedir}/trellis-data.list

%changelog

%autochangelog
