%global source0_hash 171fe15bc7cd38629b5d2c02722e81236e404062708f2aea7b583275c4e8aa22
%bcond_with perl_PkgConfig_LibPkgConf_enables_Alien_pkgconf
%bcond_without perl_PkgConfig_LibPkgConf_enables_optional_test
Name:           perl-PkgConfig-LibPkgConf
Version:        0.11
Release:        27%{?dist}
Summary:        Interface to pkg-config files via libpkgconf
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PkgConfig-LibPkgConf
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/PkgConfig-LibPkgConf-%{version}.tar.gz
Patch0:         PkgConfig-LibPkgConf-0.11-adapt_to_pkgconf_1.9.4.patch
Patch1:         PkgConfig-LibPkgConf-0.11-Fix-resolving-flags-for-packages-with-a-name-differe.patch
Patch2:         PkgConfig-LibPkgConf-0.11-adapt_to_pkgconf_2.5.0.patch
%if %{with perl_PkgConfig_LibPkgConf_enables_Alien_pkgconf}
%else
%endif
%if %{with perl_PkgConfig_LibPkgConf_enables_optional_test}
%endif
Requires:       perl(Carp)
Requires:       libpkgconf >= 2.1.0
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(YAML)
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(libpkgconf)
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-PkgConfig-LibPkgConf-tests -f %{oreon_filedir}/perl-PkgConfig-LibPkgConf-tests.list

%changelog

%autochangelog
