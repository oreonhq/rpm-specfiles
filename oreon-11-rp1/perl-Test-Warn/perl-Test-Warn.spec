Name:           perl-Test-Warn
Version:        0.37
Release:        9%{?dist}
Summary:        Perl extension to test methods for warnings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Warn
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BIGJ/Test-Warn-0.37.tar.gz
# oreon url source checksums begin
%global source0_sha256 98ca32e7f2f5ea89b8bfb9a0609977f3d153e242e2e51705126cb954f1a06b57
%global source0_file Test-Warn-0.37.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(Carp) >= 1.22
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Uplevel) >= 0.12
BuildRequires:  perl(Test::Builder) >= 0.13
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Builder::Tester) >= 1.02
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       perl(Test::Builder) >= 0.13

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::Builder\\)$

%description
This module provides a few convenience methods for testing warning
based code.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Test-Warn-0.37.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "98ca32e7f2f5ea89b8bfb9a0609977f3d153e242e2e51705126cb954f1a06b57" || { echo "oreon: Source0 SHA256 mismatch for Test-Warn-0.37.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Test-Warn-%{version}

# Fix line endings
sed -i -e 's/\r$//' Changes

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Warn.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.37-9
- Prepare for Oreon 11 (RP1)
