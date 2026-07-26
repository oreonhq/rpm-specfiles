%global source0_hash 092c8d80e0350f925dc765f272c0ee28f992300b14f5b8698412204e6c857c42

Name:           perl-Catalyst-Plugin-Session
Summary:        Catalyst generic session plugin
Version:        0.44
Release:        2%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Catalyst-Plugin-Session-%{version}.tar.gz 
URL:            https://metacpan.org/release/Catalyst-Plugin-Session
BuildArch:      noarch

# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Runtime) >= 5.71001
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Exception)
BuildRequires:  perl(Crypt::SysRandom) >= 0.007
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Moose) >= 0.76
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast) >= 0.00801
BuildRequires:  perl(Object::Signature)
BuildRequires:  perl(base)
BuildRequires:  perl(namespace::clean) >= 0.10
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(lib)
BuildRequires:  perl(utf8)
%if !0%{?perl_bootstrap}
# these cause circular builddeps
BuildRequires:  perl(Catalyst::Plugin::Authentication)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie) >= 0.03
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst) >= 0.51
BuildRequires:  perl(Test::WWW::Mechanize::PSGI)
%endif

Requires:       perl(Catalyst::Runtime) >= 5.71001
Requires:       perl(MooseX::Emulate::Class::Accessor::Fast) >= 0.00801

%{?perl_default_filter}

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

%check
%{make_build} test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
