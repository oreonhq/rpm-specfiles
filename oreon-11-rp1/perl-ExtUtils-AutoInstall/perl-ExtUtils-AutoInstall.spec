%global source0_hash 0fe48f78b5ee39acb3be38a7a039789abc46195af411297dabec294c2851027f

Name: 		perl-ExtUtils-AutoInstall
Version: 	0.64
Release: 	29%{?dist}
Summary: 	Automatic install of dependencies via CPAN
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/ExtUtils-AutoInstall
Source:		https://cpan.metacpan.org/authors/id/I/IN/INGY/ExtUtils-AutoInstall-%{version}.tar.gz
Patch0:		eai.patch

BuildArch: 	noarch

BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	perl-generators
BuildRequires:	perl(Carp)
BuildRequires:	perl(Config)
BuildRequires:	perl(CPAN)
BuildRequires:	perl(CPANPLUS) >= 0.043
BuildRequires:	perl(Cwd)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(lib)
BuildRequires:	perl(LWP::Simple)
BuildRequires:	perl(Sort::Versions) >= 1.2
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Test)
BuildRequires:	perl(vars)
BuildRequires:	perl(version)

BuildRequires:  perl(inc::Module::Install)

%description
ExtUtils::AutoInstall lets module writers specify a more sophisticated
form of dependency information than the PREREQ_PM option offered by 
ExtUtils::MakeMaker.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ExtUtils-AutoInstall-%{version}
%patch -P0 -p1
rm -r inc/

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --defaultdeps NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
# For license text(s), see the perl package
%doc Changes AUTHORS README TODO
%{perl_vendorlib}/ExtUtils
%{_mandir}/man3/*

%changelog
%autochangelog
