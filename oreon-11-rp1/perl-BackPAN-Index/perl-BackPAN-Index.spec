%global source0_hash c7a717e14c880d47c25e6ad028ddb869952dfb3ad5aaadc350d573bb90265746

Name:           perl-BackPAN-Index
Version:        0.42
Release:        36%{?dist}
Summary:        Interface to the BackPAN index
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/BackPAN-Index
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHWERN/BackPAN-Index-%{version}.tar.gz
# Make tests parallel-safe, proposed to an upstream,
# <https://github.com/book/BackPAN-Index/pull/47>
Patch0:         BackPAN-Index-0.42-Make-tests-parallel-safe.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# ACTION_result_classes() in inc/MyBuilder.pm is not executed
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build) >= 0.37
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(App::Cache) >= 0.37
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(autodie)
BuildRequires:  perl(CPAN::DistnameInfo) >= 0.09
# "dbi:SQLite:dbname" in lib/BackPAN/Index/Database.pm
BuildRequires:  perl(DBD::SQLite) >= 1.25
BuildRequires:  perl(DBI)
# Neither DBIx::Class::Core or DBIx::Class::Schema are versioned
BuildRequires:  perl(DBIx::Class) >= 0.08109
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Mouse) >= 0.64
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(overload)
BuildRequires:  perl(Path::Class) >= 0.17
BuildRequires:  perl(Path::Class::Dir)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(URI) >= 1.54
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(Test::Compile) >= 0.11
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(URI::file)
Requires:       perl(App::Cache) >= 0.37
Requires:       perl(Archive::Extract)
Requires:       perl(DBD::SQLite) >= 1.25
Requires:       perl(DBI)
Requires:       perl(DBIx::Class) >= 0.08109
Requires:       perl(Path::Class) >= 0.17
Requires:       perl(Path::Class::Dir)
Requires:       perl(Path::Class::File)
Requires:       perl(URI) >= 1.54

# Parse::BACKPAN::Packages is deprecated in favor of BackPAN::Index
Obsoletes:      perl-Parse-BACKPAN-Packages <= 0.35

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((CLASS|Path::Class|Test::More|URI)\\)$
# Hide private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(TestUtils\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(TestUtils\\)

%description
This downloads, caches and parses the BackPAN index into a local database
for efficient querying.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.90

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n BackPAN-Index-%{version}
# Remove always skipped tests
for T in t/pod.t t/pod_coverage.t; do
    rm "$T"
    perl -i -ne 'print $_ unless m{^\Q'"$T"'\E}' MANIFEST
done
# Correct a shebangs
for F in examples/backpan.pl t/*.t t/Parse-BACKPAN-Packages/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove tests which search modules in ./lib
rm %{buildroot}%{_libexecdir}/%{name}/t/00compile.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
export BACKPAN_INDEX_TEST_NO_INTERNET=1
# Recursive prove somehow does not respect t/testrules.yml. Run serially.
exec prove -I . -r -j 1
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export BACKPAN_INDEX_TEST_NO_INTERNET=1
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc CHANGES examples README
%dir %{perl_vendorlib}/BackPAN
%{perl_vendorlib}/BackPAN/Index
%{perl_vendorlib}/BackPAN/Index.pm
%dir %{perl_vendorlib}/Parse
%dir %{perl_vendorlib}/Parse/BACKPAN
%{perl_vendorlib}/Parse/BACKPAN/Packages.pm
%{_mandir}/man3/BackPAN::Index.*
%{_mandir}/man3/BackPAN::Index::*
%{_mandir}/man3/Parse::BACKPAN::Packages.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
