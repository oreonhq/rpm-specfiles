%global source0_hash 945bfb07c6d1af52773fb7845ba62e3a74111b35cbd2d5e43ef8319e55acbcea
Name:           perl-HTTP-Request-AsCGI
Summary:        Setup a CGI environment from a HTTP::Request
Version:        1.2
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/HTTP-Request-AsCGI-%{version}.tar.gz
URL:            https://metacpan.org/release/HTTP-Request-AsCGI
BuildArch:      noarch
Requires:       perl(HTTP::Response) >= 1.53
%{?perl_default_filter}
%{?perl_default_subpackage_tests}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTTP::Response\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Provides a convenient way of setting up an CGI environment from a
HTTP::Request.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Request-AsCGI-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

unset __PRESERVE_ENV_TEST GATEWAY_INTERFACE HTTP_HOST HTTP_X_TEST PATH_INFO \
    QUERY_STRING RELEASE_TESTING REQUEST_METHOD SCRIPT_NAME SERVER_NAME \
    SERVER_PORT
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
