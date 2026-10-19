%global source7_hash 93f4b1547c5a66aa084894348d8d26fcd54e74c4b4e99e30320ca4e1498c66f8
%global source0_hash 287450f5f4d1afaab6954272cc986e1a4ba5c7b71a28303a70f45996c786980e
Name:           CuraEngine
Epoch:          1
Version:        5.13.0
Release:        1%{?dist}
Summary:        Engine for processing 3D models into G-code instructions for 3D printers
License:        AGPL-3.0-or-later
URL:            https://github.com/Ultimaker/%{name}
Source0:        https://github.com/Ultimaker/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        FindGMock.cmake
Source3:        FindPolyclipping.cmake
Source4:        FindStb.cmake
Source5:        CMakeLists.txt
Source6:        CPackConfig.cmake
%global scripta_version c378c837eeb505146ab67abe0904bfed2099128f
Source7:        https://github.com/Ultimaker/Scripta_public/archive/%{scripta_version}/Scripta_public-%{scripta_version}.tar.gz
Provides:       bundled(scripta) = %{scripta_version}
Patch0:         %{name}-static-libstdcpp.patch
Patch1:         CuraEngine-5.4.0-fmt10.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libarcus-devel
BuildRequires:  polyclipping-devel
BuildRequires:  protobuf-devel
BuildRequires:  range-v3-devel
BuildRequires:  rapidjson-devel
BuildRequires:  spdlog-devel
BuildRequires:  stb_image-static
# /oreon:deps
%description
%{name} is a C++ console application for 3D printing G-code generation. It
has been made as a better and faster alternative to the old Skeinforge engine.

This is just a console application for G-code generation. For a full graphical
application look at cura with is the graphical frontend for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

mkdir cmake
cp -a %{SOURCE2} %{SOURCE3} %{SOURCE4} cmake
rm -rf CMakeLists.txt
cp -a %{SOURCE5} %{SOURCE6} .

tar xf %{SOURCE7}
mv Scripta_public-%{scripta_version}/include/scripta/ include/

%patch -P0 -p1
%patch -P1 -p1

# bundled libraries
rm -rf libs

# The -DCURA_ENGINE_VERSION does not work, so we sed-change the default value
# sed -i 's/"DEV"/"%{version}"/' src/settings/Settings.h

%build

%cmake \
  -DSET_RPATH:BOOL=OFF \
  -DBUILD_SHARED_LIBS:BOOL=OFF \
  -DCURA_ENGINE_VERSION:STRING=%{version} \
  -DUSE_SYSTEM_LIBS:BOOL=ON \
  -DCMAKE_CXX_FLAGS_RELEASE_INIT:STRING="%{optflags} -fPIC" \
  -DStb_INCLUDE_DIRS:PATH=%{_includedir}
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

%{buildroot}%{_bindir}/%{name} help
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
