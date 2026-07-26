%global source0_hash 59e76792e48058040d6a9217cad9e1a83301576d3e14955abe40841611ebe4e0

Name:           perl-Parse-CPAN-Packages
Version:        2.40
Release:        31%{?dist}
Summary:        Parse 02packages.details.txt.gz
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parse-CPAN-Packages
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MITHALDU/Parse-CPAN-Packages-%{version}.tar.gz
Patch0:         Parse-CPAN-Packages-2.40-Test::InDistDir.patch
BuildArch:      noarch
# Module Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Module Runtime
BuildRequires:  perl(Archive::Peek)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(PPI)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(version)
# Test Suite
# perl(Test::InDistDir) dependency patched out
BuildRequires:  perl(Test::More)
# Runtime

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

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/Parse/
%{_mandir}/man3/Parse::CPAN::Packages.3pm*
%{_mandir}/man3/Parse::CPAN::Packages::Distribution.3pm*
%{_mandir}/man3/Parse::CPAN::Packages::Package.3pm*

%changelog
%autochangelog
