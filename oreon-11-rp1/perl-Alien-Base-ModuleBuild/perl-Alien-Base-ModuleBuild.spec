%global source0_hash fe7270ac735adde864e468e21c642a471ba88ba25ad30da94578832132f2b9f4
%bcond_without perl_Alien_Base_ModuleBuild_enables_optional_test
%bcond_without perl_Alien_Base_ModuleBuild_enables_ssl
Name:           perl-Alien-Base-ModuleBuild
Version:        1.17
Release:        9%{?dist}
Summary:        Perl framework for building Alien:: modules and their libraries
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-Base-ModuleBuild
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Base-ModuleBuild-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Alien_Base_ModuleBuild_enables_ssl}
%endif
%define perl_Test2_V0_minver 0.000121
%if %{with perl_Alien_Base_ModuleBuild_enables_optional_test}
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
Requires:       perl(IO::Socket::SSL) >= 1.56
Requires:       perl(Net::SSLeay) >= 1.49
%endif
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Alien::Base::PkgConfig|Capture::Tiny|File::chdir|HTTP::Tiny|List::Util|Module::Build|Path::Tiny|Test2::V0|Text::ParseWords)\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Test2::Plugin::AlienEnv\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Test2::Plugin::AlienEnv\\)
# oreon:deps
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Alien::Base::PkgConfig)
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Env)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Installed)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(HTML::LinkExtor)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Net::FTP)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Shell::Config::Generate)
BuildRequires:  perl(Shell::Guess)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset ALIEN_ARCH ALIEN_DOWNLOAD_RULE ALIEN_FORCE ALIEN_INSTALL_NETWORK \
    ALIEN_INSTALL_TYPE ALIEN_VERBOSE
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset ALIEN_ARCH ALIEN_DOWNLOAD_RULE ALIEN_FORCE ALIEN_INSTALL_NETWORK \
    ALIEN_INSTALL_TYPE ALIEN_VERBOSE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Alien-Base-ModuleBuild-tests -f %{oreon_filedir}/perl-Alien-Base-ModuleBuild-tests.list

%changelog

%autochangelog
