Name:           perl-Parallel-ForkManager
Version:        2.03
Release:        4%{?dist}
Summary:        Simple parallel processing fork manager
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parallel-ForkManager
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Parallel-ForkManager-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 c0e0bead458224b9ac5bb32ed2b1fa088963b565521c1bb1a6a3566d522c2e35
%global source0_file Parallel-ForkManager-2.03.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Moo) >= 1.001000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Storable)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(utf8::all)


%description
This module is intended for use in operations that can be done in parallel
where the number of processes to be forked off should be limited. Typical
use is a downloader which will be retrieving hundreds/thousands of files.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Parallel-ForkManager-2.03.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c0e0bead458224b9ac5bb32ed2b1fa088963b565521c1bb1a6a3566d522c2e35" || { echo "oreon: Source0 SHA256 mismatch for Parallel-ForkManager-2.03.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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

%check
make test

%files
%doc Changes examples/
%{perl_vendorlib}/Parallel
%{_mandir}/man3/Parallel::ForkManager*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.03-4
- Prepare for Oreon 11 (RP1)
