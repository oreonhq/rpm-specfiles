%global source0_hash c7a717e14c880d47c25e6ad028ddb869952dfb3ad5aaadc350d573bb90265746
Name:           perl-BackPAN-Index
Version:        0.42
Release:        36%{?dist}
Summary:        Interface to the BackPAN index
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/BackPAN-Index
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHWERN/BackPAN-Index-%{version}.tar.gz
Patch0:         BackPAN-Index-0.42-Make-tests-parallel-safe.patch
BuildArch:      noarch
Requires:       perl(App::Cache) >= 0.37
Requires:       perl(Archive::Extract)
Requires:       perl(DBD::SQLite) >= 1.25
Requires:       perl(DBI)
Requires:       perl(DBIx::Class) >= 0.08109
Requires:       perl(Path::Class) >= 0.17
Requires:       perl(Path::Class::Dir)
Requires:       perl(Path::Class::File)
Requires:       perl(URI) >= 1.54
Obsoletes:      perl-Parse-BACKPAN-Packages <= 0.35
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((CLASS|Path::Class|Test::More|URI)\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(TestUtils\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(TestUtils\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(App::Cache)
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(Config)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Path::Class::Dir)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(Test::Compile)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/00compile.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
export BACKPAN_INDEX_TEST_NO_INTERNET=1
exec prove -I . -r -j 1
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export BACKPAN_INDEX_TEST_NO_INTERNET=1
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-BackPAN-Index-tests -f %{oreon_filedir}/perl-BackPAN-Index-tests.list

%changelog

%autochangelog
