%global source0_hash 92401da4cf484eb7188ec196b68186efa782a102b451ea156cd8b8772e687055

Name:       perl-Moose-Autobox 
Version:    0.16
Release:    29%{?dist}
# lib/Moose/Autobox.pm -> GPL+ or Artistic
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl 

Summary:    Autoboxed wrappers for native Perl datatypes 
Source:     https://cpan.metacpan.org/authors/id/E/ET/ETHER/Moose-Autobox-%{version}.tar.gz
Url:        https://metacpan.org/release/Moose-Autobox
BuildArch:  noarch

BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(autobox) >= 2.23
BuildRequires: perl(Carp)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(File::Spec)
BuildRequires: perl(List::MoreUtils) >= 0.07
BuildRequires: perl(metaclass)
BuildRequires: perl(Module::Metadata)
BuildRequires: perl(Moose) >= 0.42
BuildRequires: perl(Moose::Role)
BuildRequires: perl(Moose::Util)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(parent)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(strict)
BuildRequires: perl(Syntax::Keyword::Junction::All)
BuildRequires: perl(Syntax::Keyword::Junction::Any)
BuildRequires: perl(Syntax::Keyword::Junction::None)
BuildRequires: perl(Syntax::Keyword::Junction::One)
BuildRequires: perl(Test::Exception) >= 0.21
BuildRequires: perl(Test::More) >= 0.89
BuildRequires: perl(warnings)

%{?perl_default_filter}

Provides:       perl(Moose::Autobox)
%description
Moose::Autobox provides an implementation of SCALAR, ARRAY, HASH & CODE
for use with autobox. 


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Moose-Autobox-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README examples/ 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
