%global source0_hash d15b17241a07fed11ed4a917bbe00d2317e94ac52ac38ee92a9cacbb346adb16

%global cpan_version 0.998003

Name:           perl-App-cpm
Version:        0.998.3
Release:        2%{?dist}
Summary:        Fast CPAN module installer
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/App-cpm
Source0:        https://cpan.metacpan.org/authors/id/S/SK/SKAJI/App-cpm-%{cpan_version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Module::Build::Tiny) >= 0.051
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
# None of them are used at tests.
# BuildRequires:  gzip
# BuildRequires:  perl(Archive::Tar)
# BuildRequires:  perl(Archive::Zip) >= 1.68
# BuildRequires:  perl(Carton::Snapshot)
# BuildRequires:  perl(Command::Runner) >= 0.100
# BuildRequires:  perl(Config)
# BuildRequires:  perl(constant)
# BuildRequires:  perl(CPAN::02Packages::Search) >= 0.100
# BuildRequires:  perl(CPAN::DistnameInfo)
# BuildRequires:  perl(CPAN::Meta)
# BuildRequires:  perl(CPAN::Meta::Prereqs)
# BuildRequires:  perl(CPAN::Meta::Requirements)
# BuildRequires:  perl(CPAN::Meta::YAML)
# BuildRequires:  perl(Cwd)
# BuildRequires:  perl(Darwin::InitObjC)
# BuildRequires:  perl(Digest::MD5)
# BuildRequires:  perl(Exporter)
# BuildRequires:  perl(ExtUtils::Config)
# BuildRequires:  perl(ExtUtils::Helpers)
# BuildRequires:  perl(ExtUtils::Install) >= 2.20
# BuildRequires:  perl(ExtUtils::InstallPaths) >= 0.002
# BuildRequires:  perl(File::Basename)
# BuildRequires:  perl(File::Copy)
# BuildRequires:  perl(File::Copy::Recursive)
# BuildRequires:  perl(File::Find)
# BuildRequires:  perl(File::HomeDir)
# BuildRequires:  perl(File::Path)
# BuildRequires:  perl(File::pushd)
# BuildRequires:  perl(File::Spec)
# BuildRequires:  perl(File::Spec::Functions)
# BuildRequires:  perl(File::Temp)
# BuildRequires:  perl(File::Which)
# BuildRequires:  perl(Getopt::Long)
# BuildRequires:  perl(HTTP::Tiny)
# BuildRequires:  perl(HTTP::Tinyish) >= 0.12
# BuildRequires:  perl(HTTP::Tinyish::Base)
# BuildRequires:  perl(IO::Handle)
# BuildRequires:  perl(IPC::Run3)
# BuildRequires:  perl(JSON::PP) >= 2.27300
# BuildRequires:  perl(List::Util)
# BuildRequires:  perl(Module::CoreList)
# BuildRequires:  perl(Module::CPANfile)
# BuildRequires:  perl(Module::cpmfile) >= 0.001
# BuildRequires:  perl(Module::Metadata)
# BuildRequires:  perl(Parse::LocalDistribution)
# BuildRequires:  perl(Parallel::Pipes::App) >= 0.100
# BuildRequires:  perl(parent)
# BuildRequires:  perl(Pod::Text)
# BuildRequires:  perl(POSIX)
# BuildRequires:  perl(Proc::ForkSafe) >= 0.001
# BuildRequires:  perl(Time::HiRes)
# BuildRequires:  perl(version)
# BuildRequires:  perl(YAML::PP) >= 0.026
# Tests only
BuildRequires:  perl(Test::More)
Requires:       gzip
Requires:       perl(Archive::Tar)
Requires:       perl(Archive::Zip) >= 1.68
Requires:       perl(Command::Runner) >= 0.100
Requires:       perl(ExtUtils::Install) >= 2.20
Requires:       perl(File::HomeDir)
Requires:       perl(HTTP::Tinyish) >= 0.12
Requires:       perl(JSON::PP) >= 2.27300
Requires:       perl(Module::CoreList)
Requires:       perl(Module::cpmfile) >= 0.001
Requires:       perl(Parallel::Pipes::App) >= 0.100
Requires:       perl(Parse::PMFile) >= 0.43
Requires:       perl(Pod::Man)
Requires:       perl(TAP::Harness::Env)
Requires:       perl(YAML::PP) >= 0.026
Suggests:       perl(Carton::Snapshot)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(JSON::PP\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Command::Runner\\)$
%global __requires_exclude %__requires_exclude|^perl\\(ExtUtils::Install\\)$
%global __requires_exclude %__requires_exclude|^perl\\(ExtUtils::InstallPaths\\)$
%global __requires_exclude %__requires_exclude|^perl\\(HTTP::Tinyish\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Module::cpmfile\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Parallel::Pipes::App\\)$
%global __requires_exclude %__requires_exclude|^perl\\(YAML::PP\\)$

%description
cpm is a fast CPAN module installer.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-cpm-%{cpan_version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot}%{_mandir} -type f -empty -delete
# Correct permissions
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes
%{_bindir}/cpm
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/cpm
%{perl_vendorlib}/App/cpm.pm
%{_mandir}/man1/cpm.*
%{_mandir}/man3/App::cpm.*
%{_mandir}/man3/App::cpm::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
