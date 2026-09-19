%global source0_hash eda5fe08de12ea885520fc9c2b15f448905eece5ce74c765895dfeacf9f3123c

Name:           perl-CGI-Application-Plugin-RateLimit
Version:        1.0
Release:        45%{?dist}
Summary:        Limits runmode call rate per user
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-RateLimit
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAMTREGAR/CGI-Application-Plugin-RateLimit-%{version}.tar.gz
# Fix a race in tests that depends on a time frame
Patch0:         CGI-Application-Plugin-RateLimit-1.0-Skip-some-test-if-run-time-execeeds-a-time-frame.patch

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
Requires:       perl(CGI::Application)

%{?perl_default_filter}

%description
This module provides protection against a user calling a runmode too
frequently. A typical use-case might be a contact form that sends email.
You'd like to allow your users to send you messages, but thousands of
messages from a single user would be a problem.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-RateLimit-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
