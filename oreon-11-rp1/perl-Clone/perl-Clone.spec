%global source0_hash f9732a4a857974db30905233589113003301b585b0cecda29a21cfba5bb014f9
%bcond_without perl_Clone_enables_optional_test
Name:           perl-Clone
Version:        0.50
Release:        1%{?dist}
Summary:        Recursively copy perl data types
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Clone
Source0:        https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/Clone-%{version}.tar.gz
%if %{with perl_Clone_enables_optional_test}
%endif
%{?perl_default_filter}
Provides:       perl(Clone)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(B::COW)
BuildRequires:  perl(Class::DBI)
BuildRequires:  perl(Config)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::BigInt::GMP)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Taint::Runtime)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a clone() method that makes recursive
copies of nested hash, array, scalar and reference types,
including tied variables and objects.

clone() takes a scalar argument and an optional parameter that
can be used to limit the depth of the copy. To duplicate lists,
arrays or hashes, pass them in by reference.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Clone-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
