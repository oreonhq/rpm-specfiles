%global source0_hash ac24dd7da5b2247696becefc15ca935484367743aad44cb2c8cfa17a29ad8e03

Name:           perl-Devel-NYTProf
Version:        6.14
Release:        9%{?dist}
Summary:        Powerful feature-rich perl source code profiler
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-NYTProf
Source0:        https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/Devel-NYTProf-%{version}.tar.gz
Patch1:         Devel-NYTProf-6.13-Unbundled-flamegraph.patch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  flamegraph
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  zlib-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
# Unused BuildRequires:  perl(ActiveState::Browser)
# Unused BuildRequires:  perl(Apache)
BuildRequires:  perl(base)
# Unused BuildRequires:  perl(Browser::Open)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Which)
# Unused BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(AutoSplit)
# Unused BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
# Optional tests only
BuildRequires:  perl(Sub::Name) >= 0.11
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
# Unneded Requires:       perl(Apache)
# Optional features
Suggests:       perl(Browser::Open)
Suggests:       perl(JSON::MaybeXS)
Requires:       flamegraph

%{?perl_default_filter}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(NYTProfTest\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Devel::NYTProf::Test)\s*$

%description
Devel::NYTProf is a powerful feature-rich perl source code profiler.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-NYTProf-%{version}
%patch -P1 -p1

# Remove bundled flamegraph.pl
rm -r bin/flamegraph.pl
perl -i -ne 'print $_ unless m{flamegraph.pl}' MANIFEST

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
# remove duplicate installed lib in wrong location
rm -rf %{buildroot}/%{perl_vendorarch}/Devel/auto/
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# XXX - remove the tests, because it fails only with subpackage
rm %{buildroot}%{_libexecdir}/%{name}/t/test62-subcaller1-b.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
for F in nytprofcalls nytprofcg nytprofcsv nytprofhtml nytprofmerge nytprofpf; do
    ln -s %{_bindir}/"$F" %{buildroot}%{_libexecdir}/%{name}/bin
done
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
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
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes HACKING demo README.md
%{perl_vendorarch}/auto/Devel*
%{perl_vendorarch}/Devel*
%{_bindir}/nytprof*
%{_mandir}/man1/nytprof*
%{_mandir}/man3/Devel::MemoryProfiling*
%{_mandir}/man3/Devel::NYTProf*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
