%global source0_hash 3944ef77e31ddb6b953870c7f43376a4f612fd2a217df121a121823a2b1c63ce

Name:           perl-Future-IO
Version:        0.23
Release:        1%{?dist}
Summary:        Future-returning IO core methods
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Future-IO
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Future-IO-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  perl-interpreter >= 5.10
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build) >= 0.4004
# runtime requirements
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Future)
BuildRequires:  perl(strict)
BuildRequires:  perl(Struct::Dumb)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::ExpectAndCheck)
BuildRequires:  perl(Test::Future::IO::Impl) >= 0.21
BuildRequires:  perl(Test::Pod) >= 1.00

%{?perl_default_filter}

Provides:       perl(Future::IO)
Provides:       perl(Future::IO::ImplBase)
Provides:       perl(Future::IO)
Provides:       perl(Future::IO::ImplBase)
%description
This package provides a few basic methods that behave similarly to the
same-named core perl functions relating to IO operations but yield
their results asynchronously via Future instances.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Future-IO-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Future*
%{_mandir}/man3/Future*

%changelog
%autochangelog
