%global source0_hash 9c12880ae20bda79366a89cab05eca53d728d94e5e99e988763effc013e8ee8c
Name:           perl-HTTP-Request-Params
Version:        1.02
Release:        1%{?dist}
Summary:        Retrieve GET/POST Parameters from HTTP Requests
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Request-Params
Source0:        https://cpan.metacpan.org/authors/id/K/KI/KIZ/HTTP-Request-Params-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Class::Accessor::Fast) >= 0.19
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Email::MIME)
BuildRequires:  perl(Email::MIME::ContentType)
BuildRequires:  perl(Email::MIME::Modifier)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Message)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This software does all the dirty work of parsing HTTP Requests to find
incoming query parameters.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Request-Params-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
