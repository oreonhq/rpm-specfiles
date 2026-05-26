# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Tie_IxHash_enables_optional_test
%else
%bcond_with perl_Tie_IxHash_enables_optional_test
%endif

Name:           perl-Tie-IxHash
Version:        1.23
Release:        42%{?dist}
Summary:        Ordered associative arrays for Perl

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tie-IxHash
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Tie-IxHash-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 fabb0b8c97e67c9b34b6cc18ed66f6c5e01c55b257dcf007555e0b027d4caf56
%global source0_file Tie-IxHash-1.23.tar.gz
# oreon url source checksums end

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.5
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test::More)
%if %{with perl_Tie_IxHash_enables_optional_test} && !%{defined perl_bootstrap}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
%endif

%description
This Perl module implements Perl hashes that preserve the order in
which the hash elements were added. The order is not affected when
values corresponding to existing keys in the IxHash are changed.
The elements can also be set to any arbitrary supplied order. The
familiar perl array operations can also be performed on the IxHash.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Tie-IxHash-1.23.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "fabb0b8c97e67c9b34b6cc18ed66f6c5e01c55b257dcf007555e0b027d4caf56" || { echo "oreon: Source0 SHA256 mismatch for Tie-IxHash-1.23.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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


%check
make test


%files
%doc Changes README
%{perl_vendorlib}/Tie/
%{_mandir}/man3/*.3pm*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.23-42
- Prepare for Oreon 11 (RP1)
