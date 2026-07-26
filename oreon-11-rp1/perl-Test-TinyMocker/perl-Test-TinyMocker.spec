%global source0_hash 8fe5a4b2c47bb016dce489f4804c902b6b3a9f146eb7efd56cd80ffa00f5c231

# noarch, but to avoid *.list files interfering with manifest test
%global debug_package %{nil}

Name:           perl-Test-TinyMocker
Version:        0.05
Release:        35%{?dist}
Summary:        A very simple tool to mock external modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-TinyMocker
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-TinyMocker-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
# Module
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More) >= 0.88
# Release Tests
# Note: Test::Vars FTBFS with Perl 5.38 so dropped as buildreq
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::CheckManifest) >= 0.9
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
# Dependencies
# (none)

%description
This module allows you to override methods with arbitrary code blocks. This lets
you simulate some kind of behavior for your tests.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-TinyMocker-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}

%check
make test RELEASE_TESTING=1

%files
%license LICENSE
%doc AUTHORS Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::TinyMocker.3*

%changelog
%autochangelog
