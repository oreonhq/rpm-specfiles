%global source0_hash 5d61a5e6b4e4afc16d33e5290d5248b04a4fc4ee4c0a7dfc7fdd625968fba340
Name:           perl-DBM-Deep
Version:        2.0019
Release:        7%{?dist}
Summary:        A pure perl multi-level hash/array DBM
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBM-Deep
Source0:        https://cpan.metacpan.org/modules/by-module/DBM/DBM-Deep-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(Data::Dumper)
Requires:       perl(Digest::MD5)
Requires:       perl(Hash::Util::FieldHash)
Provides:       perl(DBM::Deep)
Provides:       perl(DBM::Deep)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle::Fmode)
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
A unique flat-file database module, written in pure perl. True multi-level
hash/array support (unlike MLDBM, which is faked), hybrid OO / tie()
interface, cross-platform FTPable files, and quite fast. Can handle
millions of keys and unlimited hash levels without significant slow-down.
Written from the ground-up in pure perl - this is NOT a wrapper around a
C-based DBM. Out-of-the-box compatibility with Unix, Mac OS X and Windows.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DBM-Deep-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

LONG_TESTS=1 TEST_SQLITE=1 ./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
