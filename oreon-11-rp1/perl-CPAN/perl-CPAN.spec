%global source0_hash 5b337c9e0e6f037c16c3ba01c0b758600647a83de4a5e78e41a5cc26ee68a1ee

# Don not run gnupg1 tests by default, they need network access
# (Socket::inet_aton('pool.sks-keyservers.net')).
%bcond_with perl_CPAN_enables_gnupg_test
# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_CPAN_enables_optional_test
%else
%bcond_with perl_CPAN_enables_optional_test
%endif

Name:           perl-CPAN
Version:        2.38
Release:        522%{?dist}
Summary:        Query, download and build perl modules from CPAN sites
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANDK/CPAN-2.38.tar.gz
# Create site paths for the first time, bug #1158873, CPAN RT#99905
Patch0:         CPAN-2.18-Attemp-to-create-site-library-directories-on-first-t.patch
# Change configuration directory name
Patch1:         CPAN-2.18-Replace-configuration-directory-string-with-a-marke.patch
# Only require config for CPAN shell operations
Patch2:         CPAN-2.38-Only-require-config-for-CPAN-shell-operations.patch
# Update man page to provide notes about first run, GH issue #194
Patch3:         CPAN-2.38-Add-notes-about-first-configuration.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
# Module::Signature not used
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Optional:
BuildRequires:  perl(File::Spec)
# YAML::Syck is not used because @ST_PREFS is empty in Makefile.PL

# Run-time:
# Prefer Archive::Tar and Compress::Zlib over tar and gzip
BuildRequires:  perl(Archive::Tar) >= 1.50
%if !%{defined perl_bootstrap}
# Prefer Archive::Zip over unzip
BuildRequires:  perl(Archive::Zip)
%endif
BuildRequires:  perl(autouse)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
# Devel::Size not used at tests
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Dumpvalue)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
# ExtUtils::Manifest not used at tests
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
# File::HomeDir 0.65 not used at tests
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp) >= 0.16
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Std)
# HTTP::Date is optional, prefer in-core Time::Local
# HTTP::Request is optional
BuildRequires:  perl(HTTP::Tiny) >= 0.005
BuildRequires:  perl(if)
# IO::Socket::SSL 1.56 is optional
# YAML::XS or YAML::Syck or JSON::PP, we already use YAML::Syck at a different
# place, keep JSON::PP optional
BuildRequires:  perl(lib)
# local::lib is optional
# LWP is optional, prefer HTTP::Tiny and Net::FTP
# LWP::UserAgent is optional
# Mac::BuildTools not needed
# Mac::Files not needed
# Module::Signature is optional
# Net::Config not used at tests
# Net::FTP not used at tests
# Net::Ping is required but >= 2.13 version is a soft dependency
# Net::SSLeay 1.49 is optional
BuildRequires:  perl(Net::Ping)
BuildRequires:  perl(overload)
# Pod::Perldoc is optional
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Text::Wrap)
# Time::Local not used at tests
# URI not used at tests
# URI::Escape not used at tests
# URI::URL 0.08 is optional 
# User::pwent not used at tests
BuildRequires:  perl(warnings)
# Optional:
#%%if !%%{defined perl_bootstrap}
# CPAN::DistnameInfo not used at tests
#%%endif
BuildRequires:  perl(CPAN::Meta) >= 2.110350
# Crypt::OpenPGP not used at tests
# Digest::MD5 not used at tests
BuildRequires:  perl(Digest::SHA)
# Keep Log::Log4perl optional
# Keep MIME::Base64 optional
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Module::Build)
%endif

# Tests:
BuildRequires:  perl(blib)
# CPAN::Checksums not used
BuildRequires:  perl(File::Which)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version)

%if %{with perl_CPAN_enables_optional_test}
# Optional tests:
%if %{with perl_CPAN_enables_gnupg_test}
BuildRequires:  %{_bindir}/gpg
# CPAN::Perl::Releases is helpfull only on RC or TRIAL Perl interpreters
# Digest::SHA1 not needed if Digest::SHA is available
# Digest::SHA::PurePerl not needed if Digest::SHA is available
%endif
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Expect)
%endif
BuildRequires:  perl(Hash::Util)
%if !%{defined perl_bootstrap}
# Kwalify not yet packaged
%if %{with perl_CPAN_enables_gnupg_test}
BuildRequires:  perl(Module::Signature) >= 0.66
%endif
BuildRequires:  perl(Perl::Version)
%endif
BuildRequires:  perl(Pod::Perldoc::ToMan)
%if %{with perl_CPAN_enables_gnupg_test}
BuildRequires:  perl(Socket)
%endif
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Sort::Versions)
# Test::MinimumVersion not used
# Test::Perl::Critic not used
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 0.18
BuildRequires:  perl(YAML) >= 0.60
%endif
%endif

