%global source0_hash 96765561271ee3285be3641c043a8bb262d341a564355352d37ed9512e6ea1eb

Name:           perl-Future
Version:        0.52
Release:        2%{?dist}
Summary:        Perl object system to represent an operation awaiting completion
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Future
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Future-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# runtime requirements
BuildRequires:  perl(B)
BuildRequires:  perl(Carp) >= 1.25
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test2::V0) >= 0.000148
Requires:       perl(Carp) >= 1.25

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Carp\\)$

Provides:       perl(Future)
Provides:       perl(Future::Utils)
Provides:       perl(Test::Future::Deferred)
Provides:       perl(Future::Utils)
%description
A Future object represents an operation that is currently in progress, or
has recently completed. It can be used in a variety of ways to manage the
flow of control, and data, through an asynchronous program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Future-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Future*
%{perl_vendorlib}/Test/Future*
%{_mandir}/man3/*

%changelog
%autochangelog
