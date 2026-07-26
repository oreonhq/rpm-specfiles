%global source0_hash 2dfa20d752acb0e0e87a09c4ebe9ae183d29e238b769c0dbaf7098120b532a92

Name:           perl-MojoX-JSON-RPC
Version:        0.13
Release:        15%{?dist}
Summary:        Perl implementation of JSON-RPC 2.0 protocol for Mojolicious
License:        Artistic-2.0

URL:            https://metacpan.org/release/MojoX-JSON-RPC
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARASIK/MojoX-JSON-RPC-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::UserAgent)
# Mojolicious is the only versioned module
BuildRequires:  perl(Mojolicious) >= 7.13
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Mojolicious is the only versioned module
Requires:       perl(Mojolicious) >= 7.13

%{?perl_default_filter}

%description
This module implements a client and a server plugin for JSON-RPC 2.0 for use
with Mojolicious.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MojoX-JSON-RPC-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/MojoX*
%{perl_vendorlib}/Mojolicious/Plugin/JsonRpcDispatcher.pm
%{_mandir}/man3/MojoX*
%{_mandir}/man3/Mojolicious::Plugin::JsonRpcDispatcher.3pm.gz

%changelog
%autochangelog
