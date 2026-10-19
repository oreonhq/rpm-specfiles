%global source0_hash 379f39f24c6dae5c536332b17979fd90799dabccdfe8e792e7eead3eb8cda50c
Name:           perl-URI-Fetch
Version:        0.15
Release:        12%{?dist}
Summary:        Smart URI fetching/caching
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/URI-Fetch
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/URI-Fetch-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Compress::Zlib)
Requires:       perl(Filter::Util::Call)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Cache)
BuildRequires:  perl(Class::ErrorHandler)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(LWP)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(URI)
BuildRequires:  perl-generators
# /oreon:deps
%description
URI::Fetch is a smart client for fetching HTTP pages, notably syndication
feeds (RSS, Atom, and others), in an intelligent, bandwidth and time
saving way.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n URI-Fetch-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
