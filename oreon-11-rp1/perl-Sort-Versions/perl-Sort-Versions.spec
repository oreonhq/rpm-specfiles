Name:           perl-Sort-Versions
Version:        1.62
Release:        32%{?dist}
Summary:        Perl module for sorting of revision-like numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sort-Versions
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Sort-Versions-1.62.tar.gz
# oreon url source checksums begin
%global source0_sha256 bf5f3307406ebe2581237f025982e8c84f6f6625dd774e457c03f8994efd2eaa
%global source0_file Sort-Versions-1.62.tar.gz
# oreon url source checksums end


BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Test::More)

%description
A perl 5 module for sorting of revision-like numbers

Sort::Versions allows easy sorting of mixed non-numeric and numeric strings,
like the 'version numbers' that many shared library systems and revision
control packages use. This is quite useful if you are trying to deal with
shared libraries. It can also be applied to applications that intersperse
variable-width numeric fields within text. Other applications can
undoubtedly be found.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Sort-Versions-1.62.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bf5f3307406ebe2581237f025982e8c84f6f6625dd774e457c03f8994efd2eaa" || { echo "oreon: Source0 SHA256 mismatch for Sort-Versions-1.62.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Sort-Versions-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/Sort
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.62-32
- Prepare for Oreon 11 (RP1)
