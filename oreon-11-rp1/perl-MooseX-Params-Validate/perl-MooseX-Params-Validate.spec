%global source0_hash 88295446aba999cbb8f998d7fb9a2701d6617394a51d6d724c774e6d9ff139d9

Name:           perl-MooseX-Params-Validate
Summary:        Extension of Params::Validate using Moose's types
Version:        0.21
Release:        33%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/MooseX-Params-Validate-%{version}.tar.gz 
URL:            https://metacpan.org/release/MooseX-Params-Validate
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::Caller)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.75
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Moose) >= 2.1200
BuildRequires:  perl(Moose::Meta::TypeConstraint::Role)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::Validate) >= 1.15
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This module fills a gap in Moose by adding method parameter validation to
Moose. This is just one of many developing options, it should be considered
the "official" one by any means though.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Params-Validate-%{version}

# silence rpmlint warning
sed -i -e '1s,#!.*perl,#!%{__perl},' t/*.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README.md t
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
