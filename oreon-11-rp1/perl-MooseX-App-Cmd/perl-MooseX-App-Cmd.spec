%global source0_hash f5e2f2ef129c388f2a3e36f53de598044af1b722e87d710529d05cc25d237ac2

Name:       perl-MooseX-App-Cmd
Version:    0.34
Release:    15%{?dist}
# see lib/MooseX/App/Cmd.pm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Mashes up MooseX::Getopt and App::Cmd
Source:     https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-App-Cmd-%{version}.tar.gz
Url:        https://metacpan.org/release/MooseX-App-Cmd
BuildArch:  noarch

BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Module::Build::Tiny)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)

# Run-time:
BuildRequires: perl(Any::Moose)
BuildRequires: perl(App::Cmd) >= 0.321
BuildRequires: perl(App::Cmd::Command)
BuildRequires: perl(English)
BuildRequires: perl(File::Basename)
BuildRequires: perl(Getopt::Long::Descriptive) >= 0.091
# any_moose('::Object')
BuildRequires: perl(Moose::Object)
BuildRequires: perl(MooseX::NonMoose)
# any_moose('X::Getopt')
BuildRequires: perl(MooseX::Getopt) >= 0.18
BuildRequires: perl(namespace::clean)

# Tests:
BuildRequires: perl(base)
BuildRequires: perl(Carp)
BuildRequires: perl(CPAN::Meta) >= 2.120900
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(lib)
BuildRequires: perl(Moose) >= 0.86
BuildRequires: perl(MooseX::ConfigFromFile)
BuildRequires: perl(Pod::Coverage::TrustPod)
BuildRequires: perl(Test::EOL)
BuildRequires: perl(Test::Kwalitee) >= 1.21
BuildRequires: perl(Test::CPAN::Changes)
BuildRequires: perl(Test::CPAN::Meta)
BuildRequires: perl(Test::More) >= 0.94
BuildRequires: perl(Test::NoTabs)
BuildRequires: perl(Test::Pod) >= 1.41
BuildRequires: perl(Test::Pod::Coverage) >=  1.08
BuildRequires: perl(YAML)

BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Output)

# we don't pick up Moose keywords automagically yet
Requires:   perl(App::Cmd) >= 0.321
Requires:   perl(App::Cmd::Command)
Requires:   perl(Getopt::Long::Descriptive) >= 0.091
# any_moose('::Object')
Requires:   perl(Moose::Object)
# any_moose('X::Getopt')
Requires:   perl(MooseX::Getopt) >= 0.18

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Getopt::Long::Descriptive\\)$

%description
This package marries App::Cmd with MooseX::Getopt.

Use it like the App::Cmd man-page advises (especially see the
App::Cmd::Tutorial man-page), swapping App::Cmd::Command for
MooseX::App::Cmd::Command.

Then you can write your commands as Moose classes, with the
MooseX::Getopt defining the options for you instead of 'opt_spec'
returning a Getopt::Long::Descriptive spec.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-App-Cmd-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%check
./Build test

%files
%doc Changes README
%license LICENCE
%{perl_vendorlib}/MooseX
%{_mandir}/man3/MooseX::*.3*

%changelog
%autochangelog
