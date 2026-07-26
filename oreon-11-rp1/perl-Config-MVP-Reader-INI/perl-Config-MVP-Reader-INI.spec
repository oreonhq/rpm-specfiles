%global source0_hash 13c7aa27c1df98cd33ada399e59ff38fabfa9d65513e42af02f72c2d3f636247

Name:           perl-Config-MVP-Reader-INI
Version:        2.101465
Release:        10%{?dist}
Summary:        MVP config reader for .ini files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Config-MVP-Reader-INI
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Config-MVP-Reader-INI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Config::INI::Reader)
BuildRequires:  perl(Config::MVP) >= 2
BuildRequires:  perl(Config::MVP::Reader)
BuildRequires:  perl(Config::MVP::Reader::Findable::ByExtension)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Moose)
BuildRequires:  perl(Test::More)
# not automatically detected
Requires:       perl(Config::INI::Reader)
Requires:       perl(Config::MVP::Reader)
Requires:       perl(Config::MVP::Reader::Findable::ByExtension)

%{?perl_default_filter}

%description
Config::MVP::Reader::INI reads .ini files containing MVP-style
configuration.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-MVP-Reader-INI-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes eg README
%license LICENSE
%{perl_vendorlib}/Config*
%{_mandir}/man3/Config*

%changelog
%autochangelog
