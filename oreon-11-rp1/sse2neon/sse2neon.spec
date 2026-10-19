%global source0_hash 6b70e7cb8c5ce4641002b85deaafe97efdf9ade9b49884edeaf678b35f0e132f
%global debug_package %{nil}
%global commit 706d3b58025364c2371cafcf9b16e32ff7e630ed
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20240816
%global git 0
Name:       sse2neon
Version:    1.9.1
Release:        1%{?dist}
Summary:        A translator from Intel SSE intrinsics to Arm/Aarch64 NEON implementation
License:    MIT
URL:        https://github.com/DLTcollab/sse2neon
%if 0%{?git}
Source0:        https://github.com/DLTcollab/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%else
%endif
Patch:      sse2neon-run-more-tests-on-gcc.patch
ExclusiveArch: aarch64
%global common_description %{expand:
sse2neon is a translator of Intel SSE (Streaming SIMD Extensions) intrinsics to
Arm NEON, shortening the time needed to get an Arm working program that then
can be used to extract profiles and to identify hot paths in the code. The
header file sse2neon.h contains several of the functions provided by Intel
intrinsic headers such as <xmmintrin.h>, only implemented with NEON-based
counterparts to produce the exact semantics of the intrinsics.}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%make_build check
%files -f %{oreon_filedir}/main.list
%files -n sse2neon-devel -f %{oreon_filedir}/sse2neon-devel.list

%changelog

%autochangelog
