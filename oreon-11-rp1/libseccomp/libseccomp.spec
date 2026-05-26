Name:           libseccomp
Version:        2.6.0
Release:        3%{?dist}
Summary:        Enhanced seccomp library
License:        LGPL-2.1-only
URL:            https://github.com/seccomp/libseccomp
Source0:        https://github.com/seccomp/libseccomp/releases/download/v2.6.0/libseccomp-2.6.0.tar.gz

# Backports from upstream

# From https://github.com/seccomp/libseccomp/pull/459
Patch0101:      fix-murmur-hash-strict-aliasing-violation.patch
# https://github.com/seccomp/libseccomp/pull/452
Patch0102: remove-fuzzer-test-from-62-sim-arch_transactions.patch
# oreon url source checksums begin
%global source0_sha256 83b6085232d1588c379dc9b9cae47bb37407cf262e6e74993c61ba72d2a784dc
%global source0_file libseccomp-2.6.0.tar.gz
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires:  gperf
BuildRequires:  make

%ifnarch riscv64 s390
# Versions prior to 3.13.0-4 do not work on ARM with newer glibc 2.25.0-6
# See https://bugzilla.redhat.com/show_bug.cgi?id=1466017
BuildRequires:  valgrind >= 1:3.13.0-4
%endif

%description
The libseccomp library provides an easy to use interface to the Linux Kernel's
syscall filtering mechanism, seccomp.  The libseccomp API allows an application
to specify which syscalls, and optionally which syscall arguments, the
application is allowed to execute, all of which are enforced by the Linux
Kernel.

%package devel
Summary:        Development files used to build applications with libseccomp support
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The libseccomp library provides an easy to use interface to the Linux Kernel's
syscall filtering mechanism, seccomp.  The libseccomp API allows an application
to specify which syscalls, and optionally which syscall arguments, the
application is allowed to execute, all of which are enforced by the Linux
Kernel.

%package static
Summary:        Enhanced seccomp static library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The libseccomp library provides an easy to use interface to the Linux Kernel's
syscall filtering mechanism, seccomp.  The libseccomp API allows an application
to specify which syscalls, and optionally which syscall arguments, the
application is allowed to execute, all of which are enforced by the Linux
Kernel.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libseccomp-2.6.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "83b6085232d1588c379dc9b9cae47bb37407cf262e6e74993c61ba72d2a784dc" || { echo "oreon: Source0 SHA256 mismatch for libseccomp-2.6.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
%configure
%make_build

%install
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_includedir}
mkdir -p %{buildroot}/%{_mandir}

%make_install

rm -f %{buildroot}/%{_libdir}/libseccomp.la

%check
%make_build check


%files
%license LICENSE
%doc CREDITS README.md CHANGELOG CONTRIBUTING.md
%{_libdir}/libseccomp.so.*

%files devel
%{_includedir}/seccomp.h
%{_includedir}/seccomp-syscalls.h
%{_libdir}/libseccomp.so
%{_libdir}/pkgconfig/libseccomp.pc
%{_bindir}/scmp_sys_resolver
%{_mandir}/man1/*
%{_mandir}/man3/*

%files static
%{_libdir}/libseccomp.a

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6.0-3
- Prepare for Oreon 11 (RP1)
