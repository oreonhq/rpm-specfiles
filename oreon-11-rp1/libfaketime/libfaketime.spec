%global source0_hash 8e56deeb805682b025107e095f1d94a6ea677472f05824cd475f5c5e6e1a5ddf
%define _lto_cflags %{nil}
Name:       libfaketime
Version:    0.9.13
Release:        1%{?dist}
Summary:        Manipulate system time per process for testing purposes
License:    GPL-3.0-only AND GPL-2.0-only AND BSD-1-Clause
SourceLicense:  %{license} AND GPL-2.0-or-later AND BSD-2-Clause
URL:        https://github.com/wolfcw/libfaketime
Source0:        https://github.com/wolfcw/libfaketime/archive/refs/tags/v0.9.13.tar.gz#/libfaketime-0.9.13.tar.gz
Patch1:     libfaketime-0.9.12-Dynamic-libraries-are-expected-to-be-executable-on-F.patch
Provides:   faketime = %{version}-%{release}
# oreon:deps
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl-interpreter
BuildRequires:  procps-ng
# /oreon:deps
%description
libfaketime intercepts various system calls that programs use to retrieve the
current date and time. It then reports modified (faked) dates and times (as
specified by you, the user) to these programs. This means you can modify the
system time a program sees without having to change the time system-wide.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%ifarch ppc64le
  export FAKETIME_COMPILE_CFLAGS="-DFORCE_PTHREAD_NONVER"
%endif
%ifarch riscv64
  export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX -DFORCE_PTHREAD_NONVER"
%endif
%set_build_flags
%make_build PREFIX=%{_prefix} LIBDIRNAME=/%{_lib} all
%check

%ifarch ppc64le
  export FAKETIME_COMPILE_CFLAGS="-DFORCE_PTHREAD_NONVER"
%endif
%ifarch riscv64
  export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX -DFORCE_PTHREAD_NONVER"
%endif
make PREFIX=%{_prefix} LIBDIRNAME=/%{_lib} -C test
%install
%make_install PREFIX=%{_prefix} LIBDIRNAME=/%{_lib}
rm -fr %{buildroot}/%{_docdir}/faketime
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.12-1
- Prepare for Oreon 11 (RP1)
