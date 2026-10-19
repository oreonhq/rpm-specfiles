%global source0_hash 8564849d5639015de23624e573cae2536eb909432b64d90098a1e0b452a9eb4b
%{?perl_default_filter}
Name:           perl-CDB_File
Version:        1.05
Release:        1%{?dist}
Summary:        Perl extension for access to cdb databases
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CDB_File
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/CDB_File-%{version}.tar.gz
Requires:       perl(Carp)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(B::COW)
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
