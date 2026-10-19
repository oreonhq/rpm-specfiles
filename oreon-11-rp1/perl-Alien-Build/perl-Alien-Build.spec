%global source0_hash 8e891fd3acbac39dd8fdc01376b9abff931e625be41e0910ca30ad59363b4477
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%{bcond_without perl_Alien_Build_enables_optional_test}
%{bcond_with perl_Alien_Build_enables_cmake}
%if !%{defined perl_bootstrap}
%{bcond_without perl_Alien_Build_enables_platypus}
%endif
Name:           perl-Alien-Build
Version:        2.84
Release:        5%{?dist}
Summary:        Build external dependencies for use in CPAN
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-Build
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Build-%{version}.tar.gz
Patch0:         Alien-Build-2.83-Remove-redundant-pkgconfig-implementations.patch
Patch1:         Alien-Build-2.65-Remove-redundant-SHA-implementations.patch
BuildArch:      noarch
%if %{with perl_Alien_Build_enables_cmake} && !%{defined perl_bootstrap}
%endif
%if %{with perl_Alien_Build_enables_platypus}
%endif
%if %{with perl_Alien_Build_enables_optional_test}
%if !%{defined perl_bootstrap}
%endif
%endif
Requires:       coreutils
Requires:       gcc
Requires:       make
Requires:       perl-Alien-Base = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{with perl_Alien_Build_enables_cmake} && !%{defined perl_bootstrap}
Requires:       perl(Alien::cmake3) >= 0.02
%endif
Suggests:       perl(Alien::Build::Plugin::Decode::HTML)
Requires:       perl(Alien::Build::Plugin::Decode::Mojo)
Requires:       perl(Archive::Tar)
Requires:       perl(Archive::Zip)
Requires:       perl(Config::INI::Reader::Multiline)
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(ExtUtils::MakeMaker) >= 6.52
Requires:       perl(ExtUtils::ParseXS) >= 3.30
%if %{with perl_Alien_Build_enables_platypus}
Recommends:     perl(FFI::Platypus) >= 0.12
%endif
Requires:       perl(Capture::Tiny) >= 0.17
Requires:       perl(File::BOM)
Requires:       perl(File::Find)
Requires:       perl(HTTP::Tiny) >= 0.044
Requires:       perl(Mozilla::CA)
Requires:       perl(Path::Tiny) >= 0.077
Requires:       perl(PkgConfig::LibPkgConf::Client) >= 0.04
Requires:       perl(PkgConfig::LibPkgConf::Util) >= 0.04
Requires:       perl(Storable)
Requires:       perl(Test2::API) >= 1.302096
Requires:       perl(Text::ParseWords) >= 3.26
Recommends:     perl(YAML)
Obsoletes:      perl-Test-Alien < 0.15-13
Provides:       perl-Test-Alien = %{version}-%{release}
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Capture::Tiny|Path::Tiny|Test2::API|Test2::V0|Text::ParseWords)\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Alien::Build::rc\\)$
%global __provides_exclude %{__provides_exclude}|^perl\\(Alien::Build::Plugin::(Download::Foo|Fetch::Corpus|Fetch::Foo|NesAdvantage::Controller|NesAdvantage::HelperTest|NesAdvantage::Negotiate|RogerRamjet)|Alien::Foo|Alien::Foo1|Alien::Foo1::ConfigData|Alien::Foo2|Alien::Foo2::ConfigData|Alien::foomake|Alien::libfoo1|Alien::libfoo2|Alien::libfoo3|Alien::perlhelp|Alien::SansShare|Foo::Bar::Baz|Foo::Bar::Baz1|MyTest::.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Alien::Build::Plugin::RogerRamjet|Alien::Foo|Alien::libfoo1|Alien::libfoo2|Alien::perlhelp|MyTest::.*\\)$
%global __brp_mangle_shebangs_exclude_from %{?__brp_mangle_shebangs_exclude_from:%{__brp_mangle_shebangs_exclude_from}|}^%{_libexecdir}/%{name}/corpus/dist/foo-1\.00/configure$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Acme::Alien::DontPanic)
BuildRequires:  perl(Alien::Base::ModuleBuild)
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::INI::Reader::Multiline)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Env)
BuildRequires:  perl(Env::ShellWords)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(FFI::CheckLib)
BuildRequires:  perl(FFI::Platypus)
BuildRequires:  perl(File::BOM)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mojo::DOM)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Net::FTP)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(PkgConfig::LibPkgConf::Client)
BuildRequires:  perl(PkgConfig::LibPkgConf::Util)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(YAML)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package provides tools for building external (non-CPAN) dependencies
for CPAN. It is mainly designed to be used at install time of a CPAN
client, and work closely with Alien::Base which is used at run time.

