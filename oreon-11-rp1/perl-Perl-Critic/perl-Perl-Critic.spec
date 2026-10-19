%global source0_hash 572a7c8758ba1c0ab6daf0bd40297c4f0dcf1516f084522df2c2bf04d525e232
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_with perl_Perl_Critic_enables_extra_test
Name:		perl-Perl-Critic
Version:	1.156
Release:        1%{?dist}
Summary:        Critique Perl source code for best-practices
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Perl-Critic
Source0:        https://cpan.metacpan.org/modules/by-module/Perl/Perl-Critic-%{version}.tar.gz
Patch0:		0001-Change-default-spell-check-tool-from-aspell-to-hunsp.patch
Patch3:		Perl-Critic-1.136-ppidump-shellbang.patch
BuildArch:	noarch
%if 0%{!?perl_bootstrap:1} && %{with perl_Perl_Critic_enables_extra_test}
%endif
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
Provides:       perl(Perl::Critic::Utils)
Provides:       perl(Perl::Critic::Violation)
Provides:       perl(Perl::Critic::Policy::Editor::RequireEmacsFileVariables)
Provides:       perl(Perl::Critic::Policy::ErrorHandling::RequireUseOfExceptions)
Provides:       perl(Perl::Critic::Policy::Lax::ProhibitStringyEval::ExceptForRequire)
Provides:       perl(Perl::Critic::Policy::Miscellanea::RequireRcsKeywords)
Provides:       perl(Perl::Critic::Policy)
Provides:       perl(Perl::Critic::Utils::PPI)
Provides:       perl(Perl::Critic::Policy::Modules::ProhibitModuleShebang)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-langpack-en
BuildRequires:  hunspell
BuildRequires:  hunspell-en
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(B::Keywords)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(English)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::SomeUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(PPI)
BuildRequires:  perl(PPIx::QuoteLike)
BuildRequires:  perl(PPIx::Regexp)
BuildRequires:  perl(PPIx::Regexp::Util)
BuildRequires:  perl(PPIx::Utils::Traversal)
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Pod::PlainText)
BuildRequires:  perl(Pod::Select)
BuildRequires:  perl(Pod::Spell)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(String::Format)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles perl-Test-Perl-Critic-Policy usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if 0%{!?perl_bootstrap:1} && %{with perl_Perl_Critic_enables_extra_test}
LANG=en_US.UTF-8 ./Build authortest
%else
LANG=en_US.UTF-8 ./Build test
%endif
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-Perl-Critic-Policy -f %{oreon_filedir}/perl-Test-Perl-Critic-Policy.list

%changelog

%autochangelog