Requires:       make
# Some subpackages modules are not dual-lived. E.g. "open". If a distribution
# on CPAN declares a dependency on such a module, CPAN client will fail
# because the only provider is perl distribution.
# Another issue is with dual-lived modules whose distribution actually does
# not declare all needed core dependencies and the installation would also
# fail.
# As a result, any CPAN client must run-require the complete perl.
Requires:       perl
Requires:       perl(Archive::Tar) >= 1.50
%if !%{defined perl_bootstrap}
Recommends:     perl(CPAN::DistnameInfo)
%endif
Requires:       perl(CPAN::Meta::Requirements) >= 2.121
Requires:       perl(Data::Dumper)
%if !%{defined perl_bootstrap}
Requires:       perl(Devel::Size)
%endif
Requires:       perl(ExtUtils::Manifest)
%if !%{defined perl_bootstrap}
Requires:       perl(File::HomeDir) >= 0.65
%endif
Requires:       perl(File::Temp) >= 0.16
# YAML::XS or YAML::Syck or JSON::PP, we already use YAML::Syck at a different
# place, keep JSON::PP optional
Requires:       perl(lib)
%if !%{defined perl_bootstrap}
Suggests:       perl(Log::Log4perl)
%endif
Requires:       perl(Net::Config)
Requires:       perl(Net::FTP)
Requires:       perl(POSIX)
Requires:       perl(Term::ReadLine)
Requires:       perl(Time::Local)
%if !%{defined perl_bootstrap}
Requires:       perl(URI)
Requires:       perl(URI::Escape)
%endif
Requires:       perl(User::pwent)
# Optional but highly recommended:
%if !%{defined perl_bootstrap}
# Prefer Archive::Zip over unzip
Requires:       perl(Archive::Zip)
Requires:       perl(Compress::Bzip2)
Requires:       perl(CPAN::Meta) >= 2.110350
%endif
Requires:       perl(Compress::Zlib)
Requires:       perl(Digest::MD5)
# CPAN encourages Digest::SHA strongly because of integrity checks
Requires:       perl(Digest::SHA)
Requires:       perl(Dumpvalue)
Requires:       perl(ExtUtils::CBuilder)
# Optional for signature verification CVE-2020-16156
%if ! %{defined perl_bootstrap}
Requires:       perl(Module::Signature)
%endif
%if ! %{defined perl_bootstrap}
# Avoid circular deps local::lib -> Module::Install -> CPAN when bootstraping
# local::lib recommended by CPAN::FirstTime default choice, bug #1122498
Requires:       perl(local::lib)
%endif
%if ! %{defined perl_bootstrap}
Requires:       perl(Module::Build)
%endif
Recommends:     perl(Pod::Perldoc)
%if ! %{defined perl_bootstrap}
Recommends:     perl(Term::ReadKey)
Requires:       perl(Text::Glob)
# Text::Levenshtein::XS or Text::Levenshtein::Damerau::XS or Text::Levenshtein
# or Text::Levenshtein::Damerau::PP
Suggests:       perl(Text::Levenshtein::Damerau::XS)
# YAML::Syck or YAML or Data::Dumper or overload
Suggests:       perl(YAML::Syck)
%endif
Provides:       cpan = %{version}

# Filter non-Linux dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mac::BuildTools\\)
# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CPAN::Meta::Requirements\\)
# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(CPAN::MyConfig\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(local_utils\\)

%description
The CPAN module automates or at least simplifies the make and install of
perl modules and extensions. It includes some primitive searching
capabilities and knows how to use LWP, HTTP::Tiny, Net::FTP and certain
external download clients to fetch distributions from the net.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n CPAN-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

# Change configuration name
find -type f -exec perl -i -pe 's/XCPANCONFIGNAMEX/cpan/g' {} \;
# Remove bundled modules
rm -r ./inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t distroprefs %{buildroot}%{_libexecdir}/%{name}
# Does not work with system module
rm %{buildroot}%{_libexecdir}/%{name}/t/5*pod*.t
# Remove the tests which need ./lib and ./blib
rm %{buildroot}%{_libexecdir}/%{name}/t/03pkgs.t
rm %{buildroot}%{_libexecdir}/%{name}/t/04clean_load.t
# Needed internet connection
rm %{buildroot}%{_libexecdir}/%{name}/t/31sessions.t
# Use system modules for tests
perl -i -ple 's{-Mblib}{}' %{buildroot}%{_libexecdir}/%{name}/t/97-run.t
perl -i -ple 's{-Mblib}{}' %{buildroot}%{_libexecdir}/%{name}/t/97-return_values.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/blib/script
ln -s %{_bindir}/cpan %{buildroot}%{_libexecdir}/%{name}/blib/script
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
unset AUTHOR_TEST CPAN_EXPECT_TIMEOUT CPAN_RUN_SHELL_TEST_WITHOUT_EXPECT \
    ftp_proxy http_proxy no_proxy \
    PERL5_CPAN_IS_RUNNING PERL5_CPAN_IS_RUNNING_IN_RECURSION PERL_CORE VERBOSE
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I .
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TEST CPAN_EXPECT_TIMEOUT CPAN_RUN_SHELL_TEST_WITHOUT_EXPECT \
    ftp_proxy http_proxy no_proxy \
    PERL5_CPAN_IS_RUNNING PERL5_CPAN_IS_RUNNING_IN_RECURSION PERL_CORE VERBOSE
make test

%files
%doc Changes PAUSE*.pub README Todo
%{_bindir}/cpan*
%{perl_vendorlib}/App*
%{perl_vendorlib}/CPAN*
%{_mandir}/man1/cpan*
%{_mandir}/man3/App*
%{_mandir}/man3/CPAN*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.38-522
- Prepare for Oreon 11 (RP1)