%package -n perl-Alien-Base
Summary:        Base classes for Alien:: modules
Requires:       perl(DynaLoader)
Requires:       perl(FFI::CheckLib)
Requires:       perl(File::Find)
Requires:       perl(JSON::PP)
Requires:       perl(Path::Tiny) >= 0.077
Requires:       perl(Storable)
Requires:       perl(Text::ParseWords) >= 3.26
Requires:       pkgconf-pkg-config
Conflicts:      perl-Alien-Base-ModuleBuild < 1.00
Conflicts:      perl-Alien-Build < 2.47-2
%description -n perl-Alien-Base
Alien::Base comprises base classes to help in the construction of
"Alien::" modules.

%package Plugin-Decode-HTML
Summary:        Alien::Build plugin to extract links from HTML
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(HTML::LinkExtor)
Requires:       perl(URI)
Requires:       perl(URI::Escape)
Conflicts:      perl-Alien-Build < 1.76
%description Plugin-Decode-HTML
This Alien::Build plugin decodes an HTML file listing into a list of
candidates for your Prefer plugin.

%package Plugin-Decode-Mojo
Summary:        Alien::Build plugin to extract links from HTML
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Mojo::DOM)
Requires:       perl(Mojolicious) >= 7.00
Requires:       perl(URI)
Requires:       perl(URI::Escape)
%description Plugin-Decode-Mojo
This Alien::Build plugin decodes an HTML file listing into a list of
candidates for your Prefer plugin.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Net::FTP)
Requires:       perl(Test2::V0) >= 0.000121
%if %{with perl_Alien_Build_enables_optional_test}
%if !%{defined perl_bootstrap}
Requires:       perl(Acme::Alien::DontPanic) >= 0.026
Requires:       perl(Alien::Base::ModuleBuild) >= 0.040
%endif
Requires:       perl(Devel::Hide)
Requires:       perl(Env::ShellWords)
Requires:       perl(HTTP::Tiny) >= 0.044
Requires:       perl(Mojo::DOM)
Requires:       perl(Mojolicious) >= 7.00
Requires:       perl(Readonly) >= 1.60
Requires:       perl(Sort::Versions)
Requires:       perl(URI::file)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Alien-Build-%{version}
# Remove redundant pkgconfig implementations, keep
# Alien::Build::Plugin::PkgConfig::LibPkgConf,
# MANIFEST is updated by Remove-redundant-pkgconfig-implementations.patch.
%patch -p1 -P 0
rm lib/Alien/Build/Plugin/PkgConfig/{CommandLine,PP}.pm 
rm t/alien_build_plugin_pkgconfig_{commandline,makestatic,pp}.t
# Remove redundant SHA digest imlementations, keep
# Alien::Build::Plugin::Digest::SHA, MANIFEST is updated by
# Alien-Build-2.59-Remove-redundant-SHA-implementations.patch.
%patch -p1 -P 1
rm lib/Alien/Build/Plugin/Digest/SHAPP.pm
rm t/alien_build_plugin_digest_shapp.t
%if !%{with perl_Alien_Build_enables_cmake} && !%{defined perl_bootstrap}
    # Remove CMake support
    rm lib/Alien/Build/Plugin/Build/CMake.pm
    perl -i -ne 'print $_ unless m{\b\Qlib/Alien/Build/Plugin/Build/CMake.pm\E\b}' Makefile.PL MANIFEST
    perl -i -ne 'print $_ unless m{\b\QAlien::Build::Plugin::Build::CMake\E\b}' t/01_use.t
%endif
# Remove unused tests
for F in \
    t/alien_build_plugin_probe_vcpkg.t \
    t/bin/ftpd \
    t/bin/httpd \
%if !%{with perl_Alien_Build_enables_cmake} || %{defined perl_bootstrap}
    t/alien_build_plugin_build_cmake.t \
%endif
%if !%{with perl_Alien_Build_enables_optional_test} || %{defined perl_bootstrap}
    t/alien_base__system_installed.t \
