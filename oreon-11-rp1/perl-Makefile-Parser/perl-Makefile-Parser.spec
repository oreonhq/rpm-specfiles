%global source0_hash fd4fbc691c73e143c332182ba48df47b580d4e12101200ca7625d9f63253fbd6

Name:           perl-Makefile-Parser
Version:        0.216
Release:        32%{?dist}
Summary:        Simple parser for Makefiles
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Makefile-Parser
Source0:        https://cpan.metacpan.org/authors/id/A/AG/AGENT/Makefile-Parser-%{version}.tar.gz
# Some support for GNU Make 4.0, CPAN RT#95979
Patch0:         Makefile-Parser-0.216-make-4.0-compatibility.patch
# Do not use a home directory into @INC, CPAN RT#107235
Patch1:         Makefile-Parser-0.216-Remove-use-lib.patch
# Do not use /usr/bin/env, CPAN RT#107237
Patch2:         Makefile-Parser-0.216-Do-not-use-usr-bin-env.patch
# Do not auto_install run-time only dependencies
Patch3:         Makefile-Parser-0.216-Disable-installing-dependencies-from-CPAN.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::TestBase)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Trigger) >= 0.13
# constant not used at tests
BuildRequires:  perl(Cwd)
# File::Slurp not used at tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::stat)
# Getopt::Long not used at tests
# Getopt::Std not used at tests
BuildRequires:  perl(IPC::Run3) >= 0.036
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MDOM::Document::Gmake)
BuildRequires:  perl(MDOM::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Spiffy)
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::Base::Filter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
# Test::Pod::Coverage not useful
Requires:       perl(Class::Trigger) >= 0.13
Requires:       perl(IPC::Run3) >= 0.036

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Class::Trigger|IPC::Run3)\\)$

%description
This is a simple parser for Makefiles. At this very early stage, the parser
only supports a limited set of features, so it may not recognize most of
the advanced features provided by certain make tools like GNU make. Its
initial purpose is to provide basic support for another module named
Makefile::GraphViz, which is aimed to render the building process specified
by a Makefile using the amazing GraphViz library. The Make module is not
satisfactory for this purpose, so I decided to build one of my own.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Makefile-Parser-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
# Remove bundled modules
rm -r ./inc
sed -i -e '/^inc\//d' MANIFEST
# Normalize end of lines
sed -i -e 's/\r$//' Changes
# This test does not support GNU make 4.0, CPAN RT#95979
rm t/makesimple.t
sed -i -e '/^t\/makesimple\.t/d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
# makesimple.t is disabled, see the %%prep section
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/makesimple
%{_bindir}/pgmake-db
%{_bindir}/plmake

%changelog
%autochangelog
