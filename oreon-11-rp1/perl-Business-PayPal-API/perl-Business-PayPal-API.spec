%global source0_hash 4e1b229bd1440aeb10e2107bf5730d0c9264227023e325bd39f3ad9ddfbbc19d

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(SOAP::Lite\\)$
Name:           perl-Business-PayPal-API
Version:        0.77
Release:        24%{?dist}
Summary:        PayPal API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Business-PayPal-API
Source0:        https://cpan.metacpan.org/modules/by-module/Business/Business-PayPal-API-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(autodie)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Printer)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(SOAP::Lite) >= 0.67
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(warnings)

%description
Business::PayPal::API supports both certificate authentication and the new
3-token "Signature" authentication.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Business-PayPal-API-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc auth.sample.3token auth.sample.cert Changes README.md eg
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
