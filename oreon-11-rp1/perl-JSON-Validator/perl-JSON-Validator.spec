%global source0_hash eab57676bd3c7c318bc99118754e7f973259792f1ca13099e041938dd515bc05
Name:           perl-JSON-Validator
Version:        5.15
Release:        1%{?dist}
Summary:        Validate data against a JSON schema
License:        Artistic-2.0
URL:            https://metacpan.org/release/JSON-Validator
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/JSON-Validator-%{version}.tar.gz
BuildArch:      noarch
Recommends:     perl(Config)
Suggests:       perl(Data::Validate::Domain)
Suggests:       perl(Data::Validate::IP)
Requires:       perl(List::Util) >= 1.45
Requires:       perl(Mojo::UserAgent)
Requires:       perl(Mojolicious) >= 7.28
Suggests:       perl(Net::IDN::Encode)
Suggests:       perl(Sereal::Encoder) >= 4.00
Requires:       perl(YAML::XS) >= 0.67
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(List::Util\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Validate::Domain)
BuildRequires:  perl(Data::Validate::IP)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Collection)
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::JSON::Pointer)
BuildRequires:  perl(Mojo::Loader)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojo::UserAgent)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Net::IDN::Encode)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::StdHash)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(base)
BuildRequires:  perl(boolean)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
JSON::Validator is a data structure validation library based around JSON
Schema. This module can be used directly with a JSON schema or you can use
the elegant DSL schema-builder JSON::Validator::joi to define the schema
programmatically.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n JSON-Validator-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

unset JSON_VALIDATOR_CACHE_ANYWAYS JSON_VALIDATOR_CACHE_PATH \
    JSON_VALIDATOR_DEBUG JSON_VALIDATOR_NO_SEREAL \
    JSON_VALIDATOR_RECURSION_LIMIT JSON_VALIDATOR_WARN \
    TEST_ONLINE TEST_RANDOM_ITERATIONS
%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
