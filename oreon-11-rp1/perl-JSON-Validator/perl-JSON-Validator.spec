%global source0_hash eab57676bd3c7c318bc99118754e7f973259792f1ca13099e041938dd515bc05

Name:           perl-JSON-Validator
Version:        5.15
Release:        3%{?dist}
Summary:        Validate data against a JSON schema
License:        Artistic-2.0

URL:            https://metacpan.org/release/JSON-Validator
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/JSON-Validator-%{version}.tar.gz

BuildArch:      noarch
# build dependencies
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# runtime deps
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Collection)
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::JSON::Pointer)
BuildRequires:  perl(Mojo::Loader)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojo::UserAgent)
BuildRequires:  perl(Mojo::Util)
# Mojo::Base is not versioned
BuildRequires:  perl(Mojolicious) >= 7.28
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::StdHash)
BuildRequires:  perl(Time::Local)
# YAML::XS || YAML::PP
BuildRequires:  perl(YAML::XS) >= 0.67
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
# optional runtime
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Validate::Domain)
BuildRequires:  perl(Data::Validate::IP)
BuildRequires:  perl(Net::IDN::Encode)
# If Sereal::Encoder is available, YAML::XS is not helpful, but still needed
# because of a suboptimal BEGIN section.
# Sereal::Encoder 4.00 skip to exhibit YAML::XS fallback
# test deps
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More) >= 1.30
BuildRequires:  perl(lib)
# Optional test deps
# Test::JSON::Schema::Acceptance not yet packaged
BuildRequires:  perl(boolean)
Recommends:     perl(Config)
Suggests:       perl(Data::Validate::Domain)
Suggests:       perl(Data::Validate::IP)
Requires:       perl(List::Util) >= 1.45
Requires:       perl(Mojo::UserAgent)
# No other perl-Mojolicious module is versioned
Requires:       perl(Mojolicious) >= 7.28
Suggests:       perl(Net::IDN::Encode)
Suggests:       perl(Sereal::Encoder) >= 4.00
# YAML::XS || YAML::PP
Requires:       perl(YAML::XS) >= 0.67

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(List::Util\\)$

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

%check
unset JSON_VALIDATOR_CACHE_ANYWAYS JSON_VALIDATOR_CACHE_PATH \
    JSON_VALIDATOR_DEBUG JSON_VALIDATOR_NO_SEREAL \
    JSON_VALIDATOR_RECURSION_LIMIT JSON_VALIDATOR_WARN \
    TEST_ONLINE TEST_RANDOM_ITERATIONS
%{make_build} test

%files
%doc Changes CONTRIBUTING.md
%{perl_vendorlib}/JSON*
%{_mandir}/man3/JSON*

%changelog
%autochangelog
