# TODO: BR: perl(B::C) when available
# Run optional test
%bcond_without perl_Sub_Name_enables_optional_test

Name:		perl-Sub-Name
Version:	0.28
Release:	5%{?dist}
Summary:	Name - or rename - a sub
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Sub-Name
Source0:	https://www.cpan.org/modules/by-module/Sub/Sub-Name-%{version}.tar.gz
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(B)
BuildRequires:	perl(B::Deparse)
BuildRequires:	perl(Carp)
BuildRequires:	perl(feature)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(if)
BuildRequires:	perl(Test::More)
%if %{with perl_Sub_Name_enables_optional_test}
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(Devel::CheckBin)
%endif
# Dependencies
# (none)

# Don't "provide" private perl objects
%{?perl_default_filter}

%description
This module allows one to "name" or rename subroutines, including anonymous
ones.

Note that this is mainly for aid in debugging; you still cannot call the sub
by the new name (without some deep magic).

%prep
%setup -q -n Sub-Name-%{version}

%build
perl Makefile.PL \
	INSTALLDIRS=vendor \
	NO_PACKLIST=1 \
	NO_PERLLOCAL=1 \
	optimize="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorarch}/auto/Sub/
%{perl_vendorarch}/Sub/
%{_mandir}/man3/Sub::Name.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.28-5
- Prepare for Oreon 11 (RP1)
