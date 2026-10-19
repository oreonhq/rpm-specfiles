%global source0_hash ed2a3268658f2f2a9b5367628a85ccd4cf9516460ed8604eed369653d49b25fb
%global commit_simde fefc7857ff3e785b988a61a8f5f3c5bd5eb24342
%global short_commit_simde %(c=%{commit_simde}; echo ${c:0:7})
%global debug_package %{nil}
%undefine _auto_set_build_flags
%global simde_version 0.8.2
Name: simde
Version: %{simde_version}%{?rc_version:~rc%{rc_version}}
Release:        1%{?dist}
Summary:        Implementations of SIMD instruction sets for non-native systems
License: MIT AND CC0-1.0
URL: https://github.com/simd-everywhere/simde
Source0:        https://github.com/simd-everywhere/simde/archive/v%{version}/simde-%{version}.tar.gz
Patch: https://github.com/simd-everywhere/simde/pull/1220/commits/a891834ff66c80bb9e0491d6be92c7ab7ed6362f.patch#/simde-issue-1200.patch
Patch: https://github.com/simd-everywhere/simde/commit/f046ab773733f09edaadec30345b592dfe85368e.patch
Patch: https://github.com/simd-everywhere/simde/commit/a1ce45cf5dc2253a1f9c0590fe111ebd8d1613c0.patch
Patch: %{name}-clang20.patch
Patch: %{name}-gcc16.patch
# oreon:deps
BuildRequires:  /bin/time
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hedley-devel
BuildRequires:  hedley-static
BuildRequires:  meson
# /oreon:deps
%description
%{summary}
The SIMDe header-only library provides fast, portable implementations of SIMD
intrinsics on hardware which doesn't natively support them, such as calling
SSE functions on ARM. There is no performance penalty if the hardware supports
the native implementation (e.g., SSE/AVX runs at full speed on x86,
NEON on ARM, etc.).

%package devel
Summary: Header files for SIMDe development
Provides: %{name}-static = %{version}-%{release}
Requires: hedley-devel
Requires: hedley-static
BuildArch: noarch
Obsoletes: simde-devel < 0.8.2-2%{?dist}
%description devel
The simde-devel package contains the header files needed
to develop programs that use the SIMDe.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1
ln -svf %{_includedir}/hedley.h %{name}/

%build

%install
mkdir -p %{buildroot}%{_includedir}
cp -a simde %{buildroot}%{_includedir}
ln -svf ../hedley.h %{buildroot}%{_includedir}/%{name}/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

version_major=$(grep '^#define SIMDE_VERSION_MAJOR ' simde/simde-common.h | cut -d ' ' -f 3)
version_minor=$(grep '^#define SIMDE_VERSION_MINOR ' simde/simde-common.h | cut -d ' ' -f 3)
version_micro=$(grep '^#define SIMDE_VERSION_MICRO ' simde/simde-common.h | cut -d ' ' -f 3)
test "%{simde_version}" = "${version_major}.${version_minor}.${version_micro}"
bash - <<\EOF
for file in $(find simde/ -type f); do
  if ! [[ "${file}" =~ \.h$ ]]; then
    echo "${file} is not a header file."
    exit 1
  elif [ -x "${file}" ]; then
    echo "${file} has executable bit."
    exit 1
  fi
done
EOF
cp -p .packit/ci.sh ci.sh
sed -i -e '/^cat \/proc\/cpuinfo/ s/^/#/' ci.sh
sed -i -e '/^cat \/proc\/meminfo/ s/^/#/' ci.sh
sed -i -e '/^pip3 install meson/ s/^/#/' ci.sh
sed -i -e '/^IGNORE_EXIT_STATUS=/ s/^/#/' ci.sh
sed -i -e '/^MATRIX_.*=/ s/^/#/' ci.sh
cat > config.txt <<EOF
IGNORE_EXIT_STATUS=
MATRIX_DEFAULT_GCC_DEFAULT="exclude"
MATRIX_DEFAULT_GCC_O2="exclude"
MATRIX_DEFAULT_GCC_RPM="include"
MATRIX_DEFAULT_CLANG_DEFAULT="exclude"
MATRIX_DEFAULT_CLANG_O2="exclude"
MATRIX_DEFAULT_CLANG_RPM="include"
MATRIX_i686_GCC_RPM="exclude"
MATRIX_i686_CLANG_RPM="exclude"
MATRIX_ppc64le_CLANG_RPM="exclude"
MATRIX_s390x_CLANG_RPM="exclude"
EOF
sed -i -e '/^# Configuration$/r config.txt' ci.sh
if diff -u .packit/ci.sh ci.sh; then
  exit 1
elif [ "${?}" != 1 ]; then
  exit 2
fi
%global toolchain clang
export CI_CLANG_RPM_CFLAGS="%{build_cflags} -fno-strict-aliasing"
export CI_CLANG_RPM_CXXFLAGS="%{build_cxxflags} -fno-strict-aliasing"
export CI_CLANG_RPM_LDFLAGS="%{build_ldflags}"
%global toolchain gcc
export CI_GCC_RPM_CFLAGS="%{build_cflags} -fno-strict-aliasing"
export CI_GCC_RPM_CXXFLAGS="%{build_cxxflags} -fno-strict-aliasing"
export CI_GCC_RPM_LDFLAGS="%{build_ldflags}"
/bin/time -f '=> [%E]' ./ci.sh
%files -f %{oreon_filedir}/main.list
%files -n simde-devel -f %{oreon_filedir}/simde-devel.list

%changelog

%autochangelog
