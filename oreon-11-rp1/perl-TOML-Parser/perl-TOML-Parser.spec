%global source0_hash 2a8513b904e377e0cae726910be676f4ff96bd960001c358dd66dc7c37aa9a8e

Name:           perl-TOML-Parser
Version:        0.91
Release:        20%{?dist}
Summary:        Simple toml parser
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/TOML-Parser
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARUPA/TOML-Parser-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Storable) >= 2.38
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Deep::Fuzzy)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Types::Serialiser)
BuildRequires:  perl(constant)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%description
TOML::Parser is a simple toml parser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n TOML-Parser-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
