%global source0_hash f5eaccc9d2977c83308651be9379f09f34348398f419e8f8b5bbd95928c777ed

%global libjit_soversion 3
Name:           jitterentropy
Version:        3.7.0
Release:        1%{?dist}
Summary:        Library implementing the jitter entropy source

License:        BSD-3-Clause OR GPL-2.0-only
URL:            https://github.com/smuellerDD/jitterentropy-library
Source0:        %{url}/archive/v%{version}/%{name}-library-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

# Disable Upstream Makefiles debuginfo strip on install
Patch0: jitterentropy-rh-makefile.patch
# Gcc with -std=c11 defines __powerpc__ only
Patch1: jitterentropy-powerpc.patch
# Restore previous jitterentropy public api
Patch2: jitterentropy-api.patch
# _DEFAULT_SOURCE is needed for clock_gettime() on riscv64
# TODO drop when the next upstream release is imported
Patch3: jitterentropy-riscv64.patch

%description
Library implementing the CPU jitter entropy source

%package devel
Summary: Development headers for jitterentropy library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and libraries for jitterentropy

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p0 -n %{name}-library-%{version}

%build
%set_build_flags
%make_build

%install
mkdir -p %{buildroot}%{_includedir}
%make_install PREFIX=%{_prefix} LIBDIR=%{_lib}

%files
%doc README.md CHANGES.md
%license LICENSE LICENSE.bsd LICENSE.gplv2
%{_libdir}/libjitterentropy.so.%{libjit_soversion}*

%files devel
%{_includedir}/*
%{_libdir}/libjitterentropy.so
%{_mandir}/man3/*

%changelog
%autochangelog
