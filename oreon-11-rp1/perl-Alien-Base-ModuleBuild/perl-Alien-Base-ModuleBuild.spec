%global source0_hash fe7270ac735adde864e468e21c642a471ba88ba25ad30da94578832132f2b9f4

# Run optional tests
%bcond_without perl_Alien_Base_ModuleBuild_enables_optional_test
# Enable SSL support
%bcond_without perl_Alien_Base_ModuleBuild_enables_ssl

Name:           perl-Alien-Base-ModuleBuild
Version:        1.17
Release:        9%{?dist}
Summary:        Perl framework for building Alien:: modules and their libraries
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-Base-ModuleBuild
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Base-ModuleBuild-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Dependency on pkgconf-pkg-config is not needed since 1.00
# <https://github.com/Perl5-Alien/Alien-Base-ModuleBuild/issues/5>
# Run-time:
# Alien::Base in lib/Alien/Base/ModuleBuild.pm is optional
BuildRequires:  perl(Alien::Base::PkgConfig) >= 1.20
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(Capture::Tiny) >= 0.17
BuildRequires:  perl(Carp)
BuildRequires:  perl(Env)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Installed)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::chdir) >= 0.1005
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Tiny) >= 0.044
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Net::FTP)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Tiny) >= 0.077
# PkgConfig not used if pkg-config tool is available
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Shell::Config::Generate)
BuildRequires:  perl(Shell::Guess)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(Text::ParseWords) >= 3.26
BuildRequires:  perl(URI)
# Optional run-time:
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(HTML::LinkExtor)
%if %{with perl_Alien_Base_ModuleBuild_enables_ssl}
# The Alien::Base::ModuleBuild is used from user's Build.PL to interpret
# alien_repository Build.PL section. The section contains an URL to fetch
# sources of a missing C library. If the URL uses https schema,
# IO::Socket::SSL and Net::SSLeay are added into compile-time dependencies
# via MY_META.json and interpreted by a CPAN client as build-time dependencies.
# So either the CPAN client will try to build the SSL modules, or in case of
# no CPAN client, the build fails with an "Internal Exception" in
# Alien::Base::ModuleBuild because it won't download the sources using
# HTTP::Tiny.
# IO::Socket::SSL 1.56 not used at tests
# Net::SSLeay 1.49 not used at tests
%endif
# Tests:
# bash for /bin/sh
BuildRequires:  bash
BuildRequires:  perl(base)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
%define perl_Test2_V0_minver 0.000121
BuildRequires:  perl(Test2::V0) >= %{perl_Test2_V0_minver}
BuildRequires:  perl(URI::file)
%if %{with perl_Alien_Base_ModuleBuild_enables_optional_test}
# Optional tests:
# ExtUtils::CBuilder for platform=>src test in t/alien_base_modulebuild.t
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(LWP::UserAgent)
%endif
Requires:       perl(Alien::Base::PkgConfig) >= 1.20
Recommends:     perl(Digest::SHA)
Requires:       perl(File::chdir) >= 0.1005
Requires:       perl(File::Find)
Requires:       perl(File::ShareDir) >= 1.00
Recommends:     perl(HTML::LinkExtor)
Requires:       perl(HTTP::Tiny) >= 0.044
Requires:       perl(List::Util) >= 1.45
Requires:       perl(Module::Build) >= 0.4004
Requires:       perl(Path::Tiny) >= 0.077
Requires:       perl(Text::ParseWords) >= 3.26
%if %{with perl_Alien_Base_ModuleBuild_enables_ssl}
# The Alien::Base::ModuleBuild is used from user's Build.PL to interpret
# alien_repository Build.PL section. The section contains an URL to fetch
# sources of a missing C library. If the URL uses https schema,
# IO::Socket::SSL and Net::SSLeay are added into compile-time dependencies
# via MY_META.json and interpreted by a CPAN client as build-time dependencies.
# So either the CPAN client will try to build the SSL modules, or in case of
# no CPAN client, the build fails with an "Internal Exception" in
# Alien::Base::ModuleBuild because it won't download the sources using
# HTTP::Tiny.
Requires:       perl(IO::Socket::SSL) >= 1.56
Requires:       perl(Net::SSLeay) >= 1.49
%endif
# Dependency on pkgconf-pkg-config is not needed since 1.00
# <https://github.com/Perl5-Alien/Alien-Base-ModuleBuild/issues/5>

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Alien::Base::PkgConfig|Capture::Tiny|File::chdir|HTTP::Tiny|List::Util|Module::Build|Path::Tiny|Test2::V0|Text::ParseWords)\\)
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(Test2::Plugin::AlienEnv\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Test2::Plugin::AlienEnv\\)

%description
This is a Perl base class and framework for creating Alien distributions. The
goal of the project is to make things as simple and easy as possible for both
developers and users of Alien modules.

Alien is a Perl name space for defining dependencies in CPAN for libraries and
tools which are not "native" to CPAN. Alien modules will typically use the
system libraries if they are available, or download the latest version from
the internet and build them from source code. These libraries can then be
used by other Perl modules, usually modules that are implemented with XS or FFI.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Capture::Tiny) >= 0.17
Requires:       perl(Test2::V0) >= %{perl_Test2_V0_minver}
Requires:       perl(File::chdir) >= 0.1005
Requires:       perl(Path::Tiny) >= 0.077
%if %{with perl_Alien_Base_ModuleBuild_enables_optional_test}
Requires:       perl(Digest::SHA)
Requires:       perl(HTTP::Tiny) >= 0.044
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(LWP::UserAgent)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Alien-Base-ModuleBuild-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset ALIEN_ARCH ALIEN_DOWNLOAD_RULE ALIEN_FORCE ALIEN_INSTALL_NETWORK \
    ALIEN_INSTALL_TYPE ALIEN_VERBOSE
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset ALIEN_ARCH ALIEN_DOWNLOAD_RULE ALIEN_FORCE ALIEN_INSTALL_NETWORK \
    ALIEN_INSTALL_TYPE ALIEN_VERBOSE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
