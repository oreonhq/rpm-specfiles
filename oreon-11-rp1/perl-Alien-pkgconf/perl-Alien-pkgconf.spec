%global source0_hash b9abab04605aab11089005b98e5ff202b93912cbde2ec67ee688f278ea77f765
Name:           perl-Alien-pkgconf
Version:        0.21
Release:        3%{?dist}
Summary:        Discover pkgconf and libpkgconf
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
SourceLicense:  (%{license}) AND GPL-3.0-or-later WITH Autoconf-exception-macro
URL:            https://metacpan.org/release/Alien-pkgconf
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-pkgconf-%{version}.tar.gz
Patch0:         Alien-pkgconf-0.19-Accept-pkgconf-1.9.patch
%global debug_package %{nil}
Requires:       libpkgconf-devel(%{__isa}) = %(type -p pkgconf >/dev/null && pkgconf --exists libpkgconf && pkgconf --modversion libpkgconf || echo 0)
Requires:       perl(File::ShareDir) >= 1.102
Requires:       perl(JSON::PP) >= 2.27400
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((File::ShareDir|JSON::PP|Test::Alien|Test2::V0)\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FFI::CheckLib)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Alien)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(libpkgconf)
# /oreon:deps
%description
This Perl module provides you with the information that you need to invoke
pkgconf or link against libpkgconf. It isn't intended to be used directly,
but rather to provide the necessary package by a CPAN module that needs
libpkgconf, such as PkgConfig::LibPkgConf.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-devel
Requires:       perl-Test-Harness
Requires:       perl(Test2::V0) >= 0.000065
Requires:       perl(Test::Alien) >= 0.08
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Alien-pkgconf-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

unset ALIEN_FORCE ALIEN_INSTALL_TYPE
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
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
%files -n perl-Alien-pkgconf-tests -f %{oreon_filedir}/perl-Alien-pkgconf-tests.list

%changelog

%autochangelog
