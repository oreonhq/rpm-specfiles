%global source0_hash df5ee5dc71be1d941cb1931c7adf866ad38d2fc20826caecb797244102f0eeee

# Run optional test
%if ! 0%{?rhel}
%bcond_without perl_BerkeleyDB_enables_optional_test
%else
%bcond_with perl_BerkeleyDB_enables_optional_test
%endif

# We need to know the exact DB version we're built against
%global db_ver %(sed '/DB_VERSION_STRING/!d;s/.*Berkeley DB[[:space:]]*\\([^:]*\\):.*/\\1/' /usr/include/db.h 2>/dev/null || echo 4.0.0)

Name:           perl-BerkeleyDB
Version:        0.67
Release:        1%{?dist}
Summary:        Interface to Berkeley DB
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/BerkeleyDB
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/BerkeleyDB-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libdb-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(strict)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(vars)
BuildRequires:  perl(XSLoader)
# Test Suite
BuildRequires:  perl(charnames)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
%if %{with perl_BerkeleyDB_enables_optional_test}
# Optional Tests
BuildRequires:  perl(Data::Dumper) >= 2.08
BuildRequires:  perl(Encode)
BuildRequires:  perl(MLDBM)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::CPAN::Meta::JSON)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod) >= 1.00
%endif
# Runtime
# Hard-code Berkeley DB requirement to avoid problems like #592209
Requires:       libdb = %{db_ver}
Requires:       perl(XSLoader)

# Don't "provide" private Perl libs
%{?perl_default_filter}

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(util\\)

%description
BerkeleyDB is a module that allows Perl programs to make use of the
facilities provided by Berkeley DB version 2 or greater (note: if
you want to use version 1 of Berkeley DB with Perl you need the DB_File
module).

Berkeley DB is a C library that provides a consistent interface to a
number of database formats. BerkeleyDB provides an interface to all
four of the database types (hash, btree, queue and recno) currently
supported by Berkeley DB.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n BerkeleyDB-%{version}

chmod -c -x Changes README

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
install -D -m755 dbinfo %{buildroot}%{_bindir}/dbinfo

# Remove files we don't want packaged
rm %{buildroot}%{perl_vendorarch}/{mkconsts,scan}.pl

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove release tests
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
rm %{buildroot}%{_libexecdir}/%{name}/t/meta*
# Do not change dir when blib does not exist
perl -i -pe "s{(chdir 't' if -d 't';)}{# \$1}" %{buildroot}%{_libexecdir}/%{name}/t/examples*.t
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
%doc README Changes Todo
%{_bindir}/dbinfo
%{perl_vendorarch}/BerkeleyDB/
%{perl_vendorarch}/BerkeleyDB.pm
%doc %{perl_vendorarch}/BerkeleyDB.pod
%{perl_vendorarch}/auto/BerkeleyDB/
%{_mandir}/man3/BerkeleyDB.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
