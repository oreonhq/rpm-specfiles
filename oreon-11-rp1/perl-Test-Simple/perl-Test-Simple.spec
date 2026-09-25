%global source0_hash 7cf84a18d6c9450e53ae8b4de5d5fa32c9fe99f3cebbe408fe59433f19921ec2

# Disable non-core dependencies when bootstrapping a core module
# Run optional tests with additional dependencies
# Break lines according to Unicode rules
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
Version:        1.302222
Release:        2%{?dist}
# CC0-1.0: lib/ok.pm
# Public Domain: lib/Test/Tutorial.pod
# GPL-1.0-or-later OR Artistic-1.0-Perl: the rest of the distribution
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND CC0-1.0 AND LicenseRef-Public-Domain
URL:            https://metacpan.org/release/Test-Simple
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-Simple-%{version}.tar.gz







Patch0:         Test-Simple-1.302200-add_perl.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
%if %{with perl_Test_Simple_enables_Module_Pluggable} && !%{defined perl_bootstrap}
BuildRequires:  perl(Module::Pluggable) >= 2.7
%endif
# mro used since Perl 5.010
BuildRequires:  perl(mro)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(PerlIO) >= 1.02
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util) >= 1.13
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Term::Table) >= 0.013
BuildRequires:  perl(Term::Table::Cell)
BuildRequires:  perl(Term::Table::LineBreak)
BuildRequires:  perl(Term::Table::Util)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(lib)
BuildRequires:  perl(threads)
# Optional Tests
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120920
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Test::Harness) >= 2.03
%if !%{defined perl_bootstrap}
%if %{with perl_Test_Simple_enables_optional_test}
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Pod) >= 0.95
BuildRequires:  perl(Test::Script)
%endif
%endif
%if %{with perl_Test_Simple_enables_unicode}
BuildRequires:  perl(Unicode::GCString)
%endif
BuildRequires:  perl(utf8)
# Dependencies
Requires:       perl(Data::Dumper)
Requires:       perl(JSON::PP)
%if %{with perl_Test_Simple_enables_Module_Pluggable} && !%{defined perl_bootstrap}
Recommends:     perl(Module::Pluggable) >= 2.7
%endif
# mro used since Perl 5.010
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
# perl-Test2-Suite-0.000163-4.fc41 merged
Obsoletes:      perl-Test2-Suite < 0.000163-5
Provides:       perl-Test2-Suite = %{version}-%{release}
# 3 inlined modules for future Perl Core
Provides:       bundled(Importer) = 0.026
Provides:       bundled(Scope::Guard) = 0.21
Provides:       bundled(Sub::Info) = 0.002

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Term::Table\\)$

# Remove private modules
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
# perl-Test2-Suite-0.000163-4.fc41 merged
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

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -r -I . -j "$(getconf _NPROCESSORS_ONLN)" t/
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test %{!?perl_bootstrap:AUTHOR_TESTING=1}

