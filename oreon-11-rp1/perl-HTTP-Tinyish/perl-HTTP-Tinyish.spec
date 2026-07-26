%global source0_hash e9ce94a9913f9275d312ded4ddb34f76baf011b6b8d6029ff2871d5bd7bae468

Name:           perl-HTTP-Tinyish
Version:        0.19
Release:        6%{?dist}
Summary:        HTTP::Tiny compatible HTTP client wrappers
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Tinyish
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/HTTP-Tinyish-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Temp)
# BuildRequires:  perl(File::Which)
# BuildRequires:  perl(HTTP::Tiny) >= 0.054
# BuildRequires:  perl(IPC::Run3)
# BuildRequires:  perl(LWP) >= 5.802
# BuildRequires:  perl(LWP::Protocol::https)
# BuildRequires:  perl(LWP::UserAgent)
# BuildRequires:  perl(parent)
# Tests only
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(:HTTP-Tinyish:backend) = %{version}
Recommends:     perl(HTTP::Tinyish::LWP)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(HTTP::Tiny\\)$

%description
HTTP::Tinyish is a wrapper module for HTTP client modules LWP, HTTP::Tiny
and HTTP client software curl and wget.

%package        Curl
Summary:        HTTP::Tinyish curl backend
Requires:       curl
Provides:       perl(:HTTP-Tinyish:backend) = %{version}

%description Curl
%{summary}.

%package        HTTPTiny
Summary:        HTTP::Tinyish HTTP::Tiny backend
Requires:       perl(HTTP::Tiny) >= 0.054
Provides:       perl(:HTTP-Tinyish:backend) = %{version}

%description HTTPTiny
%{summary}.

%package        LWP
Summary:        HTTP::Tinyish LWP backend
Provides:       perl(:HTTP-Tinyish:backend) = %{version}
Recommends:     perl(LWP::Protocol::https)

%description LWP
%{summary}.

%package        Wget
Summary:        HTTP::Tinyish wget backend
Requires:       wget
Provides:       perl(:HTTP-Tinyish:backend) = %{version}

%description Wget
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Tinyish-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
# Nothing is really tested; this could be completely
# disabled to save us some builddeps but oh well.
%{make_build} test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/HTTP
%dir %{perl_vendorlib}/HTTP/Tinyish
%{perl_vendorlib}/HTTP/Tinyish.pm
%{perl_vendorlib}/HTTP/Tinyish/Base.pm
%{_mandir}/man3/HTTP::Tinyish.*

%files Curl
%license LICENSE
%{perl_vendorlib}/HTTP/Tinyish/Curl.pm

%files HTTPTiny
%license LICENSE
%{perl_vendorlib}/HTTP/Tinyish/HTTPTiny.pm

%files LWP
%license LICENSE
%{perl_vendorlib}/HTTP/Tinyish/LWP.pm

%files Wget
%license LICENSE
%{perl_vendorlib}/HTTP/Tinyish/Wget.pm

%changelog
%autochangelog
