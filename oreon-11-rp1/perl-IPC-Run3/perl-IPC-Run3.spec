Name:           perl-IPC-Run3
Version:        0.049
Release:        5%{?dist}
Summary:        Run a subprocess in batch mode
License:        GPL-1.0-or-later OR Artistic-1.0-Perl OR BSD-2-Clause
URL:            https://metacpan.org/release/IPC-Run3
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/IPC-Run3-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More) >= 0.31
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)

# For improved tests
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod)

# RHBZ #1062267 / https://rt.cpan.org/Public/Bug/Display.html?id=52317
# Patch against IPC-Run3-0.048 from
# https://github.com/rschupp/IPC-Run3/commit/8ebe48760cfdc78fbf4fc46413dde9470121b99e
# FIXME: For now, keep the patch, but do not apply it.
# Upstream considers the issue to be a known implementation limitation.
Patch0:         0001-test-and-fix-for-RT-52317-Calling-run3-garbles-STDIN.patch
# oreon url source checksums begin
%global source0_sha256 9d048ae7b9ae63871bae976ba01e081d887392d904e5d48b04e22d35ed22011a
%global source0_file IPC-Run3-0.049.tar.gz
# oreon url source checksums end

%description
This module allows you to run a subprocess and redirect stdin, stdout,
and/or stderr to files and perl data structures. It aims to satisfy 99% of
the need for using system, qx, and open3 with a simple, extremely Perlish
API and none of the bloat and rarely used features of IPC::Run.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/IPC-Run3-0.049.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9d048ae7b9ae63871bae976ba01e081d887392d904e5d48b04e22d35ed22011a" || { echo "oreon: Source0 SHA256 mismatch for IPC-Run3-0.049.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n IPC-Run3-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test RELEASE_TESTING=1

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.049-5
- Prepare for Oreon 11 (RP1)
