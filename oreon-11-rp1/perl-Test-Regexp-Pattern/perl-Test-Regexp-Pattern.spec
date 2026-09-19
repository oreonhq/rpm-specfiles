%global source0_hash a432a015938c10b4bbcb802f9fbc60121d43c92ac3cea8c1dc9006e28be29586

Name:           perl-Test-Regexp-Pattern
Version:        0.010
Release:        9%{?dist}
Summary:        Test Regexp::Pattern patterns
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Test-Regexp-Pattern
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Test-Regexp-Pattern-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(blib)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long) >= 2.50
BuildRequires:  perl(Hash::DefHash) >= 0.06
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Regexp::Pattern) >= 0.2.7
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
This module performs various checks on a module's Regexp::Pattern patterns.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Test-Regexp-Pattern-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{_bindir}/test-regexp-pattern
%{perl_vendorlib}/*
%{_mandir}/man1/test-regexp-pattern.1*
%{_mandir}/man3/Test::Regexp::Pattern*.*

%changelog
%autochangelog
