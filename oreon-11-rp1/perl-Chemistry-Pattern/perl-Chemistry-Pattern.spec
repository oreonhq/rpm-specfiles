%global source0_hash 4616612523cf2318cb79c27315d5a3030c9c860c5df169035092cf297cc504af
%bcond check 1
Name:           perl-Chemistry-Pattern
Version:        0.27
Release:        1%{?dist}
Summary:        Chemical substructure pattern matching
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Chemistry-Pattern
Source0:        https://cpan.metacpan.org/authors/id/I/IT/ITUB/Chemistry-Pattern-%{version}.tar.gz
%if %{with check}
%endif
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Chemistry::Mol)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements basic pattern matching for molecules. The
Chemistry::Pattern class is a subclass of Chemistry::Mol, so patterns
have all the properties of molecules and can come from reading the same
file formats. Of course there are certain formats (such as SMARTS) that
are exclusively used to describe patterns.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Chemistry-Pattern-%{version}
chmod -x README

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
