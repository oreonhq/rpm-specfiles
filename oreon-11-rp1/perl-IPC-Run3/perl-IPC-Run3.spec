%global source0_hash 9d048ae7b9ae63871bae976ba01e081d887392d904e5d48b04e22d35ed22011a
Name:           perl-IPC-Run3
Version:        0.049
Release:        1%{?dist}
Summary:        Run a subprocess in batch mode
License:        GPL-1.0-or-later OR Artistic-1.0-Perl OR BSD-2-Clause
URL:            https://metacpan.org/release/IPC-Run3
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/IPC-Run3-%{version}.tar.gz
BuildArch:      noarch
Patch0:         0001-test-and-fix-for-RT-52317-Calling-run3-garbles-STDIN.patch
Provides:       perl(IPC::Run3)
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module allows you to run a subprocess and redirect stdin, stdout,
and/or stderr to files and perl data structures. It aims to satisfy 99% of
the need for using system, qx, and open3 with a simple, extremely Perlish
API and none of the bloat and rarely used features of IPC::Run.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n IPC-Run3-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test RELEASE_TESTING=1
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.049-5
- Prepare for Oreon 11 (RP1)
