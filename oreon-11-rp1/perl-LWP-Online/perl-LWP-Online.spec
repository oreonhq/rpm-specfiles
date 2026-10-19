%global source0_hash e26f91b7781f2a6d3b8c364961d5e74fae660d202dc97e3c88288030d736ce9c
%bcond_with perl_LWP_Online_enables_network_test
Name:           perl-LWP-Online
Version:        1.08
Release:        1%{?dist}
Summary:        Check whether your process has an access to the web
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/LWP-Online
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/LWP-Online-%{version}.tar.gz
Patch0:         LWP-Online-1.08-Remove-using-of-MI-DSL.patch
BuildArch:      noarch
Requires:       perl(Exporter)
Requires:       perl(Test::More) >= 0.42
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module attempts to answer, as accurately as it can, one of the
nastiest technical questions there is: Am I on the internet?

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n LWP-Online-%{version}
%patch -P0 -p1
# Remove bundled libraries
rm -r inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
%if %{with perl_LWP_Online_enables_network_test}
rm t/02_main.t
perl -i -ne 'print $_ unless m{^t/02_main.t$}' MANIFEST
%endif

%build

perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

unset AUTOMATED_TESTING RELEASE_TESTING
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
