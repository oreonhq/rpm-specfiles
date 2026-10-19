%global source0_hash 4b2799f478cca0bd9c980f748b0625df627ee3d203b39f00f8b469a0ab39605c
Name:		perl-Perl-PrereqScanner-NotQuiteLite
Version:	0.9918
Release:        2%{?dist}
Summary:        A tool to scan your Perl code for its prerequisites
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Perl-PrereqScanner-NotQuiteLite
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/Perl-PrereqScanner-NotQuiteLite-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(Data::Dump)
Requires:	perl(JSON::PP)
Requires:	perl(Module::CoreList)
Requires:	perl(Module::Find)
Suggests:	perl(CPAN::Common::Index)
Provides:       perl(Perl::PrereqScanner::NotQuiteLite)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::MakeMaker::CPANfile)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Module::CPANfile)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(Parse::Distname)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Regexp::Trie)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::UseAllModules)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
