%global source0_hash 6d87bcdfa63b28cefcfa870803a519b6590e3ea19c300f98cecb0e190bb19305

Name: 		perl-prefork
Version: 	1.05
Release: 	22%{?dist}
Summary: 	Optimized module loading for forking or non-forking processes
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/prefork
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/prefork-1.05.tar.gz

BuildArch: noarch

BuildRequires: %{__perl}
BuildRequires: %{__make}

BuildRequires: perl-generators
BuildRequires: perl(Carp)  
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(List::Util) >= 0.18
BuildRequires: perl(Scalar::Util) >= 1.18
BuildRequires: perl(strict)  
BuildRequires: perl(vars)  

# Required by tests
BuildRequires: perl(Test::Pod) >= 1.00
BuildRequires: perl(Test::MinimumVersion) >= 0.007
BuildRequires: perl(Perl::MinimumVersion) >= 1.20
BuildRequires: perl(Test::CPAN::Meta) >= 0.12

%description
Optimized module loading for forking or non-forking processes

prefork.pm is intended to serve as a central and optional marshalling
point for state detection (are we running in compile-time or run-time
mode) and to act as a relatively light-weight module loader.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n prefork-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test AUTOMATED_TESTING=1

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/prefork*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.05-22
- Prepare for Oreon 11 (RP1)
