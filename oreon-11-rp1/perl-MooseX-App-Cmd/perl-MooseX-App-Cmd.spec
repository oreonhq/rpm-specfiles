%global source0_hash f5e2f2ef129c388f2a3e36f53de598044af1b722e87d710529d05cc25d237ac2
Name:       perl-MooseX-App-Cmd
Version:    0.34
Release:        15%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Mashes up MooseX::Getopt and App::Cmd
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-App-Cmd-%{version}.tar.gz
Url:        https://metacpan.org/release/MooseX-App-Cmd
BuildArch:  noarch
Requires:   perl(App::Cmd) >= 0.321
Requires:   perl(App::Cmd::Command)
Requires:   perl(Getopt::Long::Descriptive) >= 0.091
Requires:   perl(Moose::Object)
Requires:   perl(MooseX::Getopt) >= 0.18
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Getopt::Long::Descriptive\\)$
# oreon:deps
BuildRequires:  perl(Any::Moose)
BuildRequires:  perl(App::Cmd)
BuildRequires:  perl(App::Cmd::Command)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Object)
BuildRequires:  perl(MooseX::ConfigFromFile)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(MooseX::NonMoose)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(YAML)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
