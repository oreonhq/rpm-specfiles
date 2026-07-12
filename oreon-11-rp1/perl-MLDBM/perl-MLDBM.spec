%global source0_hash 586880ed0c20801abbf6734747e13e0203edefece6ebc4f20ddb5059f02a17a2

Name:           perl-MLDBM
Version:        2.05
Release:        37%{?dist}
Summary:        Store multi-level hash structure in single level tied hash
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MLDBM
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHORNY/MLDBM-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  sed
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper) >= 2.08
BuildRequires:  perl(FreezeThaw)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Test::More)
# Optional Tests
# Note: test suite can use perl(DB_File) but that is based on libdb,
#       which has been deprecated since Fedora 33
#       https://fedoraproject.org/wiki/Changes/Libdb_deprecated
# Dependencies
# (none)

Provides:       perl(MLDBM)
%description
This module can serve as a transparent interface to any TIEHASH package that is
required to store arbitrary perl data, including nested references. Thus, this
module can be used for storing references and other arbitrary data within DBM
databases.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MLDBM-%{version}

# Fix line endings for documentation
sed -i -e 's/\r$//' README Changes

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/MLDBM/
%{perl_vendorlib}/MLDBM.pm
%{_mandir}/man3/MLDBM.3*

%changelog
%autochangelog
