%global source0_hash c3460feb033a47d57b3c76d66547eb7f4e6772312798c7e8029e6aabaa678487
%global cpan_version 1.43
Name:           perl-MooseX-App
Version:        %(echo '%{cpan_version}' | sed 's/\(\...\)\(.\)/\1.\2/')
Release:        1%{?dist}
Summary:        Write user-friendly command line apps with even less suffering
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-App
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAROS/MooseX-App-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(I18N::Langinfo)
Requires:       perl(Moose) >= 2.00
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moose\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(I18N::Langinfo)
BuildRequires:  perl(IO::Interactive)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Pod::Elemental)
BuildRequires:  perl(Pod::Elemental::Selectors)
BuildRequires:  perl(Pod::Elemental::Transformer::Nester)
BuildRequires:  perl(Pod::Elemental::Transformer::Pod5)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Text::WagnerFischer)
BuildRequires:  perl(base)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
MooseX-App is a highly customisable helper to write user-friendly command
line applications without having to worry about most of the annoying things
usually involved. Just take any existing Moose class, add a single line
(use MooseX-App qw(PluginA PluginB ...);) and create one class for each
command in an underlying namespace. Options and positional parameters can
be defined as simple Moose accessors.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n MooseX-App-%{cpan_version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

unset APP_DEVELOPER
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
