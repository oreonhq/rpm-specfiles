%global source0_hash 33951831af236c1ed3fa8eb037fdafb1b42f38b3c01fb3ce852b964cd200b619
Name:           perl-Config-ZOMG
Version:        1.000000
Release:        1%{?dist}
Summary:        Catalyst::Plugin::ConfigLoader-style layer over Config::Any
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-ZOMG
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/Config-ZOMG-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Clone)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(Config::General)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
