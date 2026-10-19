%global source0_hash b902d6cd3ba30426d53c5bb7844f7860ffc57849bea25f24fd7af87a80eb63c1
Name:           perl-Code-TidyAll
Version:        0.85
Release:        1%{?dist}
Summary:        Engine for tidyall, your all-in-one code tidier and validator
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Code-TidyAll
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Code-TidyAll-%{version}.tar.gz
Source1:        README.nodejs_plugins
Patch0:         Code-TidyAll-0.83-Replace-aspell-by-hunspell.patch
BuildArch:      noarch
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
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  hunspell
BuildRequires:  make
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config::INI::Reader)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(List::Compare)
BuildRequires:  perl(List::SomeUtils)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Mason::Tidy)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Parallel::ForkManager)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Perl::Tidy::Sweetened)
BuildRequires:  perl(Pod::Checker)
BuildRequires:  perl(Pod::Spell)
BuildRequires:  perl(Pod::Tidy)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Specio)
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::Numeric)
BuildRequires:  perl(Specio::Library::Path::Tiny)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Test::Class::Most)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(Time::Duration::Parse)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(lib::relative)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
