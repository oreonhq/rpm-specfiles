%global source0_hash 8564849d5639015de23624e573cae2536eb909432b64d90098a1e0b452a9eb4b

%{?perl_default_filter}

Name:           perl-CDB_File
Version:        1.05
Release:        19%{?dist}
Summary:        Perl extension for access to cdb databases
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CDB_File
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/CDB_File-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
# BuildRequires:  perl(Carp) - not used for tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(B::COW)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings) >= 0.005
Requires:       perl(Carp)

%description
CDB_File is a module which provides a Perl interface to Dan Berstein's
cdb package. cdb is a fast, reliable, lightweight package for creating and 
reading constant databases.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CDB_File-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -size 0 -delete

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc ACKNOWLEDGE COPYRIGHT
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/CDB_File*
%{perl_vendorarch}/bun-x.pl
%{_mandir}/man3/*

%changelog
%autochangelog
