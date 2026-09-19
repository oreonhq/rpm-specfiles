%global source0_hash 44a40b312a19dda6edf8eb33656c078a7e73f5fedf51d16c06a438383d885988

%global _cmake_generator "Unix Makefiles"

Name: openssl-gost-engine
Version: 3.0.3
Release: 11%{?dist}

URL: https://github.com/gost-engine/engine
License: Apache-2.0
Summary: A reference implementation of the Russian GOST crypto algorithms for OpenSSL

Source: https://github.com/gost-engine/engine/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1: libprov-cmake.patch

BuildRequires: make
BuildRequires: cmake-rpm-macros
BuildRequires: gcc
BuildRequires: perl-Test-Simple
BuildRequires: cmake
BuildRequires: openssl-devel
BuildRequires: openssl-devel-engine
BuildRequires: pkgconf-pkg-config

%{?!_without_check:%{?!_disable_check:BuildRequires: perl-devel openssl}}

%description
A reference implementation of the Russian GOST crypto algorithms for OpenSSL.

%package -n gostsum
Summary: GOST file digesting utilities
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n gostsum
GOST file digesting utilities.

%global _enginesdir %(pkg-config --variable=enginesdir libcrypto)
%global _providersdir %(pkg-config --variable=modulesdir libcrypto)
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n engine-%version -p1

%build
%cmake -B "%{_vpath_builddir}"

%make_build -C "%{_vpath_builddir}"

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_mandir/man1
mkdir -p %buildroot%_enginesdir
mkdir -p %buildroot%_providersdir
cp "%{_vpath_builddir}"/bin/gost.so README.gost %buildroot%_enginesdir/
cp "%{_vpath_builddir}"/bin/gostprov.so %buildroot%_providersdir/
cp "%{_vpath_builddir}"/bin/gost*sum %buildroot%_bindir/
cp gost*sum.1 %buildroot%_mandir/man1/

%check
echo "ALL" > "$PWD/openssl-crypto-policy.override"
OPENSSL_ENGINES="$PWD/%{_vpath_builddir}/bin" \
	OPENSSL_SYSTEM_CIPHERS_OVERRIDE="$PWD/openssl-crypto-policy.override" \
	LD_LIBRARY_PATH="$PWD/%{_vpath_builddir}/bin" \
	CTEST_OUTPUT_ON_FAILURE=1 \
	make -C "%{_vpath_builddir}" test ARGS="--verbose"

%files
%_enginesdir/gost.so
%_providersdir/gostprov.so
%doc %_enginesdir/README.gost

%files -n gostsum
%_bindir/gost*sum*
%_mandir/man1/gost*sum*

%changelog
%autochangelog
