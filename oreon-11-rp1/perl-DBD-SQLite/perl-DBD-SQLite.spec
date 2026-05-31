%global source0_hash efbad7794bafaa4e7476c07445a33bbfe1040e380baa3395a02635eebe3859d5

# Run optional test
%bcond_without perl_DBD_SQLite_enables_optional_test

Name:           perl-DBD-SQLite
Version:        1.78
Release:        2%{?dist}
Summary:        SQLite DBI Driver
# lib/DBD/SQLite.pm:        GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:                  GPL-1.0-or-later OR Artistic-1.0-Perl
## unbundled
# inc/Test/FailWarnings.pm: Apache-2.0
# sqlite3.c:                Public Domain (copied from sqlite)
# sqlite3.h:                Public Domain (copied from sqlite)
# sqlite3ext.h:             Public Domain (copied from sqlite)
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/DBD-SQLite
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/DBD-SQLite-%{version}.tar.gz
# Use system sqlite if it is available
Patch0:         perl-DBD-SQLite-bz543982.patch
# Remove notes about bundled sqlite C source from man page and README
Patch1:         DBD-SQLite-1.62-Remove-bundled-source-extentions.patch
# Adapt tests to unbundled Test::FailWarnings
Patch2:         DBD-SQLite-1.64-Unbundle-Test-FailWarnings.patch
# if sqlite >= 3.6.0 then
#   perl-DBD-SQLite uses the external library
# else
#   perl-DBD-SQLite is self-contained (uses the sqlite local copy)
# But we always unbundle sqlite.
BuildRequires:  sqlite-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
# Prevent from bug #443495
BuildRequires:  perl(DBI) >= 1.607
BuildRequires:  perl(DBI::DBD)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(strict)
# Run-time:
# File::Basename not used
BuildRequires:  perl(locale)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
# POSIX not used
BuildRequires:  perl(Test::More)
# Test::FailWarnings not used
BuildRequires:  perl(Time::HiRes)
# Win32 not used
%if %{with perl_DBD_SQLite_enables_optional_test}
# Optional tests
BuildRequires:  perl(Unicode::UCD)
%endif

%{?perl_default_filter}

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(SQLiteTest\\)

%description
SQLite is a public domain, file-based, relational database engine that you can
find at <https://www.sqlite.org/>. This package provides a Perl DBI driver for
SQLite.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DBD-SQLite-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
# Remove bundled sqlite libraries (BZ#1059154)
# System libraries will be used
rm sqlite*
perl -i -ne 'print $_ unless m{^sqlite}' MANIFEST
# Remove bundled modules
rm -rf inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
# Handle optional tests
%if !%{with perl_DBD_SQLite_enables_optional_test}
rm t/virtual_table/21_perldata_charinfo.t
perl -i -ne 'print $_ unless m{^t/virtual_table/21_perldata_charinfo\.t}' MANIFEST
%endif

# Help generators to recognize Perl scripts
for F in `find t -name *.t`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build} OPTIMIZE="%{optflags}"

%install
%{make_install}
find %{buildroot} -type f  -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/DBD/
%{_mandir}/man3/*.3pm*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.78-2
- Prepare for Oreon 11 (RP1)
