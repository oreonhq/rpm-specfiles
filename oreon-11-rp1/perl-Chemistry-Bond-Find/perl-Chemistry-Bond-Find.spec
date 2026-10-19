%global source0_hash 07ee896bf91cbe94f46dca0bb0d222c0989432a6c8255691bafadcf4cbb3fae6
%bcond check 1
Name:           perl-Chemistry-Bond-Find
Version:        0.23
Release:        1%{?dist}
Summary:        Detect bonds in a molecule from atomic 3D coords and assign formal bond orders
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Chemistry-Bond-Find
Source0:        https://cpan.metacpan.org/authors/id/I/IT/ITUB/Chemistry-Bond-Find-%{version}.tar.gz
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
This module provides functions for detecting the bonds in a molecule from its
3D coordinates by using simple cutoffs, and for guessing the formal bond
orders.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Chemistry-Bond-Find-%{version}
chmod -x Changes Makefile.PL README t/*.t

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
