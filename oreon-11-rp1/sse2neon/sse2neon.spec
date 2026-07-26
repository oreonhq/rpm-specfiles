%global source0_hash e251746e3b761f3f0de1ad462b1efe53532341b6b0498d394765fceb85ce8a46

# This package only contains header files.
%global debug_package %{nil}
%global commit 706d3b58025364c2371cafcf9b16e32ff7e630ed
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20240816
%global git 0

Name:       sse2neon
Version:    1.8.0
Release:    %autorelease
Summary:    A translator from Intel SSE intrinsics to Arm/Aarch64 NEON implementation
License:    MIT
URL:        https://github.com/DLTcollab/sse2neon
%if 0%{?git}
Source:     %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source:     %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif
Patch:      sse2neon-run-more-tests-on-gcc.patch
ExclusiveArch: aarch64
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make

%global common_description %{expand:
sse2neon is a translator of Intel SSE (Streaming SIMD Extensions) intrinsics to
Arm NEON, shortening the time needed to get an Arm working program that then
can be used to extract profiles and to identify hot paths in the code. The
header file sse2neon.h contains several of the functions provided by Intel
intrinsic headers such as <xmmintrin.h>, only implemented with NEON-based
counterparts to produce the exact semantics of the intrinsics.}

%description
%{common_description}

%package    devel
Summary:    %{summary}
Provides:   %{name}-static = %{version}-%{release}

%description devel
%{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?git}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1
%endif

%install
install -dm755 %{buildroot}%{_includedir}
install -pm644 %{name}.h %{buildroot}%{_includedir}

%check
%make_build check

%files devel
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_includedir}/%{name}.h

%changelog
%autochangelog
