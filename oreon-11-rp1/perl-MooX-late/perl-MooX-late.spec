%global source0_hash 2ae5b1e3da5abc0e4006278ecbcfa8fa7c224ea5529a6a688acbb229c09e6a5f

Name:           perl-MooX-late
Version:        0.100
Release:        12%{?dist}
Summary:        Easily translate Moose code to Moo
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-late
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/MooX-late-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-interpreter >= 1:5.8.0
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.006000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX)
%if "%{version}" < "0.100"
BuildRequires:  perl(MooX::HandlesVia) >= 0.001004
%endif
BuildRequires:  perl(Scalar::Util)
%if "%{version}" >= "0.100"
BuildRequires:  perl(Sub::HandlesVia) >= 0.013
%endif
BuildRequires:  perl(Test::Fatal) >= 0.010
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires) >= 0.06
BuildRequires:  perl(Type::Utils) >= 1.000001
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(Moo) >= 1.006000
%if "%{version}" < "0.100"
Requires:       perl(MooX::HandlesVia) >= 0.001004
%endif
%if "%{version}" >= "0.100"
Requires:       perl(Sub::HandlesVia) >= 0.013
%endif
Requires:       perl(Type::Utils) >= 1.000001

# Filter under-specified requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo\\)$

%description
Moo is a light-weight object oriented programming framework which aims to
be compatible with Moose. It does this by detecting when Moose has been
loaded, and automatically "inflating" its classes and roles to full Moose
classes and roles. This way, Moo classes can consume Moose roles, Moose
classes can extend Moo classes, and so forth.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooX-late-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
