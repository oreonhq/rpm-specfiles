%global source0_hash f2019e7703f39fc03e736b46a0609b2d5ad6a276f03e1af298894ac7506010ba

Name:           perl-CGI-Application-Plugin-MessageStack
Version:        0.34
Release:        45%{?dist}
Summary:        Message stack for your CGI::Application
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-MessageStack
Source0:        https://cpan.metacpan.org/authors/id/P/PU/PURDY/CGI-Application-Plugin-MessageStack-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(CGI::Application::Plugin::Session)
BuildRequires:  perl(CGI::Application::Plugin::TT)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)

%{?perl_default_filter}

%description
This plugin gives you a few support methods that you can call within your
cgiapp to pass along messages between requests for a given user.

It's recommended that you use this in conjunction with
CGI::Application::Plugin::Session. You can opt to not have the messages
persist and thereby, not use CAP-Session by using an option in the
capms_config method.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-MessageStack-%{version}

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
