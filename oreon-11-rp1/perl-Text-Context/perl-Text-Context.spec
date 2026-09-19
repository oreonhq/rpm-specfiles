%global source0_hash 6f42b7c9ab3776a0cff9d98ba10872fe1fdae55c544ef28280c6865def490528

Name:           perl-Text-Context
Version:        3.7
Release:        45%{?dist}
Summary:        Handle highlighting search result context snippets
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Text-Context
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMTM/Text-Context-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(constant)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Context::EitherSide) >= 1.1
BuildRequires:  perl(UNIVERSAL::require) >= 0.03
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.09

%description
Given a piece of text and some search terms, produces an object which
locates the search terms in the message, extracts a reasonable-length
string containing all the search terms, and optionally dumps the string out
as HTML text with the search terms highlighted in bold.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Context-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
