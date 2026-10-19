%global source0_hash bf0757d887243d3435ee8afaf796b16e54a2d9f44eafc69b0274c83ae57056e1
Name:           perl-Text-Context-EitherSide
Version:        1.4
Release:        1%{?dist}
Summary:        Get n words either side of search keywords
License:        Artistic-2.0
URL:            https://metacpan.org/release/Text-Context-EitherSide
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMTM/Text-Context-EitherSide-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Suppose you have a large piece of text - typically, say, a web page or a
mail message. And now suppose you've done some kind of full-text search on
that text for a bunch of keywords, and you want to display the context in
which you found the keywords inside the body of the text.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Context-EitherSide-%{version}

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
