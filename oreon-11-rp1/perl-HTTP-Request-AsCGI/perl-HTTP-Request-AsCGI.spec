%global source0_hash 945bfb07c6d1af52773fb7845ba62e3a74111b35cbd2d5e43ef8319e55acbcea

Name:           perl-HTTP-Request-AsCGI
Summary:        Setup a CGI environment from a HTTP::Request
Version:        1.2
Release:        49%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/HTTP-Request-AsCGI-%{version}.tar.gz 
URL:            https://metacpan.org/release/HTTP-Request-AsCGI

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(HTTP::Response) >= 1.53
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(Test::More)
# Optional tests:
# Pod::Coverage::TrustPod not used
# Test::Pod 1.00 not used
# Test::Pod::Coverage 1.08 not used

Requires:       perl(HTTP::Response) >= 1.53

%{?perl_default_filter}
%{?perl_default_subpackage_tests}
# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTTP::Response\\)$

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

%check
unset __PRESERVE_ENV_TEST GATEWAY_INTERFACE HTTP_HOST HTTP_X_TEST PATH_INFO \
    QUERY_STRING RELEASE_TESTING REQUEST_METHOD SCRIPT_NAME SERVER_NAME \
    SERVER_PORT
make test

%files
%license LICENSE
%doc Changes README examples/
%dir %{perl_vendorlib}/HTTP
%dir %{perl_vendorlib}/HTTP/Request
%{perl_vendorlib}/HTTP/Request/AsCGI.pm
%{_mandir}/man3/HTTP::Request::AsCGI.*

%changelog
%autochangelog
