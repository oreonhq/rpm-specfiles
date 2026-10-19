%global source1_hash e9ce535b0ecaf287af8c026c3268d6281a3c38e4079ae50548990cff18338f03
%global source0_hash 4e3323b13770ea529cc23e7c6aea6451372745f9fcccaa6ff171a458e6a3896b
Name:           prename
Version:        1.16.2
Release:        1%{?dist}
Summary:        Perl script to rename multiple files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PEDERST/rename-%{version}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEDERST/rename-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/pstray/rename/master/LICENSE
Patch0:         0001-Rename-the-executable-from-rename-to-prename.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Prename renames the file names supplied according to the rule specified as
the first argument. The argument is a Perl expression which is expected
to modify the $_ string for at least some of the file names specified.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n rename-%{version}
cp %{SOURCE1} .

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
