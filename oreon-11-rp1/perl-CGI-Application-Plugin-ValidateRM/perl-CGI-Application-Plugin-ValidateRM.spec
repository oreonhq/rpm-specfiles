%global source0_hash 94b0d7d4b16b686e0c40b00deb16b9c2125ab3a1b15edda126d07517969297a8

Name:           perl-CGI-Application-Plugin-ValidateRM
Version:        2.52
Release:        10%{?dist}
Summary:        Help validate CGI::Application run modes using Data::FormValidator
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application-Plugin-ValidateRM
Source0:        https://cpan.metacpan.org/authors/id/F/FA/FANY/CGI-Application-Plugin-ValidateRM-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(Data::FormValidator)
BuildRequires:  perl(HTML::FillInForm)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)

%{?perl_default_filter}

%description
CGI::Application::Plugin::ValidateRM helps to validate web forms when using
the CGI::Application framework and the Data::FormValidator module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-ValidateRM-%{version}
chmod 644 Changes

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*
chmod 0644 $RPM_BUILD_ROOT/%{perl_vendorlib}/CGI/Application/Plugin/ValidateRM.pm

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
