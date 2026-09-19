%global source0_hash 5fb3c535906cff5064ce29307f96166ec02819818983dd72c6ea991943cd928d

Name:           perl-Data-Validate-Type
Version:        1.6.0
Release:        28%{?dist}
Summary:        Public interface to Params::Util offering data type validation functions
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Validate-Type
Source0:        https://cpan.metacpan.org/authors/id/A/AU/AUBERTG/Data-Validate-Type-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This module presents an alternative API to Params::Util which fixes a number
of drawbacks (function names start with an underscore, are uppercase and don't
pass PerlCritic validation).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Validate-Type-v%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
