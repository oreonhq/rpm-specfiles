%global source0_hash cb88a1a03115ce050016fd2c64b87ae149c908b3662d70f53670b28b562fb818
Name:           perl-Catalyst-Plugin-Authentication
Summary:        Infrastructure plugin for the Catalyst authentication framework
Version:        0.10024
Release:        4%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Catalyst-Plugin-Authentication-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Plugin-Authentication
BuildArch:      noarch
Requires:       perl(Catalyst::Runtime)
Requires:       perl(MooseX::Emulate::Class::Accessor::Fast)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Engine)
BuildRequires:  perl(Catalyst::Exception)
BuildRequires:  perl(Catalyst::Plugin::Session)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(Class::MOP::Class)
BuildRequires:  perl(Digest)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Object)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The authentication plugin provides generic user support for Catalyst apps.
It is the basis for both authentication (checking the user is who they
claim to be), and authorization (allowing the user to do what the system
authorizes them to do).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Authentication-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
