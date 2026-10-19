%global source0_hash 9b5eefd82a9544582d43d2fb4e3d07e3f97d93293568593b41ad5010afccc785
%if !%{defined perl_bootstrap} && ! (0%{?rhel}) || (0%{?oreon} >= 11)
%bcond_without perl_Test_Simple_enables_Module_Pluggable
%bcond_without perl_Test_Simple_enables_optional_test
%bcond_without perl_Test_Simple_enables_unicode
%else
%bcond_with perl_Test_Simple_enables_Module_Pluggable
%bcond_with perl_Test_Simple_enables_optional_test
%bcond_with perl_Test_Simple_enables_unicode
%endif
Name:           perl-Test-Simple
Summary:        Basic utilities for writing tests
Epoch:          3
Version:        1.302225
Release:        1%{?dist}
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND CC0-1.0 AND LicenseRef-Public-Domain
URL:            https://metacpan.org/release/Test-Simple
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-Simple-%{version}.tar.gz
Patch0:         Test-Simple-1.302200-add_perl.patch
BuildArch:      noarch
%if %{with perl_Test_Simple_enables_Module_Pluggable} && !%{defined perl_bootstrap}
%endif
%if !%{defined perl_bootstrap}
%if %{with perl_Test_Simple_enables_optional_test}
%endif
%endif
%if %{with perl_Test_Simple_enables_unicode}
%endif
Requires:       perl(Data::Dumper)
Requires:       perl(JSON::PP)
%if %{with perl_Test_Simple_enables_Module_Pluggable} && !%{defined perl_bootstrap}
Recommends:     perl(Module::Pluggable) >= 2.7
%endif
Requires:       perl(mro)
Requires:       perl(PerlIO) >= 1.02
Requires:       perl(Sub::Util)
Requires:       perl(Term::ANSIColor)
Requires:       perl(Term::Table) >= 0.013
Requires:       perl(threads)
%if %{with perl_Test_Simple_enables_unicode}
Recommends:     perl(Unicode::GCString)
%endif
Requires:       perl(utf8)
Obsoletes:      perl-Test2-Suite < 0.000163-5
Provides:       perl-Test2-Suite = %{version}-%{release}
Provides:       bundled(Importer) = 0.026
Provides:       bundled(Scope::Guard) = 0.21
Provides:       bundled(Sub::Info) = 0.002
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Term::Table\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Dev::Null\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(main::HBase\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(main::HBase::Wrapped\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MyOverload\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MyTest\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MyTest::Target\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(SmallTest\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::Builder::NoOutput\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::Simple::Catch\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(TieOut\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
Provides:       perl(Test::More)
Provides:       perl(Test2)
Provides:       perl(Test2::API)
Provides:       perl(Test2::Event)
Provides:       perl(Test2::IPC)
Provides:       perl(Test2::Plugin::UTF8)
Provides:       perl(Test2::Require::Module)
Provides:       perl(Test2::Tools::Tiny)
Provides:       perl(Test2::Util::HashBase)
Provides:       perl(Test2::V0)
Provides:       perl(Test::Builder::Tester)
Provides:       perl(Test::Tester)
Provides:       perl(Test2::Require::Perl)
Provides:       perl(Test2::Require::Threads)
Provides:       perl(Test::Builder::Module)
Provides:       perl(Test)
Provides:       perl(Test::Builder)
Provides:       perl(Test::Simple)
Provides:       perl(Test::More)
Provides:       perl(Test::Builder::Module)
Provides:       perl(Test2::V0)
Provides:       perl(Test::Tester)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Term::Table)
BuildRequires:  perl(Term::Table::Cell)
BuildRequires:  perl(Term::Table::LineBreak)
BuildRequires:  perl(Term::Table::Util)
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Unicode::GCString)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package provides the bulk of the core testing facilities. For more
information, see perldoc for Test::Simple, Test::More, etc.

This package is the CPAN component of the dual-lifed core package Test-Simple.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(CPAN::Meta)
Requires:       perl(CPAN::Meta::Requirements) >= 2.120920
Requires:       perl(JSON::MaybeXS)
Requires:       perl(Module::Metadata)
Requires:       perl(Test::Pod) >= 0.95
Obsoletes:      perl-Test2-Suite-tests < 0.000163-5
Provides:       perl-Test2-Suite-tests = %{version}-%{release}
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Simple-%{version}

# Help generators to recognize Perl scripts
for F in `find . -type f -name '*.t'`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*(/usr/bin/)?perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

# Fix tests to work with added shellbangs
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -r -I . -j "$(getconf _NPROCESSORS_ONLN)" t/
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test %{!?perl_bootstrap:AUTHOR_TESTING=1}
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-Simple-tests -f %{oreon_filedir}/perl-Test-Simple-tests.list

%changelog

%autochangelog
