%global source0_hash cf04c028a590b1f324850736bfc2e5efa44538a91571d8bf29f9a1b48f0069a9

Name:           perl-Shipwright
Version:        2.4.42
Release:        25%{?dist}
Summary:        Build and Manage Self-contained Software Bundle
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Shipwright
Source0:        https://cpan.metacpan.org/authors/id/S/SU/SUNNAVY/Shipwright-%{version}.tar.gz
# Drop useless build-time feautures
Patch0:         Shipwright-2.4.41-Disable-author-test-and-network-installation-when-bu.patch
# Use real interpreter path instead of /usr/bin/env trampoline
Patch1:         Shipwright-2.4.41-Do-not-use-usr-bin-env.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install) >= 0.76
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::Share)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
# Algorithm::Dependency::Ordered not used at tests
# Algorithm::Dependency::Source::HoA not used at tests
BuildRequires:  perl(App::CLI)
# 0.47 is broken, fixed in 0.48
BuildConflicts: perl(App::CLI) = 0.47
BuildRequires:  perl(App::CLI::Command)
BuildRequires:  perl(App::CLI::Command::Help)
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Config)
BuildRequires:  perl(CPAN) >= 1.9205
# CPAN::Config is optional
BuildRequires:  perl(CPAN::DistnameInfo)
# CPAN::MyConfig is optional
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
# File::Compare not used at tests
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(File::Slurp)
# File::Spec not used at tests
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp) >= 0.18
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Log::Log4perl)
# LWP::UserAgent not used at tests
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Info)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
# Tie::File not used at tests
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(version)
BuildRequires:  perl(YAML::Tiny)
Requires:       perl(Algorithm::Dependency::Ordered)
Requires:       perl(Algorithm::Dependency::Source::HoA)
Requires:       perl(CPAN) >= 1.9205
Requires:       perl(File::Compare)
Requires:       perl(File::Path) >= 2.07
Requires:       perl(File::Temp) >= 0.18
Requires:       perl(LWP::UserAgent)
Requires:       perl(Test::More)
Requires:       perl(Tie::File)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Path|File::Temp)\\)$

%description
Shipwright is a tool to help you bundle your software with all its dependencies,
regardless of whether they are CPAN modules or non-Perl modules from elsewhere.
Shipwright makes the bundle work easy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Shipwright-%{version}
%patch -P0 -p1
%patch -P1 -p1
# Remove bundled modules
rm -rf ./inc
sed -i -e '/^inc\//d' MANIFEST
# Fix shellbangs unnoticed by build script
sed -i -e 's|#!perl|%(perl -MConfig -e 'print $Config{startperl}')|' \
    share/bin/* share/etc/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test %{?_smp_mflags}

%files
%doc AUTHORS Changes README TODO
%{_bindir}/shipwright*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
