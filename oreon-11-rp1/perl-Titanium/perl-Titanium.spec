%global source0_hash be4e0d6ec4caaacff6e31b05555f68b77a1d537079da380fb584bdce595c0a2b

Name:           perl-Titanium
Version:        1.04
Release:        56%{?dist}
Summary:        Strong, lightweight web application framework
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Titanium
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKSTOS/Titanium-%{version}.tar.gz  
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI::Application) >= 4
BuildRequires:  perl(CGI::Application::Dispatch)
BuildRequires:  perl(CGI::Application::Plugin::ConfigAuto)
BuildRequires:  perl(CGI::Application::Plugin::DBH)
BuildRequires:  perl(CGI::Application::Plugin::DebugScreen)
BuildRequires:  perl(CGI::Application::Plugin::DevPopup)
BuildRequires:  perl(CGI::Application::Plugin::ErrorPage)
BuildRequires:  perl(CGI::Application::Plugin::FillInForm)
BuildRequires:  perl(CGI::Application::Plugin::Forward)
BuildRequires:  perl(CGI::Application::Plugin::LogDispatch)
BuildRequires:  perl(CGI::Application::Plugin::Redirect)
BuildRequires:  perl(CGI::Application::Plugin::Session)
BuildRequires:  perl(CGI::Application::Plugin::Stream)
BuildRequires:  perl(CGI::Application::Plugin::ValidateRM)
BuildRequires:  perl(CGI::Application::Server)
BuildRequires:  perl(CGI::Application::Standard::Config)
BuildRequires:  perl(Module::Build)
# Module::Starter::Plugin::CGIApp requires Titanium itself
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(Module::Starter::Plugin::CGIApp)
%endif
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::WWW::Mechanize::CGIApp)

%{?perl_default_filter}

%description
Titanium is a more user-friendly packaging of the mature CGI::Application
framework and some useful plugins, with the intention of creating a strong
but lightweight web application framework. It runs well in a plain CGI
environment and provides excellent performance in a persistent environment
such as FastCGI or mod_perl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Titanium-%{version}

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
