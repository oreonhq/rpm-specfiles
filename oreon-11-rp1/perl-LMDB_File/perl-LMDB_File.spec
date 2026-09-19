%global source0_hash 1cb394093cd081a0c2b18bc96e311f9357ceb6ab73382b8eaa0310fb70ff689b

Name:           perl-LMDB_File
Version:        0.14
Release:        4%{?dist}
Summary:        Perl5 wrapper around the OpenLDAP's LMDB
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) OR Artistic-2.0
URL:            https://metacpan.org/release/LMDB_File
Source0:        https://cpan.metacpan.org/authors/id/S/SO/SORTIZ/LMDB_File-%{version}.tar.gz

# BZ1524377
ExcludeArch:    armv7hl i686

BuildRequires:  gcc
BuildRequires:  libdb-devel
BuildRequires:  lmdb-devel >= 0.9.17
BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Makefile:
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(B)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)

Requires:       lmdb-libs
Requires:       perl(AutoLoader)
Requires:       perl(Carp)
Requires:       perl(Exporter)
Requires:       perl(Fcntl)
Requires:       perl(Scalar::Util)
Requires:       perl(XSLoader)
Requires:       perl(strict)
Requires:       perl(warnings)
Requires:       rtld(GNU_HASH)
  
%{?perl_default_filter}

%description
LMDB_File is a Perl wrapper around the OpenLDAP's LMDB (Lightning
Memory-Mapped Database) C library.
LMDB is an ultra-fast, ultra-compact key-value data store developed
by Symas for the OpenLDAP Project. See http://symas.com/mdb/ for details.
LMDB_File provides full access to the complete C API, a thin Perl wrapper
with an Object-Oriented interface and a simple Perl's tie interface
compatible with others DBMs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n LMDB_File-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/LMDB_File*
%{_mandir}/man3/*

%changelog
%autochangelog
