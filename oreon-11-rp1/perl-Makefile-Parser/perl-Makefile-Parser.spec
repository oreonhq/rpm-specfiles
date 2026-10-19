%global source0_hash fd4fbc691c73e143c332182ba48df47b580d4e12101200ca7625d9f63253fbd6
Name:           perl-Makefile-Parser
Version:        0.216
Release:        32%{?dist}
Summary:        Simple parser for Makefiles
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Makefile-Parser
Source0:        https://cpan.metacpan.org/authors/id/A/AG/AGENT/Makefile-Parser-%{version}.tar.gz
Patch0:         Makefile-Parser-0.216-make-4.0-compatibility.patch
Patch1:         Makefile-Parser-0.216-Remove-use-lib.patch
Patch2:         Makefile-Parser-0.216-Do-not-use-usr-bin-env.patch
Patch3:         Makefile-Parser-0.216-Disable-installing-dependencies-from-CPAN.patch
BuildArch:      noarch
Requires:       perl(Class::Trigger) >= 0.13
Requires:       perl(IPC::Run3) >= 0.036
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Class::Trigger|IPC::Run3)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Trigger)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MDOM::Document::Gmake)
BuildRequires:  perl(MDOM::Util)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::TestBase)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Spiffy)
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::Base::Filter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
