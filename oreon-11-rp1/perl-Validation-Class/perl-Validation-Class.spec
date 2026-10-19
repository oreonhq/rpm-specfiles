%global source0_hash 6ff2a6a0ce187aca0b91d87e235a148e50e6e69310e7630607e72f437b1959d9
Name:           perl-Validation-Class
Version:        7.900059
Release:        1%{?dist}
Summary:        Powerful Data Validation Framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Validation-Class
Source0:        https://cpan.metacpan.org/authors/id/C/CK/CKRAS/Validation-Class-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Validation::Class)
Provides:       perl(Validation::Class::Simple)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Hash::Flatten)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
