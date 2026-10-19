%global source0_hash 9059074f7dc625a859452c850ccaeb4d14ecd5cc616dc31a01fb8c92366a498b
Name:           perl-POE-Component-SimpleDBI
Version:        1.31
Release:        1%{?dist}
Summary:        Asynchronous non-blocking DBI calls in POE made simple
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-SimpleDBI
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APOCAL/POE-Component-SimpleDBI-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Data::Dumper)
Requires:       perl(warnings)
# oreon:deps
BuildRequires:  perl(DBI)
BuildRequires:  perl(Error)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Filter::Reference)
BuildRequires:  perl(POE::Session)
BuildRequires:  perl(POE::Wheel::Run)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
