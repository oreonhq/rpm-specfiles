%global source0_hash 5b568a8ca0496be03515aacef8b11b46d15ddcf78a8e4026beacda5fb33f8a4f

Name:           perl-CGI-Application-Plugin-Redirect
Version:        1.00
Release:        46%{?dist}
Summary:        Easy external redirects in CGI::Application
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-Redirect
Source0:        https://cpan.metacpan.org/authors/id/C/CE/CEESHEK/CGI-Application-Plugin-Redirect-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

%{?perl_default_filter}

%description
This plugin provides an easy way to do external redirects in
CGI::Application. You don't have to worry about setting headers or worrying
about return types, as that is all handled for you.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-Redirect-%{version}

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
