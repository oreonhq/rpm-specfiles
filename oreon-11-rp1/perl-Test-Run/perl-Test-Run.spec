%global source0_hash ab60a05299372b697c2f569d93208acf9b4129cc6603361bc9134c82f91091fc
Name:           perl-Test-Run
Version:        0.0306
Release:        1%{?dist}
Summary:        Extensible and object-oriented test harness for TAP scripts
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-2.0-only AND MIT
URL:            https://metacpan.org/release/Test-Run
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Test-Run-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(IPC::System::Simple) >= 1.21
Requires:       perl(TAP::Parser) >= 3.09
Requires:       perl(Text::Sprintf::Named) >= 0.02
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((IPC::System::Simple|TAP::Parser|Text::Sprintf::Named)\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\((Dev::Null|MyFoo|MyHello)\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((Dev::Null|MyClass::|MyFoo|MyHello|MyTestRun::)
%global __requires_exclude %{__requires_exclude}|^/usr/bin/perl-latest$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::StrictConstructor)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(TAP::Parser)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::TrailingSpace)
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(Text::Sprintf::Named)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
These Perl modules are an improved test harness based on Test::Harness, but
more modular, extensible and object-oriented.

%package tests
Summary:        Tests for %{name}
License:        MIT
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(if)
Requires:       perl(TAP::Parser) >= 3.09
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Run-%{version}
# Remove bundled modules
rm -rf t/lib/Test
rm -rf t/lib/if.pm
perl -i -n -e 'print $_ unless m{^t/lib/Test/}' MANIFEST
perl -i -n -e 'print $_ unless m{^t/lib/if\.pm}' MANIFEST
# Correct shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done
# Correct permissions
chmod a+x t/data/interpreters/wrong-mini-ok.pl\
    t/sample-tests/{inc_taint,invalid-perl,leak-file.t,no_output,segfault,shbang_misparse,taint,taint_warn,test_more_fail.t,with-myhello,with-myhello-and-myfoo,skipall}

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir="$RPM_BUILD_ROOT" create_packlist=0
%{_fixperms} "$RPM_BUILD_ROOT"/*
mkdir -p "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}
cp -a t "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}
rm "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/t/{pod,pod-coverage,style-trailing-space}.t
cat > "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-Run-tests -f %{oreon_filedir}/perl-Test-Run-tests.list

%changelog

%autochangelog
