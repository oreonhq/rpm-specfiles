%global source0_hash 4e2fe355662017f4339d85013b90515a5a5487d8626537ee404151f7c6a4dd6d
Name:           perl-AnyEvent-Handle-UDP
Version:        0.050
Release:        1%{?dist}
Summary:        Client/server UDP handles for AnyEvent
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AnyEvent-Handle-UDP
Source0:        https://cpan.metacpan.org/modules/by-module/AnyEvent/AnyEvent-Handle-UDP-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Sub::Name)
# oreon:deps
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(AnyEvent::Util)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is an abstraction around UDP sockets for use with AnyEvent.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AnyEvent-Handle-UDP-%{version}

%build

perl Build.PL --installdirs=vendor
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
