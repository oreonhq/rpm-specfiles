%global source0_hash dbea1af3759eecf80547d0699b4c4d4c0839c36498c62a340e90dc643f580f4c

Name:           perl-CGI-Application-Structured-Tools
Version:        0.015
Release:        38%{?dist}
Summary:        Tools to generate and maintain CGI::Application::Structured based web apps
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application-Structured-Tools
Source0:        https://cpan.metacpan.org/authors/id/V/VA/VANAMBURG/CGI-Application-Structured-Tools-%{version}.tar.gz
Patch0:         CGI-Application-Structured-Tools-0.015-Adapt-to-Module-Starter-1.71.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(CGI::Application::Structured)
BuildRequires:  perl(DBIx::Class::Schema::Loader)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(Module::Signature)
BuildRequires:  perl(Module::Starter)
BuildRequires:  perl(Module::Starter::Plugin::Template)
BuildRequires:  perl(Module::Starter::Simple)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Probe::Perl)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::WWW::Mechanize::CGIApp)

# RPM 4.8 style:
%filter_from_requires /main_module>)/d; /perl(<tmpl_var)/d; /perl(<tmpl_var/d
%{?perl_default_filter}
# RPM 4.9 style:
%global __requires_exclude %{?__requires_exclude|%__requires_exclude"|}main_module>\\)
%global __requires_exclude %__requires_exclude|perl\\(<tmpl_var\\)
%global __requires_exclude %__requires_exclude|perl\\(<tmpl_var

%description
A simple, medium-weight, MVC, DB web micro-framework built on
CGI::Application. The framework combines tested, well known plugins, templates
and helper scripts to provide a rapid development environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Structured-Tools-%{version}
%patch -P0

cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(<tmpl_var)/d'
EOF

%global __perl_requires %{_builddir}/CGI-Application-Structured-Tools-%{version}/%{name}-req
chmod +x %{__perl_requires}

cd lib/CGI/Application/Structured/Tools/templates
for i in create_dbic_schema.pl create_controller.pl \
         boilerplate.t perl-critic.t pod.t pod-coverage.t \
         test-app.t 00-signature.t 01-load.t; do
    chmod 755 $i;
    sed -i 's#!perl#!\/usr\/bin\/perl#' $i;
done

# These are not executables
chmod 644 index.tmpl config-dev.pl

# This is a perl script
sed -i -e '1i#!/usr/bin/perl' server.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README Todo
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/cas-starter.pl

%changelog
%autochangelog
