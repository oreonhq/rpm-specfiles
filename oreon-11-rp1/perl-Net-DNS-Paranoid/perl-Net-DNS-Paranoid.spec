%global source0_hash a2bbedc3e5a91fdce61f6721ee9591266e4ef95c557f0fcb64fd97e123ed5bdf

# some tests require Internet access, don't enable by default
%bcond network_tests 0

Name:           perl-Net-DNS-Paranoid
Version:        0.09
Release:        6%{?dist}
Summary:        Paranoid DNS resolver
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-DNS-Paranoid/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Net-DNS-Paranoid-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter perl-generators coreutils
BuildRequires:  perl(:VERSION) >= 5.8.8
BuildRequires:  perl(Class::Accessor::Lite) >= 0.05
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Net::DNS) >= 0.68
# version req isn't added by RPM auto-dep
Requires:       perl(Net::DNS) >= 0.68
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%if %{with network_tests}
BuildRequires:  perl(Net::DNS::Resolver)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(utf8)
%endif

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

%check
unset VERBOSE
%if %{without network_tests}
rm t/01_simple.t
%endif
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Net/DNS/Paranoid*
%{_mandir}/man3/Net::DNS::Paranoid*

%changelog
%autochangelog
