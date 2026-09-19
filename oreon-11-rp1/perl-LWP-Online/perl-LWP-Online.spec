%global source0_hash e26f91b7781f2a6d3b8c364961d5e74fae660d202dc97e3c88288030d736ce9c

# Perform tests that need the Internet
%bcond_with perl_LWP_Online_enables_network_test

Name:           perl-LWP-Online
Version:        1.08
Release:        44%{?dist}
Summary:        Check whether your process has an access to the web
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/LWP-Online
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/LWP-Online-%{version}.tar.gz
# Update Makefile.PL to not use Module::Install::DSL CPAN RT#148297
Patch0:         LWP-Online-1.08-Remove-using-of-MI-DSL.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.5
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(LWP::Simple) >= 5.805
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.42
BuildRequires:  perl(URI) >= 1.35
BuildRequires:  perl(vars)
Requires:       perl(Exporter)
Requires:       perl(Test::More) >= 0.42

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

%check
unset AUTOMATED_TESTING RELEASE_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/LWP*
%{_mandir}/man3/LWP*

%changelog
%autochangelog
