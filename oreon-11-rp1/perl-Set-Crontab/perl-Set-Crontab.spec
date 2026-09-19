%global source0_hash 47e294e88d2d139e2d06dfa544b91a3cc5656a3a6dd15594dc764759fbaa86da

# Filter the Perl extension module
%{?perl_default_filter}

Name:           perl-Set-Crontab
Version:        1.03
Release:        40%{?dist}
Summary:        Expand crontab(5)-style integer lists
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Set-Crontab
Source0:        https://cpan.metacpan.org/modules/by-module/Set/Set-Crontab-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test)

%description
Set::Crontab parses crontab-style lists of integers and defines some
utility functions to make it easier to deal with them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Set-Crontab-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
