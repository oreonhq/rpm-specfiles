%global source0_hash 242b2ecab5018a42ba80d8df58528ecb9edf419caa671eca4864234672bf025d
%undefine __cmake_in_source_build
%global compression_tests 0
%global desc \
TRAJNG (Trajectory next generation) is a program library for handling\
molecular dynamics (MD) trajectories. It can store coordinates, and\
optionally velocities and the H-matrix. Coordinates and velocities are\
stored with user-specified precision. In addition, program specific\
information (text strings) can optionally be stored in the beginning\
of each file. Atomic labels can also optionally be stored once in the\
beginning of the file.
Name:          tng
Version:       1.8.2
Release:        22%{?dist}
Summary:        Trajectory Next Generation binary format manipulation library
License:       LicenseRef-Callaway-BSD AND Zlib
Source0:        https://github.com/gromacs/tng/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:        tng-gf12.patch
Patch1:        49.patch
URL:           http://www.gromacs.org/Developer_Zone/Programming_Guide/File_formats
Provides:      bundled(md5-deutsch)
# oreon:deps
BuildRequires:  cmake3
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  zlib-devel
# /oreon:deps
%description
%{desc}

%package devel
Summary:       Trajectory Next Generation binary format manipulation library development files
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description devel
%{desc}

This package contains the development files.

%package doc
Summary:       Trajectory Next Generation binary format manipulation library documentation
BuildArch:     noarch
%description doc
%{desc}

This package contains the documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{cmake3} \
    -DTNG_BUILD_DOCUMENTATION=ON \
    -DTNG_BUILD_FORTRAN=ON \
%if 0%{?compression_tests} > 0
    -DTNG_BUILD_COMPRESSION_TESTS=ON \
%endif
    -DTNG_BUILD_WITH_ZLIB=ON \
    %{nil}
%cmake3_build
%install
%cmake3_install
rm -r %{buildroot}%{_datadir}/tng/doc/latex
mkdir -p %{buildroot}%{_defaultdocdir}
mv %{buildroot}{%{_datadir}/tng/doc/html,%{_defaultdocdir}/tng}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd %{_vpath_builddir}/bin/tests
./tng_testing
popd
%if 0%{?compression_tests}
pushd %{_vpath_builddir}/bin/compression_tests
./test_tng_compress_write.sh
./test_tng_compress_read.sh
popd
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n tng-devel -f %{oreon_filedir}/tng-devel.list
%files -n tng-doc -f %{oreon_filedir}/tng-doc.list

%changelog

%autochangelog
