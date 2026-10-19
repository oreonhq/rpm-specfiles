%global source0_hash 8006392e9861e741537c2bbc9116c8e42b962f2e07e8d641a2ff6a11c6445077
Name:           perl-Array-Diff
Epoch:          1
Version:        0.09
Release:        1%{?dist}
Summary:        Find the differences between two arrays
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Array-Diff
Source0:        https://cpan.metacpan.org/modules/by-module/Array/Array-Diff-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Array::Diff)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
