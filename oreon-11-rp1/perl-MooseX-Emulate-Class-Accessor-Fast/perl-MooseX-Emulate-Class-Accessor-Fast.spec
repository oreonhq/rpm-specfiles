%global source0_hash 82eeb7ef1f0d25418ae406ea26912b241428d4b2ab9510d5e9deb3f72c187994

Name:       perl-MooseX-Emulate-Class-Accessor-Fast
Version:    0.009032
Release:    22%{?dist}
# lib/MooseX/Adopt/Class/Accessor/Fast.pm -> GPL+ or Artistic
# lib/MooseX/Emulate/Class/Accessor/Fast.pm -> GPL+ or Artistic
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Emulate Class::Accessor::Fast behavior using Moose attributes

Source:     https://cpan.metacpan.org/authors/id/H/HA/HAARG/MooseX-Emulate-Class-Accessor-Fast-%{version}.tar.gz
Url:        https://metacpan.org/release/MooseX-Emulate-Class-Accessor-Fast

BuildArch:  noarch

BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
# Run-time
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(Moose) >= 0.84
BuildRequires:  perl(Moose::Meta::Method::Accessor)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(namespace::clean)
# tests
BuildRequires: perl(base)
BuildRequires: perl(lib)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(warnings)

### auto-added reqs!
Requires:  perl(Moose) >= 0.84
Requires:  perl(namespace::clean)

%{?perl_default_filter}

%description
This module attempts to emulate the behavior of Class::Accessor::Fast
as accurately as possible using the Moose attribute system. The public
API of "Class::Accessor::Fast" is wholly supported, but the private
methods are not.  If you are only using the public methods (as you
should) migration should be a matter of switching your "use base" line
to a "with" line.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Emulate-Class-Accessor-Fast-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README Changes
%{perl_vendorlib}/Moose*
%{_mandir}/man3/Moose*.3*

%changelog
%autochangelog
