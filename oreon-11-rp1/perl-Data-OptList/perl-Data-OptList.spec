%global source0_hash fa0e7cdc10925db925a82f8eb9608a701f1c2bf5e88d512d9acd46977e174056
%bcond_with perl_Data_OptList_enables_extra_test
%bcond_with perl_Data_OptList_enables_optional_test
Name:           perl-Data-OptList
Version:        0.115
Release:        1%{?dist}
Summary:        Parse and validate simple name/value option pairs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-OptList
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Data-OptList-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Data_OptList_enables_optional_test}
%endif
%if %{with perl_Data_OptList_enables_extra_test}
%endif
Provides:       perl(Data::OptList)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%check

make test
%if %{with perl_Data_OptList_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
