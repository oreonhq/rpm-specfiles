Name:           perl-HTTP-CookieJar
Version:        0.014
Release:        10%{?dist}
Summary:        Minimalist HTTP user agent cookie jar
License:        Apache-2.0
URL:            https://metacpan.org/release/HTTP-CookieJar
Source0:        https://cpan.metacpan.org/modules/by-module/HTTP/HTTP-CookieJar-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(Mozilla::PublicSuffix)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
# Dependencies
Recommends:     perl(Mozilla::PublicSuffix)

%description
This module implements a minimalist HTTP user agent cookie jar in
conformance with RFC 6265.

%prep
%autosetup -p1 -n HTTP-CookieJar-%{version}

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
%doc Changes CONTRIBUTING.mkdn LICENSE README
%{perl_vendorlib}/HTTP/
%{_mandir}/man3/HTTP::CookieJar.3*
%{_mandir}/man3/HTTP::CookieJar::LWP.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.014-10
- Prepare for Oreon 11 (RP1)
