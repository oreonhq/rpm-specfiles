%global source0_hash 43b33c20f8d82dba7cc48f8cd702f8fc9811e9d07880886dfd31b7077bd4a3a6
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
Patch0:         %{cpan_name}-7.36-USE_MM_LD_RUN_PATH.patch
Patch1:         %{cpan_name}-7.30-Link-to-libperl-explicitly-on-Linux.patch
Patch2:         %{cpan_name}-7.04-Unbundle-version.patch
Patch3:         %{cpan_name}-7.22-Unbundle-Encode-Locale.patch
Patch4:         %{cpan_name}-7.11-Provide-ExtUtils-MM-methods-as-standalone-ExtUtils-M.patch
BuildArch:      noarch
%if %{with perl_ExtUtils_MakeMaker_enables_optional_test}
%endif
Recommends:     perl(CPAN::Meta) >= 2.143240
Suggests:       perl(CPAN::Meta::Converter) >= 2.141170
Recommends:     perl(CPAN::Meta::Requirements) >= 2.130
Requires:       perl(Data::Dumper)
Requires:       perl(DynaLoader)
Requires:       perl(Encode)
%if !%{defined perl_bootstrap}
Recommends:     perl(Encode::Locale)
%endif
Requires:       perl(ExtUtils::Command) >= 1.19
Requires:       perl(ExtUtils::Install) >= 1.54
Requires:       perl(ExtUtils::Manifest) >= 1.70
Requires:       perl(File::Find)
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(Getopt::Long)
Suggests:       perl(JSON::PP)
Requires:       perl(Pod::Man)
Requires:       perl(POSIX)
Requires:       perl(Test::Harness)
Recommends:     perl(Time::HiRes)
Requires:       perl(Text::ParseWords)
Requires:       perl-ExtUtils-ParseXS
Recommends:     perl-devel
Recommends:     gcc
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)\s*$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DynaLoader|ExtUtils::MakeMaker::_version\\)
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
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(AutoSplit)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(base)
BuildRequires:  perl(less)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-ExtUtils-ParseXS
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles perl-ExtUtils-Command usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles perl-ExtUtils-MM-Utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-ExtUtils-Command -f %{oreon_filedir}/perl-ExtUtils-Command.list
%files -n perl-ExtUtils-MM-Utils -f %{oreon_filedir}/perl-ExtUtils-MM-Utils.list
%files -n perl-ExtUtils-MakeMaker-tests -f %{oreon_filedir}/perl-ExtUtils-MakeMaker-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.78-1
- Prepare for Oreon 11 (RP1)
