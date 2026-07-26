%global source0_hash 38e673fb74fe0115882e5adb2674deb081fab721d728ee2a8114163d50c80788

Name:           perl-Lingua-Stem-It
Version:        0.02
Release:        44%{?dist}
Summary:        Porter's stemming algorithm for Italian
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-Stem-It
Source0:        https://cpan.metacpan.org/authors/id/A/AC/ACALPINI/Lingua-Stem-It-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only
# -

%description
This module applies the Porter Stemming Algorithm to its parameters,
returning the stemmed words.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-Stem-It-%{version}
perl -pi -e 's/\r//g' Changes README It.pm
chmod a-x -c Changes

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
