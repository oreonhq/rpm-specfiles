%global source0_hash 767e9e9abbc42fae4769901b62426358b3b7131fb14f0c0a14edd690f285d969

Name:           perl-CGI-Application-Plugin-TT
Version:        1.06
Release:        4%{?dist}
Summary:        Add Template Toolkit support to CGI::Application
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-TT
Source0:        https://cpan.metacpan.org/authors/id/C/CE/CEESHEK/CGI-Application-Plugin-TT-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(warnings)
# runtime requirements
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Template)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# test requirements
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application::Plugin::DevPopup)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)

%{?perl_default_filter}

%description
CGI::Application::Plugin::TT adds support for the popular Template Toolkit
engine to your CGI::Application modules by providing several helper methods
that allow you to process template files from within your runmodes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-TT-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/CGI*
%{_mandir}/man3/CGI*

%changelog
%autochangelog
