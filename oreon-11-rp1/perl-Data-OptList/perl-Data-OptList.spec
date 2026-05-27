%global source0_hash 9fd1093b917a21fb79ae1607db53d113b4e0ad8fe0ae776cb077a7e50044fdf3

%if ! (0%{?rhel})
# Run extra test
%bcond_without perl_Data_OptList_enables_extra_test
# Run optional test
%bcond_without perl_Data_OptList_enables_optional_test
%else
%bcond_with perl_Data_OptList_enables_extra_test
%bcond_with perl_Data_OptList_enables_optional_test
%endif

Name:           perl-Data-OptList
Version:        0.114
Release:        8%{?dist}
Summary:        Parse and validate simple name/value option pairs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-OptList
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Data-OptList-0.114.tar.gz

BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
# Module Runtime
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Install) >= 0.921
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.88
%if %{with perl_Data_OptList_enables_optional_test}
# Optional Tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(CPAN::Meta::Prereqs)
%endif
%if %{with perl_Data_OptList_enables_extra_test}
# Extra Tests
BuildRequires:  perl(Encode)
BuildRequires:  perl(Test::Pod) >= 1.41
%endif
# Dependencies
# (none)

%description
Hashes are great for storing named data, but if you want more than one entry
for a name, you have to use a list of pairs. Even then, this is really boring
to write:

$values = [
    foo => undef,
    bar => undef,
    baz => undef,
    xyz => { ... },
];

With Data::OptList, you can do this instead:

$values = Data::OptList::mkopt([
    qw(foo bar baz),
    xyz => { ... },
]);

This works by assuming that any defined scalar is a name and any reference
following a name is its value.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Data-OptList-%{version}

# Fix shellbangs in tests
for F in t/*; do
    perl -MExtUtils::MakeMaker -e "ExtUtils::MM_Unix->fixin(q{$F})"
done

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}

%check
make test
%if %{with perl_Data_OptList_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%license LICENSE
%doc Changes README t/
%{perl_vendorlib}/Data/
%{_mandir}/man3/Data::OptList.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.114-8
- Prepare for Oreon 11 (RP1)
