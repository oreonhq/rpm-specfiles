%global source0_hash 33951831af236c1ed3fa8eb037fdafb1b42f38b3c01fb3ce852b964cd200b619

Name:           perl-Config-ZOMG
Version:        1.000000
Release:        27%{?dist}
Summary:        Catalyst::Plugin::ConfigLoader-style layer over Config::Any
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-ZOMG
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/Config-ZOMG-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Clone not used at tests
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Sub::Quote)
# Tests:
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
# Test::Pod 1.41 not used
BuildRequires:  perl(Test::Warn)
# Optional tests:
BuildRequires:  perl(Config::General)
Requires:       perl(Clone)

%description
Config::ZOMG is a fork of Config::JFDI. It removes a couple of unusual
features and passes the same tests three times faster than Config::JFDI.

Config::ZOMG is an implementation of Catalyst::Plugin::ConfigLoader. It will
scan a directory for files matching a certain name. If such a file is found
which also matches an extension that Config::Any can read, then the
configuration from that file will be loaded.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-ZOMG-%{version}

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
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
