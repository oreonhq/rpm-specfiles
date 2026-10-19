%global source0_hash 13c7aa27c1df98cd33ada399e59ff38fabfa9d65513e42af02f72c2d3f636247
Name:           perl-Config-MVP-Reader-INI
Version:        2.101465
Release:        1%{?dist}
Summary:        MVP config reader for .ini files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-MVP-Reader-INI
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Config-MVP-Reader-INI-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Config::INI::Reader)
Requires:       perl(Config::MVP::Reader)
Requires:       perl(Config::MVP::Reader::Findable::ByExtension)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Config::INI::Reader)
BuildRequires:  perl(Config::MVP)
BuildRequires:  perl(Config::MVP::Reader)
BuildRequires:  perl(Config::MVP::Reader::Findable::ByExtension)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
