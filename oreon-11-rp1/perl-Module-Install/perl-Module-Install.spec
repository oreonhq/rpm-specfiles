%global source0_hash fbf91007f30565f3920e106055fd0d4287981d5e7dad8b35323ce4b733f15a7b
%bcond_with perl_Module_Install_enables_optional_test
Name:           perl-Module-Install
Version:        1.21
Release:        8%{?dist}
Summary:        Standalone, extensible Perl module installer
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Module-Install-%{version}.tar.gz
Patch0:         Module-Install-1.19-Fix-Perl-version-lookup-with-Module-CoreList.patch
BuildArch:      noarch
%if %{with perl_Module_Install_enables_optional_test} && 0%{!?perl_bootstrap:1}
%endif
Requires:       perl(Archive::Zip) >= 1.37
Requires:       perl(Carp)
Requires:       perl(CPAN)
Recommends:     perl(CPANPLUS::Backend)
Requires:       perl(Devel::PPPort) >= 3.16
Requires:       perl(ExtUtils::MakeMaker) >= 6.59
Requires:       perl(ExtUtils::MM_Unix)
Requires:       perl(File::Remove) >= 1.42
Requires:       perl(File::Spec) >= 3.28
Requires:       perl(File::Temp)
Requires:       perl(FileHandle)
Requires:       perl(FindBin)
Requires:       perl(Module::Build) >= 0.29
Requires:       perl(Module::CoreList) >= 2.17
Requires:       perl(Module::ScanDeps) >= 1.09
Requires:       perl(Parse::CPAN::Meta) >= 1.4413
Requires:       perl(Socket)
Requires:       perl(YAML::Tiny) >= 1.38
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::PPPort\\)$
%global __requires_exclude %__requires_exclude|^perl\\(ExtUtils::MakeMaker\\)$
%global __requires_exclude %__requires_exclude|^perl\\(File::Remove\\)$
%global __requires_exclude %__requires_exclude|^perl\\(File::Spec\\)$
%global __requires_exclude %__requires_exclude|^perl\\(YAML::Tiny\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %__requires_exclude|^perl\\(MyTest\\)$
Provides:       perl(Module::Install)
Provides:       perl(Module::Install::AutoInstall)
Provides:       perl(Module::Install::Base)
Provides:       perl(Module::Install::Can)
Provides:       perl(Module::Install::Makefile)
Provides:       perl(Module::Install::Metadata)
Provides:       perl(Module::Install::Win32)
Provides:       perl(Module::Install::WriteAll)
Provides:       perl(Module::Install::Include)
Provides:       perl(inc::Module::Install)
Provides:       perl(Module::Install::Include)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(ExtUtils::MM)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Remove)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::ScanDeps)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML::Tiny)
BuildRequires:  perl(autodie)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Module::Install is a package for writing installers for CPAN (or CPAN-like)
distributions that are clean, simple, minimalist, act in a strictly correct
manner with ExtUtils::MakeMaker, and will run on any Perl installation
version 5.005 or newer.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Module_Install_enables_optional_test} && 0%{!?perl_bootstrap:1}
Requires:       perl(Module::Install::AuthorTests)
Requires:       perl(Module::Install::ExtraTests) >= 0.007
%endif
Requires:       perl(utf8)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Install-%{version}
%patch -P0 -p1
# Help generators to recognize Perl scripts
for F in `find t -name *.t`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
rm -f %{buildroot}/blib/lib/auto/share/dist/Module-Install/dist_file.txt
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Module-Install-tests -f %{oreon_filedir}/perl-Module-Install-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.21-8
- Prepare for Oreon 11 (RP1)
