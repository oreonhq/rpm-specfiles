# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fabb0b8c97e67c9b34b6cc18ed66f6c5e01c55b257dcf007555e0b027d4caf56
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if ! (0%{?rhel})
%if 0%{?oreon}
%bcond_with perl_Tie_IxHash_enables_optional_test
%else
%bcond_without perl_Tie_IxHash_enables_optional_test
%endif
%else
%bcond_with perl_Tie_IxHash_enables_optional_test
%endif

Name:           perl-Tie-IxHash
Version:        1.23
Release:        1%{?dist}
Summary:        Ordered associative arrays for Perl

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tie-IxHash
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Tie-IxHash-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
BuildRequires:  perl(:VERSION) >= 5.5
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(vars)
BuildRequires:  perl(Test::More)
%if %{with perl_Tie_IxHash_enables_optional_test} && !%{defined perl_bootstrap}
BuildRequires:  perl(Test::Pod) >= 1.14
%endif

%description
This Perl module implements Perl hashes that preserve the order in
which the hash elements were added. The order is not affected when
values corresponding to existing keys in the IxHash are changed.
The elements can also be set to any arbitrary supplied order. The
familiar perl array operations can also be performed on the IxHash.

%prep
%oreon_sha256
%setup -q -n Tie-IxHash-%{version}

sed -i -e 's/\r$//' Changes README

%if !%{with perl_Tie_IxHash_enables_optional_test} || %{defined perl_bootstrap}
rm t/pod.t
perl -i -ne 'print $_ unless m{^t/pod\.t}' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Tie/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
