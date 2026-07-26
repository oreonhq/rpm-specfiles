%global source0_hash 9059074f7dc625a859452c850ccaeb4d14ecd5cc616dc31a01fb8c92366a498b

Name:           perl-POE-Component-SimpleDBI
Version:        1.31
Release:        33%{?dist}
Summary:        Asynchronous non-blocking DBI calls in POE made simple
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-SimpleDBI
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APOCAL/POE-Component-SimpleDBI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Data::Dumper not used at tests
BuildRequires:  perl(DBI) >= 1.30
BuildRequires:  perl(Error) >= 0.15
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Filter::Reference)
BuildRequires:  perl(POE::Session)
BuildRequires:  perl(POE::Wheel::Run)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
# Optional tests:
# CPAN::Meta not usefull
# Test::Apocalypse 1.000 needed only for author tests.
Requires:       perl(Data::Dumper)
Requires:       perl(warnings)

%description
This module works its magic by creating a new session with POE, then
spawning off a child process to do the "heavy" lifting. That way, your
main POE process can continue servicing other clients. Queries are put
into a queue, and processed one at a time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-SimpleDBI-%{version}
chmod a-x examples/*

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc README examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
