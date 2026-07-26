%global source0_hash a2073aaa56827518174c3e9b0c7fba8c39d5a4d876b67a9fc0bb18729186c2cf

Name:           perl-Net-Appliance-Session
Version:        4.300005
Release:        21%{?dist}
Summary:        Run command-line sessions to network appliances
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Appliance-Session
Source0:        https://cpan.metacpan.org/authors/id/O/OL/OLIVER/Net-Appliance-Session-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Class::Load)
# Cwd not used at tests
# Data::Dumper not used at tests
# Getopt::Long not used at tests
# IO::Handle not used at tests
# IO::Prompt::Tiny not used at tests
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(Net::CLI::Interact) >= 2.300003
BuildRequires:  perl(Sub::Quote)
# Term::ANSIColor not used at tests
# Term::ReadPassword not used at tests
# Text::Glob not used at tests
# Text::ParseWords not used at tests
BuildRequires:  perl(Try::Tiny)
# Tests:
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Class::Load)
Requires:       perl(Net::CLI::Interact) >= 2.300003

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Net::CLI::Interact\\)$

%description
Use this module to establish an interactive command-line session with a
network appliance. There is special support for moving into "privileged"
mode and "configure" mode, along with the ability to send commands to the
connected device and retrieve returned output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Appliance-Session-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes examples
%{perl_vendorlib}/*
%{_bindir}/nas
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
