%global source0_hash 52bd43f555913cc2ffd6405f9951d2aabd46af63d701d9b5e346a6332709f0ce

%global cpan_version 0.52
Name:           perl-App-CLI
Version:        0.520
Release:        16%{?dist}
Summary:        Dispatcher module for command line interface programs
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/App-CLI
Source0:        https://cpan.metacpan.org/authors/id/P/PT/PTC/App-CLI-%{cpan_version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76

# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Getopt::Long) >= 2.35
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Pod::Simple::Text)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)

Requires:       perl(Pod::Simple::Text)

%{?perl_default_filter}

%description
App::CLI dispatches CLI (command line interface) based commands into
command classes. It also supports sub-command and per-command options.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-CLI-%{cpan_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/App*
%{_mandir}/man3/App*

%changelog
%autochangelog
