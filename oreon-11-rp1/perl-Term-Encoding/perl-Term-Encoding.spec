%global source0_hash 95ba9687d735d25a3cbe64508d7894f009c7fa2a1726c3e786e9e21da2251d0b
%bcond_without perl_Term_Encoding_enables_locale
Name:           perl-Term-Encoding
Version:        0.03
Release:        21%{?dist}
Summary:        Detect encoding of the current terminal
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-Encoding
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Term-Encoding-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Term_Encoding_enables_locale}
%endif
Requires:       perl(warnings)
%if %{with perl_Term_Encoding_enables_locale}
Recommends:     perl(I18N::Langinfo)
%endif
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(I18N::Langinfo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Term::Encoding is a simple Perl module to detect an encoding the current
terminal expects, in various ways.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-Encoding-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

unset AUTHOR_TESTING DEV_MIYAGAWA_UNIX DEV_MIYAGAWA_WIN32
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
