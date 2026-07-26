%global source0_hash cae6edcbb2b6ed623f44c51dfb092597ff64c1887b5036b296451df459d7f8b6

Name:           perl-CGI-Application-Plugin-FillInForm
Version:        1.15
Release:        49%{?dist}
Summary:        Integrate CGI::Application with HTML::FillInForm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-FillInForm
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKSTOS/CGI-Application-Plugin-FillInForm-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(HTML::FillInForm) >= 1
BuildRequires:  perl(HTML::Parser) >= 1
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)

%{?perl_default_filter}

%description
This plugin for CGI::Application provides a mix-in method to make using
HTML::FillInForm more convenient.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-FillInForm-%{version}

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
