%global source0_hash 59e76792e48058040d6a9217cad9e1a83301576d3e14955abe40841611ebe4e0
Name:           perl-Parse-CPAN-Packages
Version:        2.40
Release:        1%{?dist}
Summary:        Parse 02packages.details.txt.gz
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parse-CPAN-Packages
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MITHALDU/Parse-CPAN-Packages-%{version}.tar.gz
Patch0:         Parse-CPAN-Packages-2.40-Test::InDistDir.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Archive::Peek)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Moo)
BuildRequires:  perl(PPI)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Comprehensive Perl Archive Network (CPAN) is a very useful collection
of Perl code. It has several indices of the files that it hosts, including
a file named "02packages.details.txt.gz" in the "modules" directory. This
file contains lots of useful information and this module provides a simple
interface to the data contained within.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Parse-CPAN-Packages-%{version}
# Remove the need for (so-far unpackaged) Test::InDistDir
%patch -P0 -p1
# Strip spurious exec permissions
find . -type f -exec chmod -c -x {} \;

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
