%global source0_hash 243157504b97116b05f947ccc51d45198ee0a27bb0589d30afde4d759e71551f
%bcond_without perl_Business_Stripe_enables_optional_test
Name:           perl-Business-Stripe
Version:        0.07
Release:        1%{?dist}
Summary:        Interface for Stripe payment system
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Business-Stripe
Source0:        https://cpan.metacpan.org/modules/by-module/Business/Business-Stripe-%{version}.tar.gz
BuildArch:      noarch
%if !%{with perl_Business_Stripe_enables_optional_test}
%endif
%if %{with perl_Business_Stripe_enables_optional_test}
%endif
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package provides Perl bindings for Stripe payment system. Any API calls
that do not have bindings can be access through the generic api method.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Business-Stripe-%{version}
%if !%{with perl_Business_Stripe_enables_optional_test}
rm t/pod.t
perl -i -ne 'print $_ unless m{^t/pod.t}' MANIFEST
%endif

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
