%global source0_hash 95e0fc3ce6c2c5f7fd51ac6466e2758ce83b52fe8b93807f4d45117fa7f1e366

Name: 		perl-Test-Inline
Version: 	2.214
Release: 	16%{?dist}
Summary: 	Test::Inline Perl module
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Test-Inline
Source0: 	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Inline-%{version}.tar.gz

BuildArch: 	noarch

BuildRequires:	%{__perl}
BuildRequires:	%{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

BuildRequires:	perl(Algorithm::Dependency) >= 1.02
BuildRequires:	perl(Class::Autouse) >= 1.29
BuildRequires:	perl(Config::Tiny) >= 2.00
BuildRequires:	perl(File::chmod) >= 0.31
BuildRequires:	perl(File::Find::Rule) >= 0.26
BuildRequires:	perl(File::Flat) >= 1.00
BuildRequires:	perl(File::Remove) >= 0.37
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Getopt::Long) >= 2.34
BuildRequires:	perl(List::Util) >= 1.19
BuildRequires:	perl(Params::Util) >= 0.21
BuildRequires:	perl(Test::ClassAPI) >= 1.02
BuildRequires:	perl(Test::More) >= 0.42
BuildRequires:	perl(Test::Script)

# For improved tests
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::CPAN::Meta) >= 0.12
BuildRequires:  perl(Perl::MinimumVersion) >= 1.20

# Required by t/00-report-prereqs.t
BuildRequires:	perl(Encode) >= 3.08
BuildRequires:	perl(File::Temp) >= 0.2311
BuildRequires:	perl(JSON::PP) >= 4.06
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(YAML)
BuildRequires:	perl(autodie)

# RPM misses these deps
Requires:	perl(File::Flat)
Requires:	perl(File::Find::Rule)

# Filter duplicate unversioned requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(List::Util\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Params::Util\\)$

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

%check
%{__make} test AUTOMATED_TESTING=1

%files
%doc Changes
%license LICENSE
%{_bindir}/*
%{perl_vendorlib}/Test
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
