%global source0_hash 0bbe797a730210644a907d90cd4aa2b23ad580cb27bd39393bfc6a7ef9fdfdea

Name:           perl-Config-INI
Version:        0.029
Release:        10%{?dist}
Summary:        Config::INI Perl module
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Config-INI
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Config-INI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File) >= 1.14
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Mixin::Linewise::Readers) >= 0.110
BuildRequires:  perl(Mixin::Linewise::Writers)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

Provides:       perl(Config::INI)
Provides:       perl(Config::INI::Reader)
%description
Config::INI - simple .ini-file format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Config-INI-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README examples
%license LICENSE
%{perl_vendorlib}/Config*
%{_mandir}/man3/Config*

%changelog
%autochangelog
