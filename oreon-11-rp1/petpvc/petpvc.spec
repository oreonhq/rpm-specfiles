%global source0_hash 026f5e0d06400f57f3baed0084e7e319b704af57a7e4e4784bd854155ccfac98

Name:           petpvc
Version:        1.2.12
Release:        %autorelease
Summary:        Tools for partial volume correction (PVC) in positron emission tomography (PET)

%global forgeurl https://github.com/UCL/PETPVC
%global tag v%{version}
%forgemeta

License:        Apache-2.0
URL:            %forgeurl
Source:         %forgesource

# Drop i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(ITK)
# XXX: this is workaround for bug in ITK
# /usr/include/InsightToolkit/itkNumericTraits.h:45:10: fatal error: vcl_limits.h: No such file or directory
#  #include "vcl_limits.h" // for std::numeric_limits
#           ^~~~~~~~~~~~~~
BuildRequires:  vxl-devel
# XXX: this is workaround for bug in ITK
BuildRequires:  gdcm-devel
# make[2]: *** No rule to make target '/usr/lib64/libfftw3.so', needed by 'src/pvc_vc'.  Stop.
BuildRequires:  fftw-devel
BuildRequires:  gtest-devel
BuildRequires:  libminc-devel
# make[2]: *** No rule to make target '/usr/lib64/libXext.so', needed by 'src/pvc_relabel'.  Stop.
# (and quite a few more of these)
BuildRequires: libXext-devel

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

%check
# Let it run serial
%global _smp_mflags "-j1"
%ctest

%files
%license LICENSE.txt
%doc README.md parc
%{_bindir}/petpvc
%{_bindir}/pvc_*

%changelog
%autochangelog
