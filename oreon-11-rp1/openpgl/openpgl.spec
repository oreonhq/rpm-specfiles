%global source0_hash d62d24241232a526491328f341df9add274fc84ae9818470d3edb5ae6141ac63

# Experimental image-space guiding buffer feature disabled by default
%bcond_with         oidn
Name:               openpgl
Version:            0.7.1
Release:            %autorelease
Summary:            Open Path Guiding Library

License:            Apache-2.0
URL:                https://github.com/OpenPathGuidingLibrary/%{name}
Source0:            %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:      cmake
BuildRequires:      embree-devel
BuildRequires:      gcc-c++
%if %{with oidn}
BuildRequires:      oidn-devel
%endif
BuildRequires:      pkgconfig(tbb)

# Upstream only supports x86_64 and ARM64 architectures
ExclusiveArch:      aarch64 x86_64

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

%check
%ctest -V

%files
%license LICENSE.txt
%doc CHANGELOG.md README.md third-party-programs*.txt
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}-%{version}
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
