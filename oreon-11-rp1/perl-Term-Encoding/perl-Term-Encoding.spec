%global source0_hash 95ba9687d735d25a3cbe64508d7894f009c7fa2a1726c3e786e9e21da2251d0b

# Use I18N::Langinfo for handling locales properly
%bcond_without perl_Term_Encoding_enables_locale

Name:           perl-Term-Encoding
Version:        0.03
Release:        21%{?dist}
Summary:        Detect encoding of the current terminal
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-Encoding
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Term-Encoding-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
# Win32::Console not used
%if %{with perl_Term_Encoding_enables_locale}
# Optional run-time:
BuildRequires:  perl(I18N::Langinfo)
%endif
# Tests:
BuildRequires:  perl(Test::More)
# Test::Pod not used
Requires:       perl(warnings)
%if %{with perl_Term_Encoding_enables_locale}
Recommends:     perl(I18N::Langinfo)
%endif

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

%check
unset AUTHOR_TESTING DEV_MIYAGAWA_UNIX DEV_MIYAGAWA_WIN32
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
