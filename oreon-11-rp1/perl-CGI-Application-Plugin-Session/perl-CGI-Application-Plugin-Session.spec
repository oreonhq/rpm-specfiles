%global source0_hash 38ea537cc0b760c36db47fd20375ce7f93f1adba5d12a45b56e613c749382f26

Name:           perl-CGI-Application-Plugin-Session
Version:        1.06
Release:        4%{?dist}
Summary:        Add CGI::Session support to CGI::Application
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-Session
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/CGI-Application-Plugin-Session-%{version}.tar.gz

BuildArch:      noarch
buildrequires:  coreutils
buildrequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI::Application) >= 3.21
BuildRequires:  perl(CGI::Session) >= 3.95
BuildRequires:  perl(CGI::Simple)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(CGI)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(CGI::Simple)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Exception)

%{?perl_default_filter}

%description
CGI::Application::Plugin::Session seamlessly adds session support to your
CGI::Application modules by providing a CGI::Session object that is
accessible from anywhere in the application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-Session-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/CGI*
%{_mandir}/man3/CGI::Application::Plugin::Session*

%changelog
%autochangelog
