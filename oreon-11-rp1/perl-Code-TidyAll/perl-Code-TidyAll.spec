%global source0_hash b902d6cd3ba30426d53c5bb7844f7860ffc57849bea25f24fd7af87a80eb63c1

Name:           perl-Code-TidyAll
Version:        0.85
Release:        3%{?dist}
Summary:        Engine for tidyall, your all-in-one code tidier and validator
# lib/Test/Code/TidyAll.pm:     GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:                      GPL-1.0-or-later OR Artistic-1.0-Perl
## Not in the binary package
# etc/editors/tidyall.el:       GPL-2.0-or-later
# node_modules/jshint/node_modules/cli/node_modules/glob/LICENSE:   BSD
# node_modules/js-beautify/node_modules/mkdirp/node_modules/minimist/LICENSE:  MIT
# php5/usr/share/php/PHP/CodeSniffer/Standards/PEAR/Docs/Commenting/FileCommentStandard.xml: MIT
# php5/usr/share/php/test/PHP_CodeSniffer/CodeSniffer/Standards/Squiz/Tests/Commenting/FileCommentUnitTest.js: PHP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Code-TidyAll
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Code-TidyAll-%{version}.tar.gz
Source1:        README.nodejs_plugins
# Replace deprecated aspell by hunspell
Patch0:         Code-TidyAll-0.83-Replace-aspell-by-hunspell.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config::INI::Reader)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(IPC::System::Simple)
# Not used for tests - perl(JSON::MaybeXS)
BuildRequires:  perl(List::Compare)
BuildRequires:  perl(List::SomeUtils)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Mason::Tidy)
# Not used for tests - perl(Mason::Tidy::App)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 2.000000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Parallel::ForkManager)
BuildRequires:  perl(Path::Tiny) >= 0.098
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Perl::Tidy::Sweetened)
BuildRequires:  perl(Pod::Checker)
BuildRequires:  perl(Pod::Spell)
BuildRequires:  perl(Pod::Tidy)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Specio) >= 0.40
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::Numeric)
BuildRequires:  perl(Specio::Library::Path::Tiny) >= 0.04
BuildRequires:  perl(Specio::Library::String)
# Not used for tests - perl(SVN::Look)
BuildRequires:  perl(Text::Diff) >= 1.44
# Not used for tests - perl(Test::Builder)
# Not used for tests - perl(Text::Diff)
# Not used for tests - perl(Text::Diff::Table)
# Not used for tests - perl(Text::ParseWords)
BuildRequires:  perl(Time::Duration::Parse)
BuildRequires:  perl(Try::Tiny)
# Tests
BuildRequires:  perl(autodie)
# Not used for tests - perl(Encode)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(lib::relative)
BuildRequires:  perl(Test::Class::Most)
# Not used for tests - perl(Test::CPAN::Meta::JSON)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings)

BuildRequires:  hunspell
Requires:       hunspell

Requires:       git
Requires:       nodejs
Requires:       perl(Getopt::Long)
Requires:       perl(Parallel::ForkManager) >= 1.19
Requires:       perl-Mason-Tidy
Requires:       perl-Perl-Critic
Requires:       php-pear-PHP-CodeSniffer
Requires:       subversion


Provides:       perl(Code::TidyAll)
Provides:       perl(Test::Code::TidyAll)
%description
This is the engine used by tidyall. You can call this API from your own
program instead of executing tidyall.

tidyall is all-in-one code tidier and validator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Code-TidyAll-%{version}
cp %{SOURCE1} .
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README.md README.nodejs_plugins CONTRIBUTING.md
%{_bindir}/tidyall
%{perl_vendorlib}/Code/*
%{perl_vendorlib}/Test/*
%{_mandir}/man1/tidyall*
%{_mandir}/man3/Code::TidyAll*
%{_mandir}/man3/Test::Code::TidyAll*

%changelog
%autochangelog
