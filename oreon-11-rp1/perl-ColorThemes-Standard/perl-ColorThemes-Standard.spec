%global source0_hash 47e252acc537c38df5bc9a2008c613bdd910204682693a66b843b07db78b9723

Name:           perl-ColorThemes-Standard
Version:        0.003
Release:        12%{?dist}
Summary:        Standard collection of generic color themes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ColorThemes-Standard/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/ColorThemes-Standard-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(ColorThemeBase::Static::FromStructColors) >= 0.006
BuildRequires:  perl(parent)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
Requires:       perl(ColorThemeBase::Static::FromStructColors) >= 0.006

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((ColorThemeBase::Static::FromStructColors)\\)\s*$

Provides:       perl(ColorTheme::NoColor)
Provides:       perl(ColorThemes::Standard)
%description
This module contains a standard collection of generic color themes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n ColorThemes-Standard-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
