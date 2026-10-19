%global source0_hash f4292d741d756ecdd486297c8d196bc69ad1d915f83c9bc8e1d82b2dc9b91558
%bcond check 1
Name:           perl-Chemistry-Isotope
Version:        0.11
Release:        1%{?dist}
Summary:        Table of the isotopes exact mass data
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Chemistry-Isotope
Source0:        https://cpan.metacpan.org/authors/id/I/IT/ITUB/Chemistry-Isotope-%{version}.tar.gz
%if %{with check}
%endif
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module contains the exact mass data from the table of the isotopes. It has
an exportable function, isotope_mass, which returns the mass of an atom in mass
units given its mass number (A) and atomic number (Z); and a function
isotope_abundance which returns a table with the natural abundance of the
isotopes given an element symbol.

The table of the masses includes 2931 nuclides and is taken from
http://ie.lbl.gov/txt/awm95.txt (G. Audi and A.H. Wapstra, Nucl. Phys. A595,
409, 1995)

The table of natural abundances includes 288 nuclides and is taken from the
Commission on Atomic Weights and Isotopic Abundances report for the
International Union of Pure and Applied Chemistry in Isotopic Compositions of
the Elements 1989, Pure and Applied Chemistry, 1998, 70, 217.
http://www.iupac.org/publications/pac/1998/pdf/7001x0217.pdf

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Chemistry-Isotope-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} '%{buildroot}'/*
%oreon_autofiles main
%if %{with check}
%check

make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
