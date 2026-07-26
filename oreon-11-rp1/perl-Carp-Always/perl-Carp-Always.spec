%global source0_hash 98aa11492171c016fb0827581ab1fa5ed01b1e99c6357489ddf3a827315866f1

Name:           perl-Carp-Always
Version:        0.16
Release:        23%{?dist}
Summary:        Warn and die in Perl noisily with stack backtraces
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Carp-Always
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Carp-Always-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
# glibc-common for the iconv tool
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::More)
# Optional tests
# Test::Pod not used
# Test::Pod::Coverage not used
Requires:       perl(Carp)
Requires:       perl(if)

%{?perl_default_filter}

%description
This module is meant as a debugging aid. It can be used to make a script
complain loudly with stack backtraces when warn()ing or die()ing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Carp-Always-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

# Recode
iconv -f iso8859-1 -t utf8 README >README.utf8
touch -r README README.utf8
mv README.utf8 README

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
