%global source0_hash ac357b5034a60f2db6b674c77e682e5b93efb0a37d19fd63cf95ea5965402530
%bcond check 1
Name:           perl-Chemistry-Mol
Version:        0.40
Release:        1%{?dist}
Summary:        Molecule object toolkit
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Chemistry-Mol
Source0:        https://cpan.metacpan.org/authors/id/M/ME/MERKYS/Chemistry-Mol-%{version}.tar.gz
%if %{with check}
%endif
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Clone)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Math::VectorReal)
BuildRequires:  perl(Set::Object)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This toolkit includes basic objects and methods to describe molecules. It
consists of several modules: Chemistry::Mol, Chemistry::Atom, Chemistry::Bond,
and Chemistry::File. These are the core modules of the PerlMol toolkit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Chemistry-Mol-%{version}
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
