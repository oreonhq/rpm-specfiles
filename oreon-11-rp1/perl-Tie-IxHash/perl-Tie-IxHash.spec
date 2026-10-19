%global source0_hash fabb0b8c97e67c9b34b6cc18ed66f6c5e01c55b257dcf007555e0b027d4caf56
%bcond_with perl_Tie_IxHash_enables_optional_test
Name:           perl-Tie-IxHash
Version:        1.23
Release:        42%{?dist}
Summary:        Ordered associative arrays for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tie-IxHash
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Tie-IxHash-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Tie_IxHash_enables_optional_test} && !%{defined perl_bootstrap}
%endif
Provides:       perl(Tie::IxHash)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This Perl module implements Perl hashes that preserve the order in
which the hash elements were added. The order is not affected when
values corresponding to existing keys in the IxHash are changed.
The elements can also be set to any arbitrary supplied order. The
familiar perl array operations can also be performed on the IxHash.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Tie-IxHash-%{version}

# Fix line endings
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.23-42
- Prepare for Oreon 11 (RP1)
