%global source0_hash 95e0fc3ce6c2c5f7fd51ac6466e2758ce83b52fe8b93807f4d45117fa7f1e366
Name: 		perl-Test-Inline
Version: 	2.214
Release:        16%{?dist}
Summary:        Test::Inline Perl module
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Test-Inline
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Inline-%{version}.tar.gz
BuildArch: 	noarch
Requires:	perl(File::Flat)
Requires:	perl(File::Find::Rule)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(List::Util\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Params::Util\\)$
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/perl
BuildRequires:  perl(Algorithm::Dependency)
BuildRequires:  perl(Class::Autouse)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Flat)
BuildRequires:  perl(File::Remove)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::chmod)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Perl::MinimumVersion)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::ClassAPI)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(YAML)
BuildRequires:  perl(autodie)
BuildRequires:  perl-generators
# /oreon:deps
%description
Test::Inline allows you to inline your tests next to the code being tested.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Inline-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test AUTOMATED_TESTING=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
