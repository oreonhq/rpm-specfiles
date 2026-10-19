%global source0_hash 092c8d80e0350f925dc765f272c0ee28f992300b14f5b8698412204e6c857c42
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:           perl-Catalyst-Plugin-Session
Summary:        Catalyst generic session plugin
Version:        0.44
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Catalyst-Plugin-Session-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Plugin-Session
BuildArch:      noarch
%if !0%{?perl_bootstrap}
%endif
Requires:       perl(Catalyst::Runtime) >= 5.71001
Requires:       perl(MooseX::Emulate::Class::Accessor::Fast) >= 0.00801
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Exception)
BuildRequires:  perl(Catalyst::Plugin::Authentication)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(Crypt::SysRandom)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:  perl(Object::Signature)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:  perl(Test::WWW::Mechanize::PSGI)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This plugin is the base of two related parts of functionality
required for session management in web applications.

The first part, the State, is getting the browser to repeat back a
session key, so that the web application can identify the client and
logically string several requests together into a session.

The second part, the Store, deals with the actual storage of information
about the client. This data is stored so that the it may be revived for
every request made by the same client.

This plugin links the two pieces together.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Session-%{version}

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
