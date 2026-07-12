%global source0_hash 5d18fa33ff6722542b52003e96a385dc5facf18cb17d601a6637c94653297cf9

Name:           perl-ColorThemeUtil-ANSI
Version:        0.002
Release:        14%{?dist}
Summary:        Utility routines related to color themes and ANSI code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ColorThemeUtil-ANSI/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/ColorThemeUtil-ANSI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Color::ANSI::Util) >= 0.164
BuildRequires:  perl(Exporter) >= 5.57
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Color::ANSI::Util) >= 0.161
Requires:       perl(Exporter) >= 5.57

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Exporter\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(Color::ANSI::Util\\)\\s*$

Provides:       perl(ColorThemeUtil::ANSI)
%description
This module provides utility routines related to color themes and ANSI
code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n ColorThemeUtil-ANSI-%{version}

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
