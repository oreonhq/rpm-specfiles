%global source0_hash 02eeb8e0a98d9ee1016fbfd6c5fdc658f379e9e9ea57936e3889701563b105b3

Name:           perl-App-DuckDuckGo
Version:        0.008
Release:        33%{?dist}
Summary:        Application class used to query duckduckgo.com from the command line
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/App-DuckDuckGo
Source0:        https://cpan.metacpan.org/authors/id/G/GE/GETTY/App-DuckDuckGo-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(Moose) >= 1.24
BuildRequires:  perl(MooseX::Getopt) >= 0.35
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(WWW::DuckDuckGo) >= 0.004
BuildRequires:  perl(warnings)
Requires:       perl(Moose) >= 1.24
Requires:       perl(MooseX::Getopt) >= 0.35
Requires:       perl(WWW::DuckDuckGo) >= 0.004

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Moose\\)$
%global __requires_exclude %__requires_exclude|^perl\\(WWW::DuckDuckGo\\)$
%description
This is the class which is used by the duckduckgo command to do the work. Please
refer to the duckduckgo package to get the documentation for the command line
tool.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-DuckDuckGo-%{version}
sed -i 's|#!/usr/bin/env perl|#!%{__perl}|' bin/duckduckgo

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%package -n duckduckgo
Summary: Command line tool to use the DuckDuckGo API

%description -n duckduckgo
This application queries the DuckDuckGo API and displays the result in
a nice human-readable way or in a batch mode which could be used by a 
shell script to automatically work with the DuckDuckGo API results.

%files -n duckduckgo
%doc LICENSE README
%{_mandir}/man1/*
%{_bindir}/*

%changelog
%autochangelog
