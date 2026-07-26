%global source0_hash cd2b328ea54a52596aeb879c6648110dd5cb8806c9beeffc0848e22be8497f75

Name:           perl-CGI-Application-Structured
Version:        0.007
Release:        42%{?dist}
Summary:        Medium-weight, MVC, DB web framework
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application-Structured
Source0:        https://cpan.metacpan.org/authors/id/V/VA/VANAMBURG/CGI-Application-Structured-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(CGI::Application::Dispatch)
BuildRequires:  perl(CGI::Application::Plugin::AutoRunmode)
BuildRequires:  perl(CGI::Application::Plugin::ConfigAuto)
BuildRequires:  perl(CGI::Application::Plugin::DBH)
BuildRequires:  perl(CGI::Application::Plugin::DBIC::Schema)
BuildRequires:  perl(CGI::Application::Plugin::DebugScreen)
BuildRequires:  perl(CGI::Application::Plugin::FillInForm)
BuildRequires:  perl(CGI::Application::Plugin::Forward)
BuildRequires:  perl(CGI::Application::Plugin::LogDispatch)
BuildRequires:  perl(CGI::Application::Plugin::Redirect)
BuildRequires:  perl(CGI::Application::Plugin::Session)
BuildRequires:  perl(CGI::Application::Plugin::SuperForm)
BuildRequires:  perl(CGI::Application::Plugin::TT)
BuildRequires:  perl(CGI::Application::Plugin::ValidateRM)
BuildRequires:  perl(CGI::Application::Server)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Simple)

%{?perl_default_filter}

%description
CGI::Application::Structured is an opinionated framework, based on
CGI::Application. It takes the view that developer time and consistent
projects structures can often be more cost-effective than focusing on the
highest performance on low cost hosting solutions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Structured-%{version}

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
%doc Changes LICENSE README Todo
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
