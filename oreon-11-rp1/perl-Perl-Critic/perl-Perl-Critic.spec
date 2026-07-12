%global source0_hash 572a7c8758ba1c0ab6daf0bd40297c4f0dcf1516f084522df2c2bf04d525e232

# Run author tests
%if ! (0%{?rhel})
%bcond_without perl_Perl_Critic_enables_extra_test
%else
%bcond_with perl_Perl_Critic_enables_extra_test
%endif

Name:		perl-Perl-Critic
Version:	1.156
Release:	5%{?dist}
Summary:	Critique Perl source code for best-practices
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Perl-Critic
Source0:	https://cpan.metacpan.org/modules/by-module/Perl/Perl-Critic-%{version}.tar.gz
Patch0:		0001-Change-default-spell-check-tool-from-aspell-to-hunsp.patch
Patch3:		Perl-Critic-1.136-ppidump-shellbang.patch
BuildArch:	noarch

# Build process
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Fatal)
BuildRequires:	perl(lib)
BuildRequires:	perl(Module::Build) >= 0.42

# Module requirements
BuildRequires:	hunspell >= 1.2.12
BuildRequires:	hunspell-en
BuildRequires:	perl(:VERSION) >= 5.10.1
BuildRequires:	perl(B::Keywords) >= 1.23
BuildRequires:	perl(Carp)
BuildRequires:	perl(Config::Tiny) >= 2
BuildRequires:	perl(English)
BuildRequires:	perl(Exception::Class) >= 1.23
BuildRequires:	perl(Exporter) >= 5.58
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Spec::Unix)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(File::Which)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(List::SomeUtils) >= 0.55
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Module::Pluggable) >= 3.1
BuildRequires:	perl(parent)
BuildRequires:	perl(Perl::Tidy)
BuildRequires:	perl(Pod::PlainText)
BuildRequires:	perl(Pod::Select)
BuildRequires:	perl(Pod::Spell) >= 1
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(PPI) >= 1.277
BuildRequires:	perl(PPIx::QuoteLike)
BuildRequires:	perl(PPIx::Regexp) >= 0.010
BuildRequires:	perl(PPIx::Regexp::Util) >= 0.068
BuildRequires:	perl(PPIx::Utils::Traversal) >= 0.003
BuildRequires:	perl(Readonly) >= 2
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(String::Format) >= 1.18
BuildRequires:	perl(Term::ANSIColor) >= 2.02
BuildRequires:	perl(Test::Builder) >= 0.92
BuildRequires:	perl(Text::ParseWords) >= 3
BuildRequires:	perl(version) >= 0.77
BuildRequires:	perl(warnings)

# Main test suite
BuildRequires:	glibc-langpack-en
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(Test::Memory::Cycle)
BuildRequires:	perl(Test::More)

# We don't run the author tests when bootstrapping due to circular dependencies
# Test::Perl::Critic obviously pulls in Perl::Critic too
%if 0%{!?perl_bootstrap:1} && %{with perl_Perl_Critic_enables_extra_test}
BuildRequires:	perl(Devel::EnforceEncapsulation)
BuildRequires:	perl(Perl::Critic::Policy::Editor::RequireEmacsFileVariables)
BuildRequires:	perl(Perl::Critic::Policy::ErrorHandling::RequireUseOfExceptions)
BuildRequires:	perl(Perl::Critic::Policy::Miscellanea::RequireRcsKeywords)
BuildRequires:	perl(Test::Kwalitee) >= 1.15
BuildRequires:	perl(Test::Perl::Critic)
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.04
BuildRequires:	perl(Test::Without::Module)
%endif

# Optional/not automatically detected runtime dependencies
Requires:	hunspell >= 1.2.12
Requires:	perl(B::Keywords) >= 1.23
Requires:	perl(ExtUtils::Manifest)
Requires:	perl(File::Which)
Requires:	perl(Module::Pluggable) >= 3.1
Requires:	perl(PPI) >= 1.277
Requires:	perl(Term::ANSIColor) >= 2.02

Provides:       perl(Perl::Critic)
Provides:       perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitMagicNumbers)
Provides:       perl(Perl::Critic::Policy::NamingConventions::Capitalization)
%description
Perl::Critic is an extensible framework for creating and applying coding
standards to Perl source code. Essentially, it is a static source code
analysis engine. Perl::Critic is distributed with a number of
Perl::Critic::Policy modules that attempt to enforce various coding
guidelines. Most Policy modules are based on Damian Conway's book Perl
Best Practices. However, Perl::Critic is not limited to PBP and will
even support Policies that contradict Conway. You can enable, disable,
and customize those Polices through the Perl::Critic interface. You can
also create new Policy modules that suit your own tastes.

%package -n perl-Test-Perl-Critic-Policy
Summary:	A framework for testing your custom Policies
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:	perl(Test::Builder) >= 0.92

%description -n perl-Test-Perl-Critic-Policy
This module provides a framework for function-testing your custom
Perl::Critic::Policy modules. Policy testing usually involves feeding it a
string of Perl code and checking its behavior. In the old days, those strings
of Perl code were mixed directly in the test script. That sucked.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Perl-Critic-%{version}

# Switch spell checker tool from aspell to hunspell
%patch -P 0 -p1

# Fix shellbang in ppidump tool
%patch -P 3

# Drop exec bits from samples/docs to avoid dependency bloat
find tools examples -type f -exec chmod -c -x {} ';'

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
%if 0%{!?perl_bootstrap:1} && %{with perl_Perl_Critic_enables_extra_test}
LANG=en_US.UTF-8 ./Build authortest
%else
LANG=en_US.UTF-8 ./Build test
%endif

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README TODO.pod examples/ extras/ tools/
%{_bindir}/perlcritic
%{perl_vendorlib}/Perl/
%{_mandir}/man1/perlcritic.1*
%{_mandir}/man3/Perl::Critic*.3*

%files -n perl-Test-Perl-Critic-Policy
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Perl::Critic::Policy.3*

%changelog
%autochangelog
