%global source0_hash ac24dd7da5b2247696becefc15ca935484367743aad44cb2c8cfa17a29ad8e03
Name:           perl-Devel-NYTProf
Version:        6.14
Release:        1%{?dist}
Summary:        Powerful feature-rich perl source code profiler
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-NYTProf
Source0:        https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/Devel-NYTProf-%{version}.tar.gz
Patch1:         Devel-NYTProf-6.13-Unbundled-flamegraph.patch
Suggests:       perl(Browser::Open)
Suggests:       perl(JSON::MaybeXS)
Requires:       flamegraph
%{?perl_default_filter}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(NYTProfTest\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Devel::NYTProf::Test)\s*$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  flamegraph
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(AutoSplit)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  zlib-devel
# /oreon:deps
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
rm -rf %{buildroot}/%{perl_vendorarch}/Devel/auto/
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/test62-subcaller1-b.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
for F in nytprofcalls nytprofcg nytprofcsv nytprofhtml nytprofmerge nytprofpf; do
    ln -s %{_bindir}/"$F" %{buildroot}%{_libexecdir}/%{name}/bin
done
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Devel-NYTProf-tests -f %{oreon_filedir}/perl-Devel-NYTProf-tests.list

%changelog

%autochangelog
