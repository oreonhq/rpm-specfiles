%global source0_hash 41c1faf183b61806b55889ceea1237750c1f61b9ce2735fdf33dc05536712dae

Name:           perl-AnyEvent-CacheDNS
Version:        0.08
Release:        32%{?dist}
Summary:        Simple DNS resolver with caching
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AnyEvent-CacheDNS
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POTYL/AnyEvent-CacheDNS-%{version}.tar.gz
# Correct test plan for case no Internet is available
# <https://github.com/potyl/perl-AnyEvent-CacheDNS/issues/5>
Patch0:         AnyEvent-CacheDNS-0.08-Fix-number-of-tests-to-skip.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Module::Build) >= 0.40
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(AnyEvent::DNS)
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dumper)
# Tests:
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Test::More)

%description
This Perl module provides a very simple DNS resolver that caches its results
and can improve the connection times to remote hosts.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n AnyEvent-CacheDNS-%{version}
chmod 0755 t/dns.t

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%dir %{perl_vendorlib}/AnyEvent
%{perl_vendorlib}/AnyEvent/CacheDNS.pm
%{_mandir}/man3/AnyEvent::CacheDNS.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
