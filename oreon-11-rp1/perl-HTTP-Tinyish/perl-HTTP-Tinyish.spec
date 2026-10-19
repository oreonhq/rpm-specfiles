%global source0_hash e9ce94a9913f9275d312ded4ddb34f76baf011b6b8d6029ff2871d5bd7bae468
Name:           perl-HTTP-Tinyish
Version:        0.19
Release:        6%{?dist}
Summary:        HTTP::Tiny compatible HTTP client wrappers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Tinyish
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/HTTP-Tinyish-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(:HTTP-Tinyish:backend) = %{version}
Recommends:     perl(HTTP::Tinyish::LWP)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(HTTP::Tiny\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list
%files -n perl-HTTP-Tinyish-Curl -f %{oreon_filedir}/perl-HTTP-Tinyish-Curl.list
%files -n perl-HTTP-Tinyish-HTTPTiny -f %{oreon_filedir}/perl-HTTP-Tinyish-HTTPTiny.list
%files -n perl-HTTP-Tinyish-LWP -f %{oreon_filedir}/perl-HTTP-Tinyish-LWP.list
%files -n perl-HTTP-Tinyish-Wget -f %{oreon_filedir}/perl-HTTP-Tinyish-Wget.list

%changelog

%autochangelog
