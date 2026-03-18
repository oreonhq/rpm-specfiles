Name:		perl-parent
Epoch:		1
Version:	0.244
Release:	521%{?dist}
Summary:	Establish an ISA relationship with base classes at compile time
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/parent
Source0:	https://cpan.metacpan.org/authors/id/C/CO/CORION/parent-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(strict)
# Test Suite
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::More) >= 0.40
# Dependencies
# (none)

%description
Allows you to both load one or more modules, while setting up inheritance
from those modules at the same time. Mostly similar in effect to:

	package Baz;

	BEGIN {
		require Foo;
		require Bar;

		push @ISA, qw(Foo Bar);
	}

%prep
%setup -q -n parent-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes
%{perl_vendorlib}/parent.pm
%{_mandir}/man3/parent.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.244-521
- Prepare for Oreon 11 (RP1)
