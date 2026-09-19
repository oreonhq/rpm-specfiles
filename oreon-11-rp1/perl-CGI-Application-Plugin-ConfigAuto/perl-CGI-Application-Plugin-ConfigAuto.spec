%global source0_hash 2197f2e6e15405e0ddcb0fb0c2152bb9d17a1b946e5969d8ef6a901f167cf535

Name:           perl-CGI-Application-Plugin-ConfigAuto
Version:        1.33
Release:        42%{?dist}
Summary:        Easy configuration file management for CGI::Application
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-ConfigAuto
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKSTOS/CGI-Application-Plugin-ConfigAuto-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(Config::Auto)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
CGI::Application::Plugin::ConfigAuto adds easy access to configuration file
variables to your CGI::Application modules. Lazy loading is used to prevent
the configuration file from being parsed if no configuration variables are
accessed during the request.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-ConfigAuto-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
