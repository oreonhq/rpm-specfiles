%global source0_hash 43b9fe684cc2569bca2d01595195ffe7f0d6df6f0d7dad29b5b1ccda218df451
%bcond_with debug
Name: gtengine
Summary:        Library for computations in mathematics, graphics, image analysis, and physics
Version: 7.2
Release:        1%{?dist}
Epoch: 1
License: BSL-1.0
URL: http://www.geometrictools.com
Source0:        https://github.com/davideberly/GeometricTools/archive/GTE-version-%{version}/GeometricTools-GTE-version-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libstdc++-devel
BuildRequires:  make
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
# /oreon:deps
%description
A library of source code for computing in the fields of mathematics,
graphics, image analysis, and physics.
The engine is written in C++ 11 and, as such, has portable access
to standard constructs for multithreading programming on cores.
The engine also supports high-performance computing using general
purpose GPU programming (GPGPU).
SIMD code is also available using Intel Streaming SIMD Extensions (SSE).

GTEngine requires OpenGL 4.5.0 (or later).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = 1:%{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package samples
Summary: Samples files of %{name}
Requires: %{name}%{?_isa} = 1:%{version}-%{release}
%description samples
This package contains samples files for
testing that use %{name}.

%prep

%autosetup -n GeometricTools-GTE-version-%{version}

# Remove -Werror flags (rhbz#1923590)
find . -type f \( -name "CMakeLists.txt" \) -exec sed -i 's| -Werror||g' '{}' \;

sed -i 's|GTE_VERSION_MINOR 1|GTE_VERSION_MINOR 2|g' -i GTE/CMakeLists.txt

%build

%if %{with debug}
%cmake -S GTE -DCMAKE_BUILD_TYPE:STRING=Debug -DBUILD_RELEASE_LIB:BOOL=ON -DBUILD_SHARED_LIB:BOOL=ON
%else
%cmake -S GTE -DCMAKE_BUILD_TYPE:STRING=Release -DBUILD_RELEASE_LIB:BOOL=ON -DBUILD_SHARED_LIB:BOOL=ON
%endif
%cmake_build
pushd GTE
%if %{with debug}
%cmake -S Samples -DCMAKE_SKIP_RPATH:BOOL=ON -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON -DCMAKE_BUILD_TYPE:STRING=Debug \
 -DBUILD_RELEASE_LIB:BOOL=ON -DBUILD_SHARED_LIB:BOOL=ON
%else
%cmake -S Samples -DCMAKE_SKIP_RPATH:BOOL=ON -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON -DCMAKE_BUILD_TYPE:STRING=Release \
 -DBUILD_RELEASE_LIB:BOOL=ON -DBUILD_SHARED_LIB:BOOL=ON
%endif
%cmake_build
popd
%install
echo 'Manual installation...'
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
install -pm 755 GTE/lib/ReleaseShared/* $RPM_BUILD_ROOT%{_libdir}/
ln -sf libgtapplications.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtapplications.so
ln -sf libgtgraphics.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtgraphics.so
ln -sf libgtmathematicsgpu.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtmathematicsgpu.so
ln -sf libgtapplications.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtapplications.so.7
ln -sf libgtgraphics.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtgraphics.so.7
ln -sf libgtmathematicsgpu.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtmathematicsgpu.so.7
mkdir -p $RPM_BUILD_ROOT%{_includedir}/GTE
cp -a GTE/Applications $RPM_BUILD_ROOT%{_includedir}/GTE/
cp -a GTE/Graphics $RPM_BUILD_ROOT%{_includedir}/GTE/
cp -a GTE/Mathematics $RPM_BUILD_ROOT%{_includedir}/GTE/
find $RPM_BUILD_ROOT%{_includedir}/GTE -type f -name "*.cpp" -exec rm -f '{}' \;
mkdir -p $RPM_BUILD_ROOT%{_includedir}/GTL
cp -a GTL/Mathematics $RPM_BUILD_ROOT%{_includedir}/GTL/
cp -a GTL/Utility $RPM_BUILD_ROOT%{_includedir}/GTL/
find $RPM_BUILD_ROOT%{_includedir}/GTL -type f -name "*.vcxproj" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_includedir}/GTL -type f -name "*.sln" -exec rm -f '{}' \;
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -a GTE/Samples $RPM_BUILD_ROOT%{_libexecdir}/%{name}/
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.h" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.cpp" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.filters" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.vcxproj" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.csproj" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.sln" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.gte" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.o" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "cmake*" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "CMake*" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "Makefile" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.json" -exec rm -f '{}' \;
for i in `find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type d -name "CMakeFiles"`; do
 rm -rf $i
done
cat > $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gtengine.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}
xthreadlib=-lpthread
Name: GTEngine
Description: Library for computations in mathematics, graphics, image analysis, and physics
Version: %{version}
Cflags: -I%{_includedir}/GTE -I%{_includedir}/GTL
Libs: -lgtgraphics -lgtmathematicsgpu -lgtapplications
Libs.private: -lpthread
EOF
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gtengine-devel -f %{oreon_filedir}/gtengine-devel.list
%files -n gtengine-samples -f %{oreon_filedir}/gtengine-samples.list

%changelog

%autochangelog
