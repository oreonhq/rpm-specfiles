%global source0_hash 606894fc2e9f7cd13d9ec099aaac103a8f0943d1d80c2c486bae14730a39b7fc
Name:           perl-Parallel-ForkManager
Version:        2.04
Release:        1%{?dist}
Summary:        Simple parallel processing fork manager
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parallel-ForkManager
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Parallel-ForkManager-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Parallel::ForkManager)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8::all)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This module is intended for use in operations that can be done in parallel
where the number of processes to be forked off should be limited. Typical
use is a downloader which will be retrieving hundreds/thousands of files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Parallel-ForkManager-%{version}

# Prepare the example scripts for inclusion as documentation, as they are not
# generally useful and have additional dependencies.
sed -i -e '1d' examples/*.pl
chmod 644 examples/*.pl

i=lib/Parallel/ForkManager.pm
iconv -f iso-8859-1 -t utf-8 < $i > $i. && touch -r $i $i. && mv -f $i. $i

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
