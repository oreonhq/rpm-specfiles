Name: 		perl-File-Find-Rule
Version: 	0.35
Release: 	3%{?dist}
Summary: 	Perl module implementing an alternative interface to File::Find
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/File-Find-Rule
Source0: 	https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/File-Find-Rule-%{version}.tar.gz

BuildArch: 	noarch

BuildRequires:	%{__make}
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires: 	perl(lib)
BuildRequires: 	perl(Number::Compare)
BuildRequires: 	perl(strict)
BuildRequires:  perl(Test::More) >= 0.07
BuildRequires: 	perl(Text::Glob)
BuildRequires: 	perl(vars)
BuildRequires: 	perl(warnings)
# Optional tests
BuildRequires: 	perl(Test::Differences)


%description
File::Find::Rule is a friendlier interface to File::Find.  It allows
you to build rules which specify the desired files and directories.

%prep
%setup -q -n File-Find-Rule-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%{_bindir}/findrule
%{_mandir}/man1/findrule*
%{perl_vendorlib}/File
%{_mandir}/man3/File::Find::Rule*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.35-3
- Prepare for Oreon 11 (RP1)
