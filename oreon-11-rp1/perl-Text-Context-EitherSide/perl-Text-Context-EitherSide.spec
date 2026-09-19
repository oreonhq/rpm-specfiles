%global source0_hash bf0757d887243d3435ee8afaf796b16e54a2d9f44eafc69b0274c83ae57056e1

Name:           perl-Text-Context-EitherSide
Version:        1.4
Release:        47%{?dist}
Summary:        Get n words either side of search keywords
License:        Artistic-2.0
URL:            https://metacpan.org/release/Text-Context-EitherSide
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMTM/Text-Context-EitherSide-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00

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

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
