%global source0_hash 171fe15bc7cd38629b5d2c02722e81236e404062708f2aea7b583275c4e8aa22

# Locate pkgconfig using Alien::pkgconf.
# Disabled by default because it creates a build cycle (perl-Alien-pkgconf →
# perl-Alien-Build → perl-PkgConfig-LibPkgConf).
%bcond_with perl_PkgConfig_LibPkgConf_enables_Alien_pkgconf
# Perform optional tests
%bcond_without perl_PkgConfig_LibPkgConf_enables_optional_test

Name:           perl-PkgConfig-LibPkgConf
Version:        0.11
Release:        27%{?dist}
Summary:        Interface to pkg-config files via libpkgconf
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PkgConfig-LibPkgConf
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/PkgConfig-LibPkgConf-%{version}.tar.gz
# Adapt to pkgconf-1.9.4, proposed to an upstream, bug #2172714,
# <https://github.com/PerlAlien/PkgConfig-LibPkgConf/issues/15>
Patch0:         PkgConfig-LibPkgConf-0.11-adapt_to_pkgconf_1.9.4.patch
# Fix retrieving flags from package files whose Name value differs from its
# file name, proposed to an upstream, bug #2172714,
# <https://github.com/PerlAlien/PkgConfig-LibPkgConf/issues/15>
Patch1:         PkgConfig-LibPkgConf-0.11-Fix-resolving-flags-for-packages-with-a-name-differe.patch
# Adapt to pkgconf-2.5.0, applies on top of 1.9.4 patch
Patch2:         PkgConfig-LibPkgConf-0.11-adapt_to_pkgconf_2.5.0.patch
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
%if %{with perl_PkgConfig_LibPkgConf_enables_Alien_pkgconf}
# Use Alien::pkgconf instead of some complicated guess
# script/cc_wrapper.pl and script/ld_wrapper.pl not used with Alien::pkgconf
BuildRequires:  perl(Alien::pkgconf) >= 0.12
%else
# script/cc_wrapper.pl and script/ld_wrapper.pl not used with pkgconf
BuildRequires:  pkgconf
%endif
BuildRequires:  pkgconfig(libpkgconf) >= 1.5.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.98
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.98
%if %{with perl_PkgConfig_LibPkgConf_enables_optional_test}
# Optional tests:
BuildRequires:  perl(YAML)
%endif
Requires:       perl(Carp)
# libpkgconf.so.4() changed an ABI without changing SONAME
# <https://github.com/pkgconf/pkgconf/issues/347>
Requires:       libpkgconf >= 2.1.0

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$

%description
Many libraries in compiled languages such as C or C++ provide *.pc files to
specify the flags required for compiling and linking against those libraries.
Traditionally, the command line program pkg-config is used to query these
files. This package provides a Perl-level API using libpkgconf to these files.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Cwd)
Requires:       perl(Test::More) >= 0.98
%if %{with perl_PkgConfig_LibPkgConf_enables_optional_test}
Requires:       perl(YAML)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n PkgConfig-LibPkgConf-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build
unset FFI_PLATYPUS_DEBUG
export PKG_CONFIG=%{_bindir}/pkgconf
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# audit_set_log() in t/client.t writed into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} $RPM_BUILD_ROOT/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorarch}/auto/PkgConfig
%{perl_vendorarch}/auto/PkgConfig/LibPkgConf
%dir %{perl_vendorarch}/PkgConfig
%{perl_vendorarch}/PkgConfig/LibPkgConf
%{perl_vendorarch}/PkgConfig/LibPkgConf.pm
%{_mandir}/man3/PkgConfig::LibPkgConf.*
%{_mandir}/man3/PkgConfig::LibPkgConf::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