%files
%license LICENSE
%doc Changes README examples/
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/ok.pm
%{perl_vendorlib}/Test/Builder.pm
%{perl_vendorlib}/Test/Builder/
%{perl_vendorlib}/Test/More.pm
%{perl_vendorlib}/Test/Simple.pm
%{perl_vendorlib}/Test/Tester.pm
%{perl_vendorlib}/Test/Tester/
%doc %{perl_vendorlib}/Test/Tutorial.pod
%{perl_vendorlib}/Test/use/
%{perl_vendorlib}/Test2.pm
%{perl_vendorlib}/Test2/
%{_mandir}/man3/ok.3*
%{_mandir}/man3/Test::Builder.3*
%{_mandir}/man3/Test::Builder::Formatter.3*
%{_mandir}/man3/Test::Builder::Module.3*
%{_mandir}/man3/Test::Builder::Tester.3*
%{_mandir}/man3/Test::Builder::Tester::Color.3*
%{_mandir}/man3/Test::Builder::TodoDiag.3*
%{_mandir}/man3/Test::More.3*
%{_mandir}/man3/Test::Simple.3*
%{_mandir}/man3/Test::Tester.3*
%{_mandir}/man3/Test::Tester::Capture.3*
%{_mandir}/man3/Test::Tester::CaptureRunner.3*
%{_mandir}/man3/Test::Tutorial.3*
%{_mandir}/man3/Test::use::ok.3*
%{_mandir}/man3/Test2.3*
%{_mandir}/man3/Test2::API.3*
%{_mandir}/man3/Test2::API::Breakage.3*
%{_mandir}/man3/Test2::API::Context.3*
%{_mandir}/man3/Test2::API::Instance.3*
%{_mandir}/man3/Test2::API::InterceptResult.3*
%{_mandir}/man3/Test2::API::InterceptResult::Event.3*
%{_mandir}/man3/Test2::API::InterceptResult::Hub.3*
%{_mandir}/man3/Test2::API::InterceptResult::Squasher.3*
%{_mandir}/man3/Test2::API::Stack.3*
%{_mandir}/man3/Test2::AsyncSubtest.3*
%{_mandir}/man3/Test2::AsyncSubtest::Event::Attach.3*
%{_mandir}/man3/Test2::AsyncSubtest::Event::Detach.3*
%{_mandir}/man3/Test2::AsyncSubtest::Hub.3*
%{_mandir}/man3/Test2::Bundle.3*
%{_mandir}/man3/Test2::Bundle::Extended.3*
%{_mandir}/man3/Test2::Bundle::More.3*
%{_mandir}/man3/Test2::Bundle::Simple.3*
%{_mandir}/man3/Test2::Compare.3*
%{_mandir}/man3/Test2::Compare::Array.3*
%{_mandir}/man3/Test2::Compare::Bag.3*
%{_mandir}/man3/Test2::Compare::Base.3*
%{_mandir}/man3/Test2::Compare::Bool.3*
%{_mandir}/man3/Test2::Compare::Custom.3*
%{_mandir}/man3/Test2::Compare::DeepRef.3*
%{_mandir}/man3/Test2::Compare::Delta.3*
%{_mandir}/man3/Test2::Compare::Event.3*
%{_mandir}/man3/Test2::Compare::EventMeta.3*
%{_mandir}/man3/Test2::Compare::Float.3*
%{_mandir}/man3/Test2::Compare::Hash.3*
%{_mandir}/man3/Test2::Compare::Isa.3*
%{_mandir}/man3/Test2::Compare::Meta.3*
%{_mandir}/man3/Test2::Compare::Negatable.3*
%{_mandir}/man3/Test2::Compare::Number.3*
%{_mandir}/man3/Test2::Compare::Object.3*
%{_mandir}/man3/Test2::Compare::OrderedSubset.3*
%{_mandir}/man3/Test2::Compare::Pattern.3*
%{_mandir}/man3/Test2::Compare::Ref.3*
%{_mandir}/man3/Test2::Compare::Regex.3*
%{_mandir}/man3/Test2::Compare::Scalar.3*
%{_mandir}/man3/Test2::Compare::Set.3*
%{_mandir}/man3/Test2::Compare::String.3*
%{_mandir}/man3/Test2::Compare::Undef.3*
%{_mandir}/man3/Test2::Compare::Wildcard.3*
%{_mandir}/man3/Test2::Env.3*
%{_mandir}/man3/Test2::Event.3*
%{_mandir}/man3/Test2::Event::Bail.3*
%{_mandir}/man3/Test2::Event::Diag.3*
%{_mandir}/man3/Test2::Event::Encoding.3*
%{_mandir}/man3/Test2::Event::Exception.3*
%{_mandir}/man3/Test2::Event::Fail.3*
%{_mandir}/man3/Test2::Event::Generic.3*
%{_mandir}/man3/Test2::Event::Note.3*
%{_mandir}/man3/Test2::Event::Ok.3*
%{_mandir}/man3/Test2::Event::Pass.3*
%{_mandir}/man3/Test2::Event::Plan.3*
%{_mandir}/man3/Test2::Event::Skip.3*
%{_mandir}/man3/Test2::Event::Subtest.3*
%{_mandir}/man3/Test2::Event::TAP::Version.3*
%{_mandir}/man3/Test2::Event::V2.3*
%{_mandir}/man3/Test2::Event::Waiting.3*
%{_mandir}/man3/Test2::EventFacet.3*
%{_mandir}/man3/Test2::EventFacet::About.3*
%{_mandir}/man3/Test2::EventFacet::Amnesty.3*
%{_mandir}/man3/Test2::EventFacet::Assert.3*
%{_mandir}/man3/Test2::EventFacet::Control.3*
%{_mandir}/man3/Test2::EventFacet::Error.3*
%{_mandir}/man3/Test2::EventFacet::Hub.3*
%{_mandir}/man3/Test2::EventFacet::Info.3*
%{_mandir}/man3/Test2::EventFacet::Info::Table.3*
%{_mandir}/man3/Test2::EventFacet::Meta.3*
%{_mandir}/man3/Test2::EventFacet::Parent.3*
%{_mandir}/man3/Test2::EventFacet::Plan.3*
%{_mandir}/man3/Test2::EventFacet::Render.3*
%{_mandir}/man3/Test2::EventFacet::Trace.3*
%{_mandir}/man3/Test2::Formatter.3*
%{_mandir}/man3/Test2::Formatter::TAP.3*
%{_mandir}/man3/Test2::Handle.3*
%{_mandir}/man3/Test2::Hub.3*
%{_mandir}/man3/Test2::Hub::Interceptor.3*
%{_mandir}/man3/Test2::Hub::Interceptor::Terminator.3*
%{_mandir}/man3/Test2::Hub::Subtest.3*
%{_mandir}/man3/Test2::IPC.3*
%{_mandir}/man3/Test2::IPC::Driver.3*
%{_mandir}/man3/Test2::IPC::Driver::Files.3*
%{_mandir}/man3/Test2::Manual.3*
%{_mandir}/man3/Test2::Manual::Anatomy.3*
%{_mandir}/man3/Test2::Manual::Anatomy::API.3*
%{_mandir}/man3/Test2::Manual::Anatomy::Context.3*
%{_mandir}/man3/Test2::Manual::Anatomy::EndToEnd.3*
%{_mandir}/man3/Test2::Manual::Anatomy::Event.3*
%{_mandir}/man3/Test2::Manual::Anatomy::Hubs.3*
%{_mandir}/man3/Test2::Manual::Anatomy::IPC.3*
%{_mandir}/man3/Test2::Manual::Anatomy::Utilities.3*
%{_mandir}/man3/Test2::Manual::Concurrency.3*
%{_mandir}/man3/Test2::Manual::Contributing.3*
%{_mandir}/man3/Test2::Manual::Testing.3*
%{_mandir}/man3/Test2::Manual::Testing::Introduction.3*
%{_mandir}/man3/Test2::Manual::Testing::Migrating.3*
%{_mandir}/man3/Test2::Manual::Testing::Planning.3*
%{_mandir}/man3/Test2::Manual::Testing::Todo.3*
%{_mandir}/man3/Test2::Manual::Tooling.3*
%{_mandir}/man3/Test2::Manual::Tooling::FirstTool.3*
%{_mandir}/man3/Test2::Manual::Tooling::Formatter.3*
%{_mandir}/man3/Test2::Manual::Tooling::Nesting.3*
%{_mandir}/man3/Test2::Manual::Tooling::Plugin::TestExit.3*
%{_mandir}/man3/Test2::Manual::Tooling::Plugin::TestingDone.3*
%{_mandir}/man3/Test2::Manual::Tooling::Plugin::ToolCompletes.3*
%{_mandir}/man3/Test2::Manual::Tooling::Plugin::ToolStarts.3*
%{_mandir}/man3/Test2::Manual::Tooling::Subtest.3*
%{_mandir}/man3/Test2::Manual::Tooling::TestBuilder.3*
%{_mandir}/man3/Test2::Manual::Tooling::Testing.3*
%{_mandir}/man3/Test2::Mock.3*
%{_mandir}/man3/Test2::Plugin.3*
%{_mandir}/man3/Test2::Plugin::BailOnFail.3*
%{_mandir}/man3/Test2::Plugin::DieOnFail.3*
%{_mandir}/man3/Test2::Plugin::ExitSummary.3*
%{_mandir}/man3/Test2::Plugin::SRand.3*
%{_mandir}/man3/Test2::Plugin::Times.3*
%{_mandir}/man3/Test2::Plugin::UTF8.3*
%{_mandir}/man3/Test2::Require.3*
%{_mandir}/man3/Test2::Require::AuthorTesting.3*
%{_mandir}/man3/Test2::Require::AutomatedTesting.3*
%{_mandir}/man3/Test2::Require::EnvVar.3*
%{_mandir}/man3/Test2::Require::ExtendedTesting.3*
%{_mandir}/man3/Test2::Require::Fork.3*
%{_mandir}/man3/Test2::Require::Module.3*
%{_mandir}/man3/Test2::Require::NonInteractiveTesting.3*
%{_mandir}/man3/Test2::Require::Perl.3*
%{_mandir}/man3/Test2::Require::RealFork.3*
%{_mandir}/man3/Test2::Require::ReleaseTesting.3*
%{_mandir}/man3/Test2::Require::Threads.3*
%{_mandir}/man3/Test2::Suite.3*
%{_mandir}/man3/Test2::Todo.3*
%{_mandir}/man3/Test2::Tools.3*
%{_mandir}/man3/Test2::Tools::AsyncSubtest.3*
%{_mandir}/man3/Test2::Tools::Basic.3*
%{_mandir}/man3/Test2::Tools::Class.3*
%{_mandir}/man3/Test2::Tools::ClassicCompare.3*
%{_mandir}/man3/Test2::Tools::Compare.3*
%{_mandir}/man3/Test2::Tools::Defer.3*
%{_mandir}/man3/Test2::Tools::Encoding.3*
%{_mandir}/man3/Test2::Tools::Event.3*
%{_mandir}/man3/Test2::Tools::Exception.3*
%{_mandir}/man3/Test2::Tools::Exports.3*
%{_mandir}/man3/Test2::Tools::GenTemp.3*
%{_mandir}/man3/Test2::Tools::Grab.3*
%{_mandir}/man3/Test2::Tools::Mock.3*
%{_mandir}/man3/Test2::Tools::Ref.3*
%{_mandir}/man3/Test2::Tools::Refcount.3*
%{_mandir}/man3/Test2::Tools::Spec.3*
%{_mandir}/man3/Test2::Tools::Subtest.3*
%{_mandir}/man3/Test2::Tools::Target.3*
%{_mandir}/man3/Test2::Tools::Tester.3*
%{_mandir}/man3/Test2::Tools::Tiny.3*
%{_mandir}/man3/Test2::Tools::Warnings.3*
%{_mandir}/man3/Test2::Transition.3*
%{_mandir}/man3/Test2::Util.3*
%{_mandir}/man3/Test2::Util::ExternalMeta.3*
%{_mandir}/man3/Test2::Util::Facets2Legacy.3*
%{_mandir}/man3/Test2::Util::Grabber.3*
%{_mandir}/man3/Test2::Util::Guard.3*
%{_mandir}/man3/Test2::Util::HashBase.3*
%{_mandir}/man3/Test2::Util::Importer.3*
%{_mandir}/man3/Test2::Util::Ref.3*
%{_mandir}/man3/Test2::Util::Sig.3*
%{_mandir}/man3/Test2::Util::Stash.3*
%{_mandir}/man3/Test2::Util::Sub.3*
%{_mandir}/man3/Test2::Util::Table.3*
%{_mandir}/man3/Test2::Util::Table::LineBreak.3*
%{_mandir}/man3/Test2::Util::Times.3*
%{_mandir}/man3/Test2::Util::Trace.3*
%{_mandir}/man3/Test2::V0.3*
%{_mandir}/man3/Test2::V1.3*
%{_mandir}/man3/Test2::V1::Base.3*
%{_mandir}/man3/Test2::V1::Handle.3*
%{_mandir}/man3/Test2::Workflow.3*
%{_mandir}/man3/Test2::Workflow::BlockBase.3*
%{_mandir}/man3/Test2::Workflow::Build.3*
%{_mandir}/man3/Test2::Workflow::Runner.3*
%{_mandir}/man3/Test2::Workflow::Task.3*
%{_mandir}/man3/Test2::Workflow::Task::Action.3*
%{_mandir}/man3/Test2::Workflow::Task::Group.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3:1.302219-2
- Import
