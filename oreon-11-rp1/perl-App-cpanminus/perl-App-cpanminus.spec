%global source0_hash b9ffb88e62a06aa91bd7d5a28ef6bdbb942608aea90e3969aa29b33640035214

Name:           perl-App-cpanminus
Version:        1.7049
Release:        1%{?dist}
Summary:        Get, unpack, build and install CPAN modules
# Other files:  GPL+ or Artistic
## unbundled
# lib/App/cpanminus/fatscript.pm:   File::pushd:    ASL 2.0
## at build-time only
# fatunpack:    GPL+
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/App-cpanminus
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/App-cpanminus-%{version}.tar.gz
Source1:        fatunpack
# Correct an SHA version in a message, in upstream's devel branch,
# <https://github.com/miyagawa/cpanminus/pull/617>
Patch0:         App-cpanminus-1.7044-SHA1-SHA256-in-checksum-chat.patch
BuildArch:      noarch
BuildRequires:  %{_bindir}/podselect
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Nothing special. The tests are very poor. But we run perl -c at built-time
# to check for correct unpacking. So we need non-optional run-time
# dependencies at build-time too:
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
# CPAN::DistnameInfo not needed for compilation
# CPAN::Meta not needed for copmilation
# CPAN::Meta::Check not needed for compilation
BuildRequires:  perl(CPAN::Meta::Requirements)
# CPAN::Meta::YAML not needed for compilation
BuildRequires:  perl(Cwd)
# Digest::SHA not needed for compilation
# ExtUtils::Manifest not needed for compilation
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
# File::HomeDir not needed for compilation
# File::pushd not needed for compilation
BuildRequires:  perl(File::Temp)
# HTTP::Tiny not needed for compilation
# JSON::PP not needed for compilation
# local::lib not needed for compilation
# LWP::Protocol::https not needed for compilation
# LWP::UserAgent not needed for compilation
# Module::CoreList not needed for compilation
# Module::CPANfile not needed for compilation
# Module::Metadata not needed for compilation
# Module::Signature not needed for compilation
# Parse::PMFile not needed for compilation
# Safe not needed for compilation
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(version)
# version::vpp not needed
# Win32 not used
# YAML not needed for compilation
# Tests:
BuildRequires:  perl(Test::More)
# There is no way to install core non-duallived modules from CPAN,
# (e.g. Path-Tiny CPAN distribution requiers "open" module), require full Perl
# for that.
%if 0%(perl -e 'print $] < 5.026' 2>/dev/null)
Requires:       perl-core
%else
Requires:       perl
%endif
# Current dependency generator cannot parse compressed code. Use PPI to find
# them, and list them manually:
# Archive::Tar is optional
# Archive::Zip is optional
# Compress::Zlib is optional
Requires:       perl(CPAN::DistnameInfo)
Requires:       perl(CPAN::Meta)
Requires:       perl(CPAN::Meta::Check) >= 0.018
Requires:       perl(CPAN::Meta::YAML)
Requires:       perl(Digest::SHA)
Requires:       perl(ExtUtils::Install) >= 1.46
Requires:       perl(ExtUtils::MakeMaker) >= 6.58
Requires:       perl(ExtUtils::Manifest)
# File::HomeDir is optional
Requires:       perl(File::pushd)
# HTTP getter by LWP::UserAgent or wget or curl or HTTP::Tiny
Requires:       perl(HTTP::Tiny)
Requires:       perl(local::lib)
# LWP::Protocol::https is optional
# LWP::UserAgent is optional
Requires:       perl(Module::Build) >= 0.38
Requires:       perl(Module::CoreList)
Requires:       perl(Module::CPANfile)
Requires:       perl(Module::Metadata)
# Module::Signature is optional
Requires:       perl(Parse::PMFile)
Requires:       perl(Safe)
# version::vpp not used
# Win32 not used
Requires:       perl(YAML)
# XXX: Keep Provides: cpanminus to allow `yum install cpanminus' instead of
# longer `yum install perl-App-cpanminus'.
Provides:       cpanminus = %{version}-%{release}
Obsoletes:      cpanminus <= 1.2002

# Filter under-specified dependencies
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(App::cpanminus\\)$
# Filter private modules
%global __provides_exclude %{__provides_exclude}|^perl\\(ModuleBuildSkipMan\\)

%description
Why? It's dependency free, requires zero configuration, and stands alone 
but it's maintainable and extensible with plug-ins and friendly to shell 
scripting. When running, it requires only 10 MB of RAM.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n App-cpanminus-%{version}
# Unbundle fat-packed modules
podselect lib/App/cpanminus.pm > lib/App/cpanminus.pod

for F in bin/cpanm lib/App/cpanminus/fatscript.pm; do
    # CVE-2024-45321 - patch to use https instead of http
    perl -pi -E 's{http://(cpan\.cpantesters\.org|www\.cpan\.org|backpan\.perl\.org|cpan\.metacpan\.org|fastapi\.metacpan\.org|cpanmetadb\.plackperl\.org)}{https://$1}g' "$F"
    %{SOURCE1} --libdir lib --filter '^App/cpanminus' "$F" > "${F}.stripped"
    perl -c -Ilib "${F}.stripped"
    mv "${F}.stripped" "$F"
done

%patch -P0 -p1

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/App*
%{_mandir}/man1/cpanm*
%{_mandir}/man3/App::cpanminus*
%{_bindir}/cpanm

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7049-1
- Prepare for Oreon 11 (RP1)
