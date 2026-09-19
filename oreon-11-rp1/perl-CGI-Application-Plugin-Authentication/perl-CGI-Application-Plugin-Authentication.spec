%global source0_hash ea2d7feec5b599580a5772e3e20e317336c50c12be9b0e9487ba0feb14ef1817

Name:           perl-CGI-Application-Plugin-Authentication
Version:        0.25
Release:        5%{?dist}
Summary:        Authentication framework for CGI::Application
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-Authentication
Source0:        https://cpan.metacpan.org/authors/id/W/WE/WESM/CGI-Application-Plugin-Authentication-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  findutils
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Apache::Htpasswd)
BuildRequires:  perl(Attribute::Handlers)
# BuildRequires:  perl(Authen::Simple)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(CGI::Application::Plugin::ActionDispatch)
BuildRequires:  perl(CGI::Application::Plugin::AutoRunmode)
BuildRequires:  perl(CGI::Application::Plugin::Session)
BuildRequires:  perl(CGI::Cookie)
BuildRequires:  perl(CGI::Util)
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(Color::Calc)
BuildRequires:  perl(Crypt::PasswdMD5)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(English)
BuildRequires:  perl(lib)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(overload)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::ConsistentVersion)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Regression)
BuildRequires:  perl(Test::Taint)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(warnings)
Requires:       perl(overload)

%{?perl_default_filter}

%description
CGI::Application::Plugin::Authentication adds the ability to
authenticate users in your CGI::Application modules. It imports one
method called 'authen' into your CGI::Application module. Through the
'authen' method you can call all the methods of the
CGI::Application::Plugin::Authentication plugin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-Authentication-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README example
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
