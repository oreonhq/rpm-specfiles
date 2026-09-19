%global source0_hash 38f0169a34679df2d59fe2e23c02036404b4515cf5591c5a5cba9c031b7fafa7

Name:           perl-MooseX-CascadeClearing
Version:        0.05
Release:        36%{?dist}
Summary:        Cascade clearer actions across attributes
License:        LGPL-2.1-only
URL:            https://metacpan.org/release/MooseX-CascadeClearing
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/MooseX-CascadeClearing-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(namespace::autoclean)
# Tests
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88

%description
MooseX::CascadeClearing does the necessary meta class fiddling to allow an
clearing one attribute to be cascaded through to other attributes as well,
calling their clear accessors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-CascadeClearing-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
