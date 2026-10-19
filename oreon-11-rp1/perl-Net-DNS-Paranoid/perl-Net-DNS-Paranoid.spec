%global source0_hash a2bbedc3e5a91fdce61f6721ee9591266e4ef95c557f0fcb64fd97e123ed5bdf
%bcond network_tests 0
Name:           perl-Net-DNS-Paranoid
Version:        0.09
Release:        1%{?dist}
Summary:        Paranoid DNS resolver
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-DNS-Paranoid/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Net-DNS-Paranoid-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Net::DNS) >= 0.68
%if %{with network_tests}
%endif
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Class::Accessor::Lite)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a wrapper module for Net::DNS.

This module detects IP address / host names for internal servers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-DNS-Paranoid-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

unset VERBOSE
%if %{without network_tests}
rm t/01_simple.t
%endif
./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
