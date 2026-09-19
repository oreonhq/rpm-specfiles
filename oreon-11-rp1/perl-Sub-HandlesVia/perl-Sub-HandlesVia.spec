%global source0_hash dc706e094a378a819f74eb3266ad78dabc16d941c1c5d08702d1e4cf45c9859e

Name:           perl-Sub-HandlesVia
Version:        0.053005
Release:        1%{?dist}

Summary:        Alternative handles_via implementation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Sub-HandlesVia
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Sub-HandlesVia-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.0

BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Eval::TypeTiny)
BuildRequires:  perl(experimental)
BuildRequires:  perl(Exporter::Shiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(feature)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(List::Util) >= 1.54
BuildRequires:  perl(MooseX::Extended)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Object::Pad)
BuildRequires:  perl(Object::Pad::MetaFunctions)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Role::Hooks) >= 0.008
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Type::Params) >= 1.004000
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(mro)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Optional, for improved tests
# N/A in Fedora: BuildRequires:  perl(Beam::Wire)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::_Utils)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::ArrayRef)
BuildRequires:  perl(MooseX::InsideOut)
# N/A in Fedora: BuildRequires:  perl(MooX::ProtectedAttributes)
# N/A in Fedora: BuildRequires:  perl(MooX::Tag::TO_HASH)
BuildRequires:  perl(MooX::TypeTiny)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Test::Moose)

Requires:       perl(B)
Recommends:     perl(Moo::_Utils)
# N/A in Fedora: Review is prepared
#Recommends:     perl(Sub::HandlesVia::XS) >= 0.002000

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

%check
%{__make} test

%files
%license LICENSE
%doc Changes CREDITS README
%{perl_vendorlib}/Sub
%{_mandir}/man3/Sub::HandlesVia*

%changelog
%autochangelog
