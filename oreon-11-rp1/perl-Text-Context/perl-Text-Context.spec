%global source0_hash 6f42b7c9ab3776a0cff9d98ba10872fe1fdae55c544ef28280c6865def490528
Name:           perl-Text-Context
Version:        3.7
Release:        45%{?dist}
Summary:        Handle highlighting search result context snippets
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Text-Context
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMTM/Text-Context-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Text::Context::EitherSide)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
