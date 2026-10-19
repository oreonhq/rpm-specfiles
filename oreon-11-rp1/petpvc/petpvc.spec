%global source0_hash 026f5e0d06400f57f3baed0084e7e319b704af57a7e4e4784bd854155ccfac98
Name:           petpvc
Version:        1.2.12
Release:        1%{?dist}
Summary:        Tools for partial volume correction (PVC) in positron emission tomography (PET)
%global forgeurl https://github.com/UCL/PETPVC
%global tag v%{version}
%forgemeta
License:        Apache-2.0
URL:            %forgeurl
Source0:        %{forgeurl}/archive/%{tag}/PETPVC-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(ITK)
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  gdcm-devel
BuildRequires:  gtest-devel
BuildRequires:  libXext-devel
BuildRequires:  libminc-devel
BuildRequires:  vxl-devel
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup
# Do not install examples
sed -i -e "/parc/d" CMakeLists.txt
# correct wrong file end of line encoding
sed -i 's/\r$//' parc/{FS.csv,GIF_v3.csv}

%build

flags=( -std=gnu++11
        -Wno-unused-variable
        -Wno-unused-but-set-variable
        -Wno-unused-local-typedefs
      )
export ITK_DIR=%{_libdir}/cmake/InsightToolkit
%cmake \
-DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS ${flags[*]}"
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

%global _smp_mflags "-j1"
%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
