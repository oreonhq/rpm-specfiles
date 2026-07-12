%global source0_hash ef4cfc50323bdfd0f13377bfb98f0860b4ad1dd91adf5e874401886bebd1fd8a

Name:           perl-MouseX-Foreign
Version:        1.000
Release:        30%{?dist}
Summary:        Extends non-Mouse classes as well as Mouse classes
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MouseX-Foreign
Source0:        https://cpan.metacpan.org/authors/id/G/GF/GFUJI/MouseX-Foreign-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Mouse) >= 0.77
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util)
BuildRequires:  perl(Mouse::Util::MetaRole)
# Tests:
BuildRequires:  perl(Any::Moose) >= 0.15
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Mouse::Exporter)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Mouse)
BuildRequires:  perl(Test::Requires)
# Optional tests:
BuildRequires:  perl(Moose)
Requires:       perl(Mouse) >= 0.77

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Mouse\\)$

Provides:       perl(MouseX::Foreign)
Provides:       perl(MouseX::Foreign)
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

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
