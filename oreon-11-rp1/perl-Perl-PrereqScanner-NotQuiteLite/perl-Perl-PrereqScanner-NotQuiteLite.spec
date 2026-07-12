%global source0_hash 4b2799f478cca0bd9c980f748b0625df627ee3d203b39f00f8b469a0ab39605c

Name:		perl-Perl-PrereqScanner-NotQuiteLite
Version:	0.9918
Release:	1%{?dist}
Summary:	A tool to scan your Perl code for its prerequisites
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Perl-PrereqScanner-NotQuiteLite
Source0:	https://cpan.metacpan.org/modules/by-module/Perl/Perl-PrereqScanner-NotQuiteLite-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(ExtUtils::MakeMaker::CPANfile) >= 0.08
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(CPAN::Meta::Prereqs)
BuildRequires:	perl(CPAN::Meta::Requirements)
BuildRequires:	perl(Data::Dump)
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Glob)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(JSON::PP)
BuildRequires:	perl(Module::CoreList)
BuildRequires:	perl(Module::CPANfile) >= 1.1004
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(parent)
BuildRequires:	perl(Parse::Distname)
BuildRequires:	perl(Regexp::Trie)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Script Runtime
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(lib)
BuildRequires:	perl(Pod::Usage)
# Test Suite
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(if)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::UseAllModules)
# Dependencies
Requires:	perl(Data::Dump)
Requires:	perl(JSON::PP)
Requires:	perl(Module::CoreList)
Requires:	perl(Module::Find)
Suggests:	perl(CPAN::Common::Index)

Provides:       perl(Perl::PrereqScanner::NotQuiteLite)
%description
Perl::PrereqScanner::NotQuiteLite is yet another prerequisites scanner. It
passes almost all the scanning tests for Perl::PrereqScanner and
Module::ExtractUse (i.e. except for a few dubious ones), and runs slightly
faster than PPI-based Perl::PrereqScanner. However, it doesn't run as fast as
Perl::PrereqScanner::Lite (which uses an XS lexer).

Perl::PrereqScanner::NotQuiteLite also recognizes eval. Prerequisites in eval
are not considered as requirements, but you can collect them as suggestions.

Conditional requirements or requirements loaded in a block are treated as
recommends. No-ed modules are stored separately (since 0.94). You may or may
not need to merge them into requires.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Perl-PrereqScanner-NotQuiteLite-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
%make_build

%install
%make_install
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/scan-perl-prereqs-nqlite
%{perl_vendorlib}/Perl/
%{_mandir}/man1/scan-perl-prereqs-nqlite.1*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::App.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Context.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::Aliased.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::AnyMoose.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::Autouse.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::Catalyst.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::ClassAccessor.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::ClassAutouse.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::ClassLoad.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::Core.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::FeatureCompatClass.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::Inline.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::KeywordDeclare.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::Later.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::Mixin.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::ModuleRuntime.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::MojoBase.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::Moose.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::MooseXDeclare.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::ObjectPad.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::Only.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::POE.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::PackageVariant.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::Plack.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::Prefork.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::Superclass.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::Syntax.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::SyntaxCollector.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::TestClassMost.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::TestMore.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::TestRequires.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::UniversalVersion.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Parser::Unless.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Tokens.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Util.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Util::CPANfile.3*
%{_mandir}/man3/Perl::PrereqScanner::NotQuiteLite::Util::Prereqs.3*

%changelog
%autochangelog