%endif
%if !%{with perl_Alien_Build_enables_optional_test}
    t/alien_build_plugin_build_searchdep.t \
    t/alien_build_plugin_extract_commandline__tar_can.t \
    t/alien_build_plugin_prefer_badversion.t \
    t/alien_build_plugin_prefer_goodversion.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E\b}' MANIFEST
    perl -i -ne 'print $_ unless m{\b\Q'"$F"'\E\b}' t/01_use.t
done
# Symlink identical files
function symlink_duplicates {
    local KEEP="$1"
    local DUPLICATE_GLOB="$2"
    local F
    shopt -s globstar
    for F in $DUPLICATE_GLOB; do
        test "$KEEP" = "$F" && continue
        cmp "$KEEP" "$F" || continue
        rm "$F"
        ln -s "$(realpath --relative-to $(dirname $F) $KEEP)" "$F"
    done
}
symlink_duplicates 'corpus/alien_build_plugin_fetch_curlcommand/dir/foo-1.00.tar' 'corpus/*/dir/foo-1.00.tar'
symlink_duplicates 'corpus/alien_build_plugin_fetch_curlcommand/dir/foo-1.01.tar' 'corpus/*/dir/foo-1.01.tar'
symlink_duplicates 'corpus/alien_build_plugin_fetch_curlcommand/dir/foo-1.02.tar' 'corpus/*/dir/foo-1.02.tar'
symlink_duplicates 'corpus/alien_build_plugin_fetch_curlcommand/dir/html_test.html' 'corpus/*/dir/html_test.html'
symlink_duplicates 'example/user/ffi-platypus/t/lzma_example.t' 'example/user/*/t/lzma_example.t'
symlink_duplicates 'example/user/xs-dzil/Example.xs' 'example/**/Example.xs'
symlink_duplicates 'example/user/xs-dzil/lib/LZMA/Example.pm' 'example/**/Example.pm'
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

unset PKG_CONFIG
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
mkdir %{buildroot}%{_libexecdir}/%{name}/example
cp -a example/*.alienfile %{buildroot}%{_libexecdir}/%{name}/example
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset ACLOCAL_PATH ALIEN_BASE_WRAPPER_QUIET ALIEN_BUILD_LIVE_TEST \
    ALIEN_BUILD_LOG ALIEN_BUILD_PKG_CONFIG ALIEN_BUILD_POSTLOAD \
    ALIEN_BUILD_PRELOAD ALIEN_BUILD_RC ALIEN_BUILD_SITE_CONFIG \
    ALIEN_CPU_COUNT ALIEN_DOWNLOAD_RULE ALIEN_FORCE \
    ALIEN_INSTALL_NETWORK ALIEN_INSTALL_TYPE CONFIG_SITE CURL DESTDIR \
    FOO1 FOO2 FOO3 TEST_ALIEN_ALIENS_MISSING TEST_ALIEN_ALWAYS_KEEP VERBOSE WGET
export CIPSOMETHING=true
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles perl-Alien-Base usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset ACLOCAL_PATH ALIEN_BASE_WRAPPER_QUIET ALIEN_BUILD_LIVE_TEST \
    ALIEN_BUILD_LOG ALIEN_BUILD_PKG_CONFIG ALIEN_BUILD_POSTLOAD \
    ALIEN_BUILD_PRELOAD ALIEN_BUILD_RC ALIEN_BUILD_SITE_CONFIG \
    ALIEN_CPU_COUNT ALIEN_DOWNLOAD_RULE ALIEN_FORCE \
    ALIEN_INSTALL_NETWORK ALIEN_INSTALL_TYPE CONFIG_SITE CURL DESTDIR \
    FOO1 FOO2 FOO3 TEST_ALIEN_ALIENS_MISSING TEST_ALIEN_ALWAYS_KEEP VERBOSE WGET
export CIPSOMETHING=true
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Alien-Base -f %{oreon_filedir}/perl-Alien-Base.list
%files -n perl-Alien-Build-Plugin-Decode-HTML -f %{oreon_filedir}/perl-Alien-Build-Plugin-Decode-HTML.list
%files -n perl-Alien-Build-Plugin-Decode-Mojo -f %{oreon_filedir}/perl-Alien-Build-Plugin-Decode-Mojo.list
%files -n perl-Alien-Build-tests -f %{oreon_filedir}/perl-Alien-Build-tests.list

%changelog

%autochangelog
