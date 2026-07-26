%global source0_hash 993b7d7662e55798448a1edaccb9abd281d2bd23be7eab99f569b8e2962d3bc3

Name:           perl-File-DirList
Version:        0.05
Release:        15%{?dist}
Summary:        Provide a sorted list of directory content
# Standard perl license, see README.md
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/File-DirList
Source0:        https://cpan.metacpan.org/authors/id/T/TP/TPABA/File-DirList/File-DirList-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  sed

%description
File::DirList can be used to get sorted directory content list.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n File-DirList-%{version}

# Fix line endings
sed -i 's|\r||g' README

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/File::DirList*.*

%changelog
%autochangelog
