%global source0_hash 287028adb3b651841008620c6138c46a8fbd813fa9f70127efad00a2993457d6

Name:           perl-App-Rad
Version:        1.05
Release:        29%{?dist}
Summary:        Rapid creation of command line applications
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/App-Rad
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GARU/App-Rad-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(Attribute::Handlers)
# B::Deparse used as "perl -MO=Deparse"
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Getopt::Long) >= 2.36
# O used as "perl -MO=Deparse"
BuildRequires:  perl(O)
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(File::Temp)
# perl executed used as "perl -MO=Deparse"
Requires:       perl-interpreter
# B::Deparse used as "perl -MO=Deparse"
Requires:       perl(B::Deparse)
# O used as "perl -MO=Deparse"
Requires:       perl(O)
Requires:       perl(Getopt::Long) >= 2.36

%description
App::Rad aims to be a simple yet powerful framework for developing your
command-line applications. It can easily transform your Perl one-liners
into reusable subroutines than can be called directly by the user of
your program. It also tries to provide a handy interface for your common
command-line tasks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-Rad-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
