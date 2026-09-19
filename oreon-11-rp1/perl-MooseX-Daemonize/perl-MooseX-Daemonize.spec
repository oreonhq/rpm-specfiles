%global source0_hash 8a7fb999dca9b802a85136a10141b2d3378a3ecde0527c1df73d55edb28e59b3

Name:           perl-MooseX-Daemonize
Version:        0.22
Release:        19%{?dist}
Summary:        Role for daemonizing your Moose based application
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/MooseX-Daemonize
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Daemonize-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Devel::AssertOS)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose) >= 0.33
BuildRequires:  perl(MooseX::Getopt) >= 0.07
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(Sub::Exporter::ForMethods)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::Pod::Coverage)

%{?perl_default_filter}

%description
Often you want to write a persistent daemon that has a pid file, and
responds appropriately to Signals. This module provides a set of basic
roles as an infrastructure to do that.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Daemonize-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENCE
%{perl_vendorlib}/MooseX*
%{perl_vendorlib}/Test*
%{_mandir}/man3/MooseX*
%{_mandir}/man3/Test*

%changelog
%autochangelog
