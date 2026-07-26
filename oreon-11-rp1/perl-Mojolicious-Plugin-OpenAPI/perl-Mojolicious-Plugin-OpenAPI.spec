%global source0_hash c29ca9243ced76037feb2ffaddd9ae94f94960c55b3df4a51fb26bf179e6d332

Name:           perl-Mojolicious-Plugin-OpenAPI
Version:        5.11
Release:        3%{?dist}
Summary:        OpenAPI / Swagger plugin for Mojolicious
# MIT-licensed files: t/spec/v2-petstore.json, t/v3-basic.t, t/v3-nullable.t, t/v3-style-array.t
# ASL 2.0-licensed files: t/spec/bundlecheck.json.
License:        Artistic-2.0

URL:            https://metacpan.org/release/Mojolicious-Plugin-OpenAPI
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/Mojolicious-Plugin-OpenAPI-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(utf8)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(JSON::Validator) >= 5.13
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Mojolicious::Plugin)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(constant)
# test requirements
BuildRequires:  perl(Data::Validate::IP)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojolicious) >= 9.00
BuildRequires:  perl(Mojolicious::Controller)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::Markdown)
BuildRequires:  perl(lib)
Requires:       perl(JSON::Validator) >= 5.15
Requires:       perl(Mojolicious::Plugin)
Recommends:     perl(Config)
Suggests:       perl(Text::Markdown)

%{?perl_default_filter}

## Filter unneeded Requires with RPM
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(JSON::Validator\\)$

%description
Mojolicious::Plugin::OpenAPI is a Mojolicious::Plugin that add routes and
input/output validation to your Mojolicious application based on a OpenAPI
(Swagger) specification. This plugin supports both version 2.0 and 3.x,
though 3.x might have some missing features.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mojolicious-Plugin-OpenAPI-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
DUMMY_DB_ERROR= JSON_VALIDATOR_DEBUG= MOJO_OPENAPI_DEBUG= %{make_build} test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
