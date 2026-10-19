%global source0_hash d62d24241232a526491328f341df9add274fc84ae9818470d3edb5ae6141ac63
%bcond_with         oidn
Name:               openpgl
Version:            0.7.1
Release:        1%{?dist}
Summary:        Open Path Guiding Library
License:            Apache-2.0
URL:                https://github.com/OpenPathGuidingLibrary/%{name}
Source0:        https://github.com/OpenPathGuidingLibrary/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with oidn}
%endif
ExclusiveArch:      aarch64 x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  embree-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(tbb)
# /oreon:deps
%description
The Intel Open Path Guiding Library (Intel Open PGL) implements
a set of representations and training algorithms needed to 
integrate path guiding into a renderer. 

%package devel
Summary:            Development files for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Convert non-UTF8 third-party file to UTF-8
iconv -f ISO-8859-1 -t UTF-8 -o third-party-programs-oneTBB.txt.new \
    third-party-programs-oneTBB.txt &&
mv third-party-programs-oneTBB.txt.new third-party-programs-oneTBB.txt

# Remove LICENSE.txt from installation list
sed -i '/LICENSE.txt/d' openpgl/CMakeLists.txt

%build

%cmake \
    -DCMAKE_CXX_FLAGS="%{optflags} -flax-vector-conversions" \
    %{?with_oidn:-DOPENPGL_EF_IMAGE_SPACE_GUIDING_BUFFER=ON} \
%ifarch x86_64
    -DOPENPGL_ISA_AVX512=ON \
%else
    -DOPENPGL_ISA_NEON=ON \
    -DOPENPGL_ISA_NEON2X=ON
%endif
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest -V
%files -f %{oreon_filedir}/main.list
%files -n openpgl-devel -f %{oreon_filedir}/openpgl-devel.list

%changelog

%autochangelog
