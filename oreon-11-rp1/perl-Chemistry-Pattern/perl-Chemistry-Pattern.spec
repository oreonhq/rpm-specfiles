%global source0_hash 4616612523cf2318cb79c27315d5a3030c9c860c5df169035092cf297cc504af

%bcond check 1

Name:           perl-Chemistry-Pattern
Version:        0.27
Release:        %autorelease
Summary:        Chemical substructure pattern matching
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Chemistry-Pattern
Source0:        https://cpan.metacpan.org/authors/id/I/IT/ITUB/Chemistry-Pattern-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
%if %{with check}
BuildRequires:  perl(Chemistry::Mol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
%endif
BuildArch:      noarch

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

%if %{with check}
%check
make test
%endif

%files
%doc README
%dir %{perl_vendorlib}/Chemistry
%dir %{perl_vendorlib}/Chemistry/Pattern
%{perl_vendorlib}/Chemistry/Pattern.pm
%{perl_vendorlib}/Chemistry/Pattern/Atom.pm
%{perl_vendorlib}/Chemistry/Pattern/Bond.pm
%{_mandir}/man3/Chemistry::Pattern.3pm.*
%{_mandir}/man3/Chemistry::Pattern::Atom.3pm.*
%{_mandir}/man3/Chemistry::Pattern::Bond.3pm.*

%changelog
%autochangelog
