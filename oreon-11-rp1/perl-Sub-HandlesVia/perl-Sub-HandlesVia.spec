%global source0_hash dc706e094a378a819f74eb3266ad78dabc16d941c1c5d08702d1e4cf45c9859e
Name:           perl-Sub-HandlesVia
Version:        0.053005
Release:        1%{?dist}
Summary:        Alternative handles_via implementation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Sub-HandlesVia
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Sub-HandlesVia-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(B)
Recommends:     perl(Moo::_Utils)
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Eval::TypeTiny)
BuildRequires:  perl(Exporter::Shiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Moo::_Utils)
BuildRequires:  perl(MooX::TypeTiny)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::ArrayRef)
BuildRequires:  perl(MooseX::Extended)
BuildRequires:  perl(MooseX::InsideOut)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Object::Pad)
BuildRequires:  perl(Object::Pad::MetaFunctions)
BuildRequires:  perl(Role::Hooks)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Type::Params)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(constant)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(mro)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
If you've used Moose's native attribute traits, or MooX::HandlesVia before,
you should have a fairly good idea what this does.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Sub-HandlesVia-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install} DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
