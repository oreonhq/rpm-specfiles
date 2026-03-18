Name:           perl-Class-Accessor
Version:        0.51
Release:        24%{?dist}
Summary:        Automated accessor generation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Accessor
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KASEI/Class-Accessor-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Name)
# Test Suite
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Hash)
# Dependencies
# (none)

%description
This module automagically generates accessors/mutators for your class.

%prep
%setup -q -n Class-Accessor-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make  %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes examples/ README
%{perl_vendorlib}/Class/
%{_mandir}/man3/Class::Accessor.3*
%{_mandir}/man3/Class::Accessor::Fast.3*
%{_mandir}/man3/Class::Accessor::Faster.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.51-24
- Prepare for Oreon 11 (RP1)
