%global source0_hash b194290f257cc6275a039374111554c666a1650e4c01ad799c1e0a277f47917d

Name:           perl-Data-Visitor
Version:        0.32
Release:        8%{?dist}
Summary:        Visitor style traversal of Perl data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Visitor
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Visitor-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Moose) >= 0.89
BuildRequires:  perl(namespace::clean) >= 0.19
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Tie::ToObject) >= 0.01
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Tie::RefHash)
# Optional Tests
BuildRequires:  perl(CPAN::Meta) > 2.120900
BuildRequires:  perl(CPAN::Meta::Prereqs)
# Dependencies
# (none)

Provides:       perl(Data::Visitor)
Provides:       perl(Data::Visitor)
%description
This module is a simple visitor implementation for Perl values.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Data-Visitor-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENCE
%doc Changes CONTRIBUTING README t/
%{perl_vendorlib}/Data/
%{_mandir}/man3/Data::Visitor.3*
%{_mandir}/man3/Data::Visitor::Callback.3*

%changelog
%autochangelog
