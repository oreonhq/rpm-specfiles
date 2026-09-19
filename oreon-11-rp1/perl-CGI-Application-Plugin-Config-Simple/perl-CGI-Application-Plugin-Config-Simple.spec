%global source0_hash fa59fb5e6d3a14ec19c9600dde3ad79ea0b1f843057489478cd7a49d7b446692

Name:           perl-CGI-Application-Plugin-Config-Simple
Version:        1.01
Release:        45%{?dist}
Summary:        Add Config::Simple support to CGI::Application
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application-Plugin-Config-Simple
Source0:        https://cpan.metacpan.org/authors/id/W/WO/WONKO/CGI-Application-Plugin-Config-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(Config::Simple)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This module acts as a plugin for Config::Simple to be easily used inside of
a CGI::Application module. It does not provide every method available from
Config::Simple but rather easy access to your configuration variables. It
does however provide direct access to the underlying Config::General object
created if you want to use it's full power.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-Config-Simple-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
# t/main.t greps for 'Permission denied.'
LANG=C ./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
