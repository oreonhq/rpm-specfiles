%global source0_hash 8006392e9861e741537c2bbc9116c8e42b962f2e07e8d641a2ff6a11c6445077

Name:           perl-Array-Diff
# Because 0.08 compares newer than 0.05002 in Perl world
# but not in RPM world :-(
Epoch:          1
Version:        0.09
Release:        21%{?dist}
Summary:        Find the differences between two arrays
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Array-Diff
Source0:        https://cpan.metacpan.org/modules/by-module/Array/Array-Diff-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Algorithm::Diff) >= 1.19
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
# Dependencies
# (none)

Provides:       perl(Array::Diff)
%description
This module compares two arrays and returns the added or deleted elements in
two separate arrays. It's a simple wrapper around Algorithm::Diff.

If you need more complex array tools, check Array::Compare.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Array-Diff-%{version}

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
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Array/
%{_mandir}/man3/Array::Diff.3*

%changelog
%autochangelog
