%global source0_hash 7094ea5c91f536d263b85e83ab4e9a963e11c4408ce08ecae553fa9c0cc47e73
Name:           perl-HTTP-CookieJar
Version:        0.014
Release:        1%{?dist}
Summary:        Minimalist HTTP user agent cookie jar
License:        Apache-2.0
URL:            https://metacpan.org/release/HTTP-CookieJar
Source0:        https://cpan.metacpan.org/modules/by-module/HTTP/HTTP-CookieJar-%{version}.tar.gz
BuildArch:      noarch
Recommends:     perl(Mozilla::PublicSuffix)
Provides:       perl(HTTP::CookieJar::LWP)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Mozilla::PublicSuffix)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements a minimalist HTTP user agent cookie jar in
conformance with RFC 6265.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir HTTP-CookieJar-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.014-10
- Prepare for Oreon 11 (RP1)
