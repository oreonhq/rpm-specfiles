%global source0_hash 322beb5d83e19d23d190c758ac4db614c61e82d67298fb80745f98d37316e159
Name:           perl-Test-Mock-Time
Version:        0.2.1
Release:        7%{?dist}
Summary:        Deterministic time & timers for event loop tests
License:        MIT
URL:            https://metacpan.org/release/Test-Mock-Time
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POWERMAN/Test-Mock-Time-v%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Carp)
BuildRequires:  perl(EV)
BuildRequires:  perl(Export::Attrs)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::Reactor::Poll)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockModule)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(bigint)
BuildRequires:  perl(bignum)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module replaces actual time with simulated time everywhere (core
time(), Time::HiRes, EV, AnyEvent with EV, Mojolicious, …) and provide
a way to write deterministic tests for event loop based applications
with timers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Mock-Time-v%{version}

%build

/usr/bin/perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
