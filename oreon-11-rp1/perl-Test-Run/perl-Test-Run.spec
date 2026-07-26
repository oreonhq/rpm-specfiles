%global source0_hash ab60a05299372b697c2f569d93208acf9b4129cc6603361bc9134c82f91091fc

Name:           perl-Test-Run
Version:        0.0306
Release:        4%{?dist}
Summary:        Extensible and object-oriented test harness for TAP scripts
# Build.PL:                         MIT
# lib/Test/Run.pm:                  MIT
# lib/Test/Run/Assert.pm:           MIT
# lib/Test/Run/Base.pm:             MIT
# lib/Test/Run/Base/Plugger.pm:     MIT
# lib/Test/Run/Base/PlugHelpers.pm: MIT
# lib/Test/Run/Base/Struct.pm:      MIT
# lib/Test/Run/Class/Hierarchy.pm:  MIT
# lib/Test/Run/Core.pm:             MIT
# lib/Test/Run/Core_GplArt.pm:      GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Test/Run/Iface.pm:            MIT
# lib/Test/Run/Obj:                 MIT
# lib/Test/Run/Obj/CanonFailedObj.pm:       MIT
# lib/Test/Run/Obj/Error.pm:        MIT
# lib/Test/Run/Obj/FailedObj.pm:    MIT
# lib/Test/Run/Obj/IntOrUnknown.pm: MIT
# lib/Test/Run/Obj/TestObj.pm:      MIT
# lib/Test/Run/Obj/TotObj.pm:       MIT
# lib/Test/Run/Output.pm:           MIT
# lib/Test/Run/Plugin/CmdLine/Output.pm:        MIT
# lib/Test/Run/Sprintf/Named/FromAccessors.pm:  MIT
# lib/Test/Run/Straps.pm:           MIT
# lib/Test/Run/Straps/Base.pm:      MIT
# lib/Test/Run/Straps/EventWrapper.pm:      MIT
# lib/Test/Run/Straps/StrapsTotalsObj.pm:   MIT
# lib/Test/Run/Straps_GplArt.pm:    "as perl, ie. GPL-2.0-only OR Artistic-1.0-Perl"
# lib/Test/Run/Trap/Obj.pm:         MIT
# LICENSE:                          MIT
# README:                           documents (GPL-1.0-or-later OR Artistic-1.0-Perl) AND MIT
# t/accumulate.t:                   MIT
# t/base.t:                         MIT
# t/hierarchy.t:                    MIT
# t/output.t:                       MIT
# t/test-failure-report.t           MIT
# t/switches.t:                     MIT
## Unbundled, never used
# t/lib/if.pm                       GPL-1.0-or-later OR Artistic-1.0-Perl
# t/lib/Test/Builder.pm:            GPL-1.0-or-later OR Artistic-1.0-Perl
# t/lib/Test/More.pm:               GPL-1.0-or-later OR Artistic-1.0-Perl
# t/lib/Test/Simple.pm:             GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-2.0-only AND MIT
URL:            https://metacpan.org/release/Test-Run
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Test-Run-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec) >= 0.6
BuildRequires:  perl(lib)
# Prefer Module::Build over ExtUtils::Maker because the Test::Run::Builder
# uses Module::Build too
BuildRequires:  perl(Module::Build) >= 0.36
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(IPC::System::Simple) >= 1.21
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::StrictConstructor)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(overload)
# POSIX is optional
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(TAP::Parser) >= 3.09
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(Text::Sprintf::Named) >= 0.02
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(UNIVERSAL::require)
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(if)
BuildRequires:  perl(POSIX)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::TrailingSpace)
Requires:       perl(IPC::System::Simple) >= 1.21
Requires:       perl(TAP::Parser) >= 3.09
Requires:       perl(Text::Sprintf::Named) >= 0.02

# Remove under-specified dependenices
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((IPC::System::Simple|TAP::Parser|Text::Sprintf::Named)\\)$
# Hide private modules
%global __requires_exclude %{__requires_exclude}|^perl\\((Dev::Null|MyFoo|MyHello)\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((Dev::Null|MyClass::|MyFoo|MyHello|MyTestRun::)
# Hide intetionally broken shebangs
%global __requires_exclude %{__requires_exclude}|^/usr/bin/perl-latest$

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
# Install tests
mkdir -p "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}
cp -a t "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}
# Remove tests that cannot work out of source tree
rm "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/t/{pod,pod-coverage,style-trailing-space}.t
cat > "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/leaked-dir.t writes to CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes DONE examples NOTES README TODO
%dir %{perl_vendorlib}/Test
%{perl_vendorlib}/Test/Run
%{perl_vendorlib}/Test/Run.pm
%{_mandir}/man3/Test::Run.*
%{_mandir}/man3/Test::Run::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
