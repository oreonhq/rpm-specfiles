%global source0_hash c29ca9243ced76037feb2ffaddd9ae94f94960c55b3df4a51fb26bf179e6d332
Name:           perl-Mojolicious-Plugin-OpenAPI
Version:        5.11
Release:        1%{?dist}
Summary:        OpenAPI / Swagger plugin for Mojolicious
License:        Artistic-2.0
URL:            https://metacpan.org/release/Mojolicious-Plugin-OpenAPI
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/Mojolicious-Plugin-OpenAPI-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(JSON::Validator) >= 5.15
Requires:       perl(Mojolicious::Plugin)
Recommends:     perl(Config)
Suggests:       perl(Text::Markdown)
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(JSON::Validator\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Validate::IP)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(JSON::Validator)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Mojolicious::Controller)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Mojolicious::Plugin)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Markdown)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(utf8)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

DUMMY_DB_ERROR= JSON_VALIDATOR_DEBUG= MOJO_OPENAPI_DEBUG= %{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
