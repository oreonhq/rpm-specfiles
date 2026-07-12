%global source0_hash 43b33c20f8d82dba7cc48f8cd702f8fc9811e9d07880886dfd31b7077bd4a3a6

# Run optional test
%bcond_without perl_ExtUtils_MakeMaker_enables_optional_test

%global cpan_name ExtUtils-MakeMaker

Name:           perl-%{cpan_name}
Epoch:          2
Version:        7.78
Release:        1%{?dist}
Summary:        Create a module Makefile
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/%{cpan_name}-%{version}.tar.gz
# Do not set RPATH to perl shared-library modules by default. Bug #773622.
# This is copy from `perl' package. This is a distributor extension.
Patch0:         %{cpan_name}-7.36-USE_MM_LD_RUN_PATH.patch
# Link to libperl.so explicitly. Bug #960048.
Patch1:         %{cpan_name}-7.30-Link-to-libperl-explicitly-on-Linux.patch
# Unbundle version modules
Patch2:         %{cpan_name}-7.04-Unbundle-version.patch
# Unbundle Encode::Locale module
Patch3:         %{cpan_name}-7.22-Unbundle-Encode-Locale.patch
# Provide maybe_command independently, bug #1129443
Patch4:         %{cpan_name}-7.11-Provide-ExtUtils-MM-methods-as-standalone-ExtUtils-M.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# Makefile.Pl uses ExtUtils::MakeMaker from ./lib
# B needed only for CPAN::Meta::Requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
# CPAN::Meta::Requirements has a fallback
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# If an XS module is compiled, xsubpp(1) is needed
BuildRequires:  perl-ExtUtils-ParseXS
# Tests:
BuildRequires:  perl(AutoSplit)
BuildRequires:  perl(base)
BuildRequires:  perl(CPAN::Meta) >= 2.143240
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Install) >= 1.52
# ExtUtils::Installed not used at tests
BuildRequires:  perl(ExtUtils::Manifest) >= 1.70
# ExtUtils::Packlist not used at tests
# ExtUtils::XSSymSet is not needed (VMS only)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp) >= 0.22
BuildRequires:  perl(Getopt::Long)
# IO::File not used at tests
# IO::Handle not used
BuildRequires:  perl(less)
BuildRequires:  perl(overload)
BuildRequires:  perl(Parse::CPAN::Meta) >= 1.4414
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
# threads::shared not used
BuildRequires:  perl(utf8)
# XSLoader not used
%if %{with perl_ExtUtils_MakeMaker_enables_optional_test}
# Optional tests
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(PerlIO)
# Keep YAML optional
# Keep YAML::Tiny optional
%endif
Recommends:     perl(CPAN::Meta) >= 2.143240
Suggests:       perl(CPAN::Meta::Converter) >= 2.141170
# CPAN::Meta::Requirements to support version ranges
Recommends:     perl(CPAN::Meta::Requirements) >= 2.130
Requires:       perl(Data::Dumper)
Requires:       perl(DynaLoader)
# Encode is needed for producing POD with =encoding statement correctly
Requires:       perl(Encode)
%if !%{defined perl_bootstrap}
Recommends:     perl(Encode::Locale)
%endif
Requires:       perl(ExtUtils::Command) >= 1.19
Requires:       perl(ExtUtils::Install) >= 1.54
Requires:       perl(ExtUtils::Manifest) >= 1.70
# ExtUtils::XSSymSet is not needed (VMS only)
Requires:       perl(File::Find)
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(Getopt::Long)
Suggests:       perl(JSON::PP)
# Optional Pod::Man is needed for generating manual pages from POD
Requires:       perl(Pod::Man)
Requires:       perl(POSIX)
Requires:       perl(Test::Harness)
Recommends:     perl(Time::HiRes)
Requires:       perl(Text::ParseWords)
# VMS::Filespec is not needed (VMS only)
# Win32 is not needed (Win32 only)
# If an XS module is compiled, xsubpp(1) is needed
Requires:       perl-ExtUtils-ParseXS
# These dependencies are weak in order to relieve building noarch
# packages from perl-devel and gcc. See bug #1547165.
# If an XS module is built, code generated from XS will be compiled and it
# includes Perl header files.
Recommends:     perl-devel
# If an XS module is built, the generated Makefile executes gcc.
Recommends:     gcc

# Do not export underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)\s*$
# Do not export private redefinitions
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DynaLoader|ExtUtils::MakeMaker::_version\\)

