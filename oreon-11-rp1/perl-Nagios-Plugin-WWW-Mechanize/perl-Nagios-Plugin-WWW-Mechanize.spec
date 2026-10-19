%global source0_hash 21a8d34ed99155566b6731172eade9ba3d56e6012e3e77a85ee0bee7463cd852
Name:           perl-Nagios-Plugin-WWW-Mechanize
Version:        0.13
Release:        1%{?dist}
Summary:        Login to a web page as a user and get data as a Nagios plugin
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Nagios-Plugin-WWW-Mechanize
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TONVOON/Nagios-Plugin-WWW-Mechanize-%{version}.tar.gz
Patch0:         Nagios-Plugin-WWW-Mechanize-monitoring.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Monitoring::Plugin::Functions)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This module ties Monitoring::Plugin with WWW::Mechanize so that there's less
code in your perl script and the most common work is done for you.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Nagios-Plugin-WWW-Mechanize-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

# Use Monitoring::Plugin instead of Nagios::Plugin
mv t/lib/Nagios t/lib/Monitoring
%patch -P0

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
