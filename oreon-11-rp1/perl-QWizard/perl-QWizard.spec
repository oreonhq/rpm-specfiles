%global source0_hash 41e4feb68c5435b2a417e05a4a26107d5b0d54946b6ed3b55ca8dfca3d214337

Name:           perl-QWizard
Version:        3.15
Release:        48%{?dist}
Summary:        Graphical question and answer wizard system
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/QWizard
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HARDAKER/QWizard-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
# Only ./Storage modules have tests, thus many run-time dependencies are not
# used at tests.
# AutoLoader
BuildRequires:  perl(CGI)
# CGI::Cookie
# Chart::Lines
# Config
# Data::Dumper
# Exporter
# File::Temp
# Glib
# Gtk2
# IO::File
# MIME::Base64
# POSIX
BuildRequires:  perl(strict)
# Term::ReadLine
# Tk
# Tk::Balloon
# Tk::FileSelect
# Tk::Pane
# Tk::PNG
# Tk::Table
# Tk::Tree
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(Chart::Lines)
Requires:       perl(MIME::Base64)
Requires:       perl(Tk::Balloon)
Requires:       perl(Tk::PNG)
Requires:       perl(Tk::Tree)

%description
The QWizard module allows script authors to concentrate on the
content of the forms they want their users to fill in without
worrying about the display.  It allows "Question Wizard" like
interfaces to be very easily created and the results of the input
easily acted upon.  Scripts written which are entirely based on
QWizard inputs are able to be run from the command line which will
show a Gtk2, Tk window or as a ReadLine interactive session or as a
CGI script without modification.  Script writers do not need to know
which interface is being used to display the resulting form(s) as it
should be transparent to the script itself.

Other wizard interfaces exist for Perl, but this one strives very
hard to be both extensible and easy to code with requiring as little
work by script authors as possible.  It is also one of the only ones
that supports both web environments and windowing environments
without code modification required by the script author.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n QWizard-%{version}
# not needed perl script that is actually just a POD generator from dist
rm QWizard_Widgets.pl
perl -i -ne 'print $_ unless m{\A\QQWizard_Widgets.pl\E}' MANIFEST
# Correct permissions
chmod a-x examples/*.pl
chmod a+x Storage/t/tests.pl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a Storage/t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/file.t writes to CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I .
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
# Not parallel-safe: Storage/t/file.t creates a file and Storage/t/read-file.t
# reads it.
export HARNESS_OPTIONS=j1
make test

%files
%doc examples README
%dir %{perl_vendorlib}/auto
%{perl_vendorlib}/auto/QWizard
%{perl_vendorlib}/QWizard
%{perl_vendorlib}/QWizard.pm
%{perl_vendorlib}/QWizard_Widgets.pod
%{_mandir}/man3/QWizard.*
%{_mandir}/man3/QWizard::*
%{_mandir}/man3/QWizard_Widgets.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
