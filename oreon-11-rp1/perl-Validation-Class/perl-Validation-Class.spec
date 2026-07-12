%global source0_hash 6ff2a6a0ce187aca0b91d87e235a148e50e6e69310e7630607e72f437b1959d9

Name:           perl-Validation-Class
Version:        7.900059
Release:        9%{?dist}
Summary:        Powerful Data Validation Framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Validation-Class
Source0:        https://cpan.metacpan.org/authors/id/C/CK/CKRAS/Validation-Class-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 4:5.10.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Hash::Flatten)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(Class::Method::Modifiers)
# Dependencies
# (none)

Provides:       perl(Validation::Class)
Provides:       perl(Validation::Class::Simple)
%description
Validation::Class is a scalable data validation library with interfaces for
applications of all sizes. The most common usage of Validation::Class is to
transform class namespaces into data validation domains where consistency
and reuse are primary concerns. Validation::Class provides an extensible
framework for defining reusable data validation rules. It ships with a
complete set of pre-defined validations and filters referred to as
"directives".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Validation-Class-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Validation/
%{_mandir}/man3/Validation::Class.3*
%{_mandir}/man3/Validation::Class::Cookbook.3*
%{_mandir}/man3/Validation::Class::Directive.3*
%{_mandir}/man3/Validation::Class::Directive::*.3*
%{_mandir}/man3/Validation::Class::Directives.3*
%{_mandir}/man3/Validation::Class::Exporter.3*
%{_mandir}/man3/Validation::Class::Listing.3*
%{_mandir}/man3/Validation::Class::Mapping.3*
%{_mandir}/man3/Validation::Class::Prototype.3*
%{_mandir}/man3/Validation::Class::Simple.3*
%{_mandir}/man3/Validation::Class::Simple::Streamer.3*
%{_mandir}/man3/Validation::Class::Whitepaper.3*

%changelog
%autochangelog
