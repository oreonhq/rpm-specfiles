%global source0_hash 71f6d5fd9f358611d1457c0c6b3fbe18224a4133e395e58d2a5ae4232f2761a5

Name:           perl-Catalyst-Action-RenderView
Summary:        Sensible default end action for view rendering
Version:        0.17
Release:        4%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Action-RenderView-%{version}.tar.gz 
URL:            https://metacpan.org/release/Catalyst-Action-RenderView
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Action)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Runtime) >= 5.80030
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(Catalyst::View)
BuildRequires:  perl(Data::Visitor) >= 0.24
BuildRequires:  perl(Data::Visitor::Callback)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Request::AsCGI)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)
BuildRequires:  sed

Requires:       perl(Catalyst::Action)
Requires:       perl(Catalyst::Runtime) >= 5.70
Requires:       perl(Data::Visitor) >= 0.24
Requires:       perl(MRO::Compat)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
This action implements a sensible default end action, which will forward to
the first available view, unless status is set to 3xx, or there is a
response body. It also allows you to pass dump_info=1 to the URL in order
to force a debug screen, while in debug mode.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Action-RenderView-%{version}

# correct line encoding and an errant interperter setting
find t/ -type f -exec perl -pi -e 's|^#!perl|#!/usr/bin/perl|; s/\r//' {} +

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
