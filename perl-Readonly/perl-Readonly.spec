Name:		perl-Readonly
Version:	2.05
Release:	30%{?dist}
Summary:	Facility for creating read-only scalars, arrays, hashes
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Readonly
Source0:	https://cpan.metacpan.org/authors/id/S/SA/SANKO/Readonly-%{version}.tar.gz
Patch0:		Readonly-2.05-interpreter.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build::Tiny) >= 0.035
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Storable)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(warnings)
# Runtime
Requires:	perl(Carp)
Requires:	perl(Storable)

%description
Readonly provides a facility for creating non-modifiable scalars,
arrays, and hashes. Any attempt to modify a Readonly variable throws
an exception.

Readonly:
* Creates scalars, arrays (not lists), and hashes
* Creates variables that look and work like native perl variables
* Creates global or lexical variables
* Works at run-time or compile-time
* Works with deep or shallow data structures
* Prevents reassignment of Readonly variables

%prep
%setup -q -n Readonly-%{version}

# Fix script interpreter for test suite since we're packaging it
%patch -P0

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%check
./Build test

%files
%license LICENSE
%doc Changes README.md eg/benchmark.pl t/
%{perl_vendorlib}/Readonly.pm
%{_mandir}/man3/Readonly.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.05-30
- Prepare for Oreon 11 (RP1)
