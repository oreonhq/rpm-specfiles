%global source0_hash e7ca8b4fb8e54f5a76f4cb920c9191932d337c075eeb909d7dc35b1bbf88c564

%global cpan_version 0.9916
Name:           perl-CPANPLUS
Version:        0.991.600
Release:        3%{?dist}
Summary:        Ameliorated interface to the Comprehensive Perl Archive Network
# Other files:                              GPL-1.0-or-later OR Artistic-1.0-Perl
## Unbundled, not used
# inc/bundle/Locale/Maketext/Simple.pm:     MIT
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPANPLUS
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/CPANPLUS-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Module::Loaded)
# Run-time:
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Simple)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Fetch)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Log::Message)
BuildRequires:  perl(Module::CoreList) >= 2.22
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Object::Accessor)
BuildRequires:  perl(overload)
BuildRequires:  perl(Package::Constants)
BuildRequires:  perl(Params::Check)
# Parse::CPAN::Meta also for loading t/testrules.yml at tests
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Term::UI)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
# lib/CPANPLUS/Internals.pm:465
Requires:       perl(File::Glob)
# File::Path not found in lib/CPANPLUS/Internals/Utils.pm:68 and
# generated from lib/CPANPLUS/Internals/Extract.pm
# lib/CPANPLUS/Internals/Utils.pm:323
Requires:       perl(File::stat)
# bin/cpanp-boxed:10
Requires:       perl(FindBin)
# lib/CPANPLUS/Module.pm:477
Requires:       perl(Module::CoreList) >= 2.22
# lib/CPANPLUS/Configure.pm:181
Requires:       perl(Module::Pluggable)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Your::Module::Here|Test)\\)

%description
The CPANPLUS library is an API to the CPAN mirrors and a collection of
interactive shells, command line programs, etc., that use this API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPANPLUS-%{cpan_version}
# Removed unused bootstrap modules (required only when updating CPANPLUS with
# CPANPLUS when Module::Build is preferred by CPANPLUS)
rm -rf bundled
perl -i -ne 'print $_ unless m{^bundled/}' MANIFEST
# Remove bundled modules
rm -rf inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
export HARNESS_OPTIONS=$(perl -e \
    'for (@ARGV) { $j=$1 if m/\A-j(\d+)\z/; }; print "j$j" if $j' -- \
    %{?_smp_mflags})
make test

%files
%doc ChangeLog README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
