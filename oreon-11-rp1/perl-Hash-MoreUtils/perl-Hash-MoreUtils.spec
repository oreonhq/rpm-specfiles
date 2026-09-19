%global source0_hash db9a8fb867d50753c380889a5e54075651b5e08c9b3b721cb7220c0883547de8

Name:           perl-Hash-MoreUtils
Version:        0.06
Release:        24%{?dist}
Summary:        Provide the stuff missing in Hash::Util
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Hash-MoreUtils
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/Hash-MoreUtils-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  %{__perl}
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.90

%description
Similar to List::MoreUtils, Hash::MoreUtils contains trivial but commonly-
used functionality for hashes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Hash-MoreUtils-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

%check
%{__make} test

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
