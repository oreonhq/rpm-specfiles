%global source0_hash 5c9509f1a8693d8287fa013def0bf87aa64cd927138461ef8deb55503c6651c2

Name:           perl-IO-Stty
Version:        0.04
Release:        18%{?dist}
Summary:        Change and print terminal line settings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Stty
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/IO-Stty-%{version}.tar.gz
BuildArch:      noarch
Patch0:         IO-Stty-0.04-Packed-script-into-rpm.patch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(POSIX)
# Tests
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This is the Perl POSIX compliant stty.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Stty-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