# Filter modules bundled for tests
%global __requires_exclude %{__requires_exclude}|^perl\\(MY)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(TieIn)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(TieOut)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(MakeMaker::Test.*)\s*$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

Provides:       perl(ExtUtils::MakeMaker::Config)
Provides:       perl(ExtUtils::Command::MM)
Provides:       perl(ExtUtils::MM_Any)
Provides:       perl(ExtUtils::MM_Unix)
Provides:       perl(ExtUtils::MY)
Provides:       perl(ExtUtils::Mkbootstrap)
Provides:       perl(ExtUtils::Mksymlists)
Provides:       perl(ExtUtils::testlib)
%description
This utility is designed to write a Makefile for an extension module from a
Makefile.PL. It is based on the Makefile.SH model provided by Andy
Dougherty and the perl5-porters.

%package -n perl-ExtUtils-Command
Summary:        Perl routines to replace common UNIX commands in Makefiles
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(File::Copy)
Requires:       perl(File::Find)
Requires:       perl(File::Path)
# File::Spec not used
# VMS::Feature not used

%description -n perl-ExtUtils-Command
This Perl module is used to replace common UNIX commands. In all cases the
functions work with @ARGV rather than taking arguments. This makes them
easier to deal with in Makefiles.

%package -n perl-ExtUtils-MM-Utils
Summary:        ExtUtils::MM methods without dependency on ExtUtils::MakeMaker
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch

%description -n perl-ExtUtils-MM-Utils
This is a collection of ExtUtils::MM subroutines that are used by many
other modules but that do not need full-featured ExtUtils::MakeMaker. The
issue with ExtUtils::MakeMaker is it pulls in Perl header files and that
is an overkill for small subroutines.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(CPAN::Meta) >= 2.143240
Requires:       perl(Encode)
Requires:       perl(File::Spec)
Requires:       perl(Parse::CPAN::Meta) >= 1.4414
Requires:       perl(Pod::Man)
Requires:       perl(version)
%if %{with perl_ExtUtils_MakeMaker_enables_optional_test}
# Optional tests
Requires:       perl-devel
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(PerlIO)
%endif

%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n ExtUtils-MakeMaker-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
# Remove bundled modules
rm -rf bundled
perl -i -ne 'print $_ unless m{^bundled/}' MANIFEST
rm -rf t/lib/Test
perl -i -ne 'print $_ unless m{^t/lib/Test/}' MANIFEST
rm -rf lib/ExtUtils/MakeMaker/version{,.pm}
perl -i -ne 'print $_ unless m{^lib/ExtUtils/MakeMaker/version(?:/|\.pm)}' MANIFEST
rm -rf lib/ExtUtils/MakeMaker/Locale.pm
perl -i -ne 'print $_ unless m{^lib/ExtUtils/MakeMaker/Locale\.pm}' MANIFEST

%if !%{with perl_ExtUtils_MakeMaker_enables_optional_test}
# Remove optional tests
rm t/02-xsdynamic.t t/03-xsstatic.t
perl -i -ne 'print $_ unless m{^t/02-xsdynamic\.t}' MANIFEST
perl -i -ne 'print $_ unless m{^t/03-xsstatic\.t}' MANIFEST
perl -i -ne 'print $_ unless m{^t/unicode\.t}' MANIFEST
%endif

# Help file to recognise the Perl scripts and normalize shebangs
for F in `find t -name *.t`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
BUILDING_AS_PACKAGE=1 perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Lots of tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%{_fixperms} %{buildroot}/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes CONTRIBUTING README
%{_bindir}/*
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/ExtUtils/Command.pm
%exclude %dir %{perl_vendorlib}/ExtUtils/MM
%exclude %{perl_vendorlib}/ExtUtils/MM/Utils.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
%exclude %{_mandir}/man3/ExtUtils::Command.*
%exclude %{_mandir}/man3/ExtUtils::MM::Utils.*

%files -n perl-ExtUtils-Command
%dir %{perl_vendorlib}/ExtUtils
%{perl_vendorlib}/ExtUtils/Command.pm
%{_mandir}/man3/ExtUtils::Command.*

%files -n perl-ExtUtils-MM-Utils
%dir %{perl_vendorlib}/ExtUtils
%dir %{perl_vendorlib}/ExtUtils/MM
%{perl_vendorlib}/ExtUtils/MM/Utils.pm
%{_mandir}/man3/ExtUtils::MM::Utils.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.78-1
- Prepare for Oreon 11 (RP1)
