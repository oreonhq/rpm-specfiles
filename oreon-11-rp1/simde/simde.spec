%global source0_hash ed2a3268658f2f2a9b5367628a85ccd4cf9516460ed8604eed369653d49b25fb

%global commit_simde fefc7857ff3e785b988a61a8f5f3c5bd5eb24342
%global short_commit_simde %(c=%{commit_simde}; echo ${c:0:7})
# Disable debuginfo package for the header only package.
%global debug_package %{nil}

# Disable the auto_set_build_flags. Because it sets clang flags for gcc in
# the %%check section.
%undefine _auto_set_build_flags

%global simde_version 0.8.2
# %%global rc_version 1

Name: simde
Version: %{simde_version}%{?rc_version:~rc%{rc_version}}
# Align the release format with the packages setting Source0 by commit hash
# such as podman.spec and moby-engine.spec.
Release: 6%{?dist}
Summary: Implementations of SIMD instruction sets for non-native systems
# find simde/ -type f | xargs licensecheck
#   simde: MIT
#   simde/check.h: CC0-1.0
#   simde/debug-trap.h: CC0-1.0
#   simde/simde-align.h: CC0-1.0
#   simde/simde-arch.h: CC0-1.0
#   simde/simde-detect-clang.h: CC0-1.0
# removed in %%prep (unbundled):
#   simde/hedley.h: CC0
# Consider relicensing CC0 code to another license (MIT?)
# https://github.com/simd-everywhere/simde/issues/999
License: MIT AND CC0-1.0
URL: https://github.com/simd-everywhere/simde
Source0: https://github.com/simd-everywhere/simde/archive/v%{version}/simde-%{version}.tar.gz
# fix for https://github.com/simd-everywhere/simde/issues/1200
Patch: https://github.com/simd-everywhere/simde/pull/1220/commits/a891834ff66c80bb9e0491d6be92c7ab7ed6362f.patch#/simde-issue-1200.patch
# avoid warnings when "__ARM_NEON_FP" is not defined
Patch: https://github.com/simd-everywhere/simde/commit/f046ab773733f09edaadec30345b592dfe85368e.patch
# Partial fix for https://github.com/simd-everywhere/simde/issues/1203
Patch: https://github.com/simd-everywhere/simde/commit/a1ce45cf5dc2253a1f9c0590fe111ebd8d1613c0.patch
# Avoid undefined behaviour in signed multiplication https://github.com/simd-everywhere/simde/issues/1295
Patch: %{name}-clang20.patch
# gcc and clang are used in the unit tests.
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson
# Header-only library dependency
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
BuildRequires: hedley-devel
BuildRequires: hedley-static
BuildRequires: %{_bindir}/time
# Do not set noarch for header only package.
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries

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
# The API includes the hedley header-only library.
Requires: hedley-devel
Requires: hedley-static
# subpackage can be noarch, it's identical across all arches
# the main package is archful, so tests run on all arches
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
# The %%build section is not used.

%install
mkdir -p %{buildroot}%{_includedir}
cp -a simde %{buildroot}%{_includedir}
ln -svf ../hedley.h %{buildroot}%{_includedir}/%{name}/

%check
# Check version.
version_major=$(grep '^#define SIMDE_VERSION_MAJOR ' simde/simde-common.h | cut -d ' ' -f 3)
version_minor=$(grep '^#define SIMDE_VERSION_MINOR ' simde/simde-common.h | cut -d ' ' -f 3)
version_micro=$(grep '^#define SIMDE_VERSION_MICRO ' simde/simde-common.h | cut -d ' ' -f 3)
test "%{simde_version}" = "${version_major}.${version_minor}.${version_micro}"

# Check if all the shipped file is a valid header file.
# Suppress the command logging during the check by running on bash.
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

# Only test the GCC and Clang cases with RPM build flags.
# If you find test failures on the cases, reproduce it in the upstream CI.
# in the O2 or RPM build flags cases, and report it.
# See <https://github.com/simd-everywhere/simde/blob/master/.packit/>.

# Copy to use the modified script.
cp -p .packit/ci.sh ci.sh
# Suppress the system info.
sed -i -e '/^cat \/proc\/cpuinfo/ s/^/#/' ci.sh
sed -i -e '/^cat \/proc\/meminfo/ s/^/#/' ci.sh
# Use the meson RPM package instead of the PyPI package.
sed -i -e '/^pip3 install meson/ s/^/#/' ci.sh
# Comment out the default configuration.
sed -i -e '/^IGNORE_EXIT_STATUS=/ s/^/#/' ci.sh
sed -i -e '/^MATRIX_.*=/ s/^/#/' ci.sh
# Prepare the configuration.
cat > config.txt <<EOF
IGNORE_EXIT_STATUS=
MATRIX_DEFAULT_GCC_DEFAULT="exclude"
MATRIX_DEFAULT_GCC_O2="exclude"
MATRIX_DEFAULT_GCC_RPM="include"
MATRIX_DEFAULT_CLANG_DEFAULT="exclude"
MATRIX_DEFAULT_CLANG_O2="exclude"
MATRIX_DEFAULT_CLANG_RPM="include"
# https://github.com/simd-everywhere/simde/issues/1201
MATRIX_i686_GCC_RPM="exclude"
# https://github.com/simd-everywhere/simde/issues/1202
MATRIX_i686_CLANG_RPM="exclude"
# https://github.com/llvm/llvm-project/issues/110753
MATRIX_ppc64le_CLANG_RPM="exclude"
# https://github.com/simd-everywhere/simde/issues/1203
MATRIX_s390x_CLANG_RPM="exclude"
EOF
# Insert the configuration.
sed -i -e '/^# Configuration$/r config.txt' ci.sh
# Print the difference on the debugging purpose.
if diff -u .packit/ci.sh ci.sh; then
  exit 1
elif [ "${?}" != 1 ]; then
  exit 2
fi

# Set environment variables to test with RPM build flags.
# See <https://github.com/simd-everywhere/simde/blob/master/.packit/simde.spec>.
# Append the `-fno-strict-aliasing` for a compatibility from the past commit
# below, though it's not related to the shipping simde RPM package.
# https://src.fedoraproject.org/rpms/simde/c/3371c3a422f2512562fd4641b956d0c4b848c7ec
%global toolchain clang
export CI_CLANG_RPM_CFLAGS="%{build_cflags} -fno-strict-aliasing"
export CI_CLANG_RPM_CXXFLAGS="%{build_cxxflags} -fno-strict-aliasing"
export CI_CLANG_RPM_LDFLAGS="%{build_ldflags}"
%global toolchain gcc
export CI_GCC_RPM_CFLAGS="%{build_cflags} -fno-strict-aliasing"
export CI_GCC_RPM_CXXFLAGS="%{build_cxxflags} -fno-strict-aliasing"
export CI_GCC_RPM_LDFLAGS="%{build_ldflags}"

# Run tests.
/bin/time -f '=> [%E]' ./ci.sh

%files devel
%license COPYING
%doc README.md
%{_includedir}/%{name}

%changelog
%autochangelog
