%global source0_hash 632bcd38de7b90abbb6c2a5577740d970ba482eb0e00cbc65edfb685f993c40f

Name:           perl-POE-Component-SimpleLog
Version:        1.05
Release:        47%{?dist}
Summary:        A simple logging system for POE 
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-SimpleLog            
Source0: https://cpan.metacpan.org/authors/id/A/AP/APOCAL/POE-Component-SimpleLog-%{version}.tar.gz        
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Carp)
BuildRequires:  perl(POE)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This module is a vastly simplified logging system that can do nice stuff.
Think of this module as a dispatcher for various logs.

This module *DOES NOT* do anything significant with logs, it simply routes
them to the appropriate place ( Events )

You register a log that you are interested in, by telling SimpleLog the target
session and target event. Once that is done, any log messages your program
generates ( sent to SimpleLog of course ) will be massaged, then sent to the
target session / target event for processing.

This enables an interesting logging system that can be changed during runtime
and allow pluggable interpretation of messages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-SimpleLog-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README Changes examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
