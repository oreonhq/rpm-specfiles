%global source0_hash ef4cfc50323bdfd0f13377bfb98f0860b4ad1dd91adf5e874401886bebd1fd8a
Name:           perl-MouseX-Foreign
Version:        1.000
Release:        30%{?dist}
Summary:        Extends non-Mouse classes as well as Mouse classes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MouseX-Foreign
Source0:        https://cpan.metacpan.org/authors/id/G/GF/GFUJI/MouseX-Foreign-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Mouse) >= 0.77
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Mouse\\)$
Provides:       perl(MouseX::Foreign)
Provides:       perl(MouseX::Foreign)
# oreon:deps
BuildRequires:  perl(Any::Moose)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Exporter)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util)
BuildRequires:  perl(Mouse::Util::MetaRole)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Mouse)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
MouseX::Foreign Perl module provides an ability for Mouse classes to extend
any classes, including non-Mouse classes, including Moose classes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MouseX-Foreign-%{version}

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
