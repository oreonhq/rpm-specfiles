%global source0_hash a1c8fdf4915fa82dcc2499d28aafaa3718b1b6a058077989abf9a8f7f7f264e6
Name:           perl-CGI-Prototype
Version:        0.9054
Release:        42%{?dist}
Summary:        Create a CGI application by subclassing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Prototype
Source0:        https://cpan.metacpan.org/authors/id/M/ME/MERLYN/CGI-Prototype-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(CGI)
Requires:       perl(Template)
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(My::
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(Class::Prototyped)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The core of every CGI application seems to be roughly the same:

*   Analyze the incoming parameters, cookies, and URLs to determine the state
of the application (let's call this "dispatch").  
* Based on the current state, analyze the incoming parameters to respond to 
any form submitted ("respond").  
*   From there, decide what response page should be generated, and produce it
("render").

CGI::Prototype creates a "Class::Prototyped" engine for doing all this, with 
the right amount of callback hooks to customize the process.  Because I'm 
biased toward Template Toolkit for rendering HTML, I've also integrated that 
as my rendering engine of choice. And, being a fan of clean MVC designs, the
classes become the controllers, and the templates become the views, with clean 
separation of responsibilities, and "CGI::Prototype" a sort of "archetypal" 
controller.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Prototype-%{version}

# make rpmlint happy
perl -pi -e 's|^#! ?perl|#!/usr/bin/perl|' t/*.t t/cprove
chmod -c -x t/cprove

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
