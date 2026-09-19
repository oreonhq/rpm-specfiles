%global source0_hash abf61efecc90bee85711c3626f5ec51a8d314cc91d13eeba03e1617c8fe809d7

Name:           perl-POE-Filter-IRCD
Version:        2.44
Release:        36%{?dist}
Summary:        A POE-based parser for the IRC protocol
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Filter-IRCD
Source0: https://cpan.metacpan.org/authors/id/B/BI/BINGOS/POE-Filter-IRCD-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(POE::Filter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(POE::Filter)

%description
POE::Filter::IRCD provides a convenient way of parsing and creating IRC
protocol lines.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Filter-IRCD-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
