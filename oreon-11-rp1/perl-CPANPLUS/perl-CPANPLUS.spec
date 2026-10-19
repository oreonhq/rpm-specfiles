%global source0_hash e7ca8b4fb8e54f5a76f4cb920c9191932d337c075eeb909d7dc35b1bbf88c564
%global cpan_version 0.9916
Name:           perl-CPANPLUS
Version:        0.991.600
Release:        1%{?dist}
Summary:        Ameliorated interface to the Comprehensive Perl Archive Network
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPANPLUS
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/CPANPLUS-%{cpan_version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::Glob)
Requires:       perl(File::stat)
Requires:       perl(FindBin)
Requires:       perl(Module::CoreList) >= 2.22
Requires:       perl(Module::Pluggable)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Your::Module::Here|Test)\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Simple)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Fetch)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Log::Message)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Module::Loaded)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Object::Accessor)
BuildRequires:  perl(Package::Constants)
BuildRequires:  perl(Params::Check)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Term::UI)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

export HARNESS_OPTIONS=$(perl -e \
    'for (@ARGV) { $j=$1 if m/\A-j(\d+)\z/; }; print "j$j" if $j' -- \
    %{?_smp_mflags})
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
