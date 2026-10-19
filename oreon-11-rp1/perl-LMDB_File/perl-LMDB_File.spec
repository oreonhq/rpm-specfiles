%global source0_hash 1cb394093cd081a0c2b18bc96e311f9357ceb6ab73382b8eaa0310fb70ff689b
Name:           perl-LMDB_File
Version:        0.14
Release:        1%{?dist}
Summary:        Perl5 wrapper around the OpenLDAP's LMDB
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) OR Artistic-2.0
URL:            https://metacpan.org/release/LMDB_File
Source0:        https://cpan.metacpan.org/authors/id/S/SO/SORTIZ/LMDB_File-%{version}.tar.gz
ExcludeArch:    armv7hl i686
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
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libdb-devel
BuildRequires:  lmdb-devel
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(B)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(bytes)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%global oreon_srcdir LMDB_File-%{version}
%oreon_prep
%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
