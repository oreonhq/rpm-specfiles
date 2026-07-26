%global source0_hash 4df5a5d1ce8346dd1f92c0f0bc38ac7383a1b2dd8977fa9e708340e72e027a88

Name:           perl-MooseX-Types-NetAddr-IP
Version:        0.07
Release:        25%{?dist}
Summary:        NetAddr::IP related types and coercions for Moose
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Types-NetAddr-IP
Source0:        https://cpan.metacpan.org/authors/id/T/TC/TCAINE/MooseX-Types-NetAddr-IP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Module::Runtime) >= 0.014
BuildRequires:  perl(Moose) >= 0.41
BuildRequires:  perl(MooseX::Types) >= 0.19
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(namespace::clean) >= 0.08
BuildRequires:  perl(NetAddr::IP)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(warnings)

%description
This package provides internet address types for Moose.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n MooseX-Types-NetAddr-IP-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
