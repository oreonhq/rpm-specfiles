%global source0_hash d6b724b75a9c5b962083ee59983cf3b45feaf9a59b96127f1068684d53843e69

Name:           perl-Data-HexDump-XXD
Version:        0.1.1
Release:        34%{?dist}
Summary:        Format hexadecimal dump like xxd
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-HexDump-XXD
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POLETTIX/Data-HexDump-XXD-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)

%description
Produce an hexadecimal dump like the program xxd would do, and do the
reverse as well.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-HexDump-XXD-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
AUTHOR_TEST=1 ./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
