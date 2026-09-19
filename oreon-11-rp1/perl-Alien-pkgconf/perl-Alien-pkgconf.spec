%global source0_hash b9abab04605aab11089005b98e5ff202b93912cbde2ec67ee688f278ea77f765

Name:           perl-Alien-pkgconf
Version:        0.21
Release:        3%{?dist}
Summary:        Discover pkgconf and libpkgconf
# Other files:  GPL-1.0-or-later OR Artistic-1.0-Perl
## Not used
# patch/pkgconf-solaris-1.3.9.diff: GPL-3.0-or-later WITH Autoconf-exception-macro
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
SourceLicense:  (%{license}) AND GPL-3.0-or-later WITH Autoconf-exception-macro
URL:            https://metacpan.org/release/Alien-pkgconf
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-pkgconf-%{version}.tar.gz
# Accept pkgconf-1.9, we have patched perl-PkgConfig-LibPkgConf, bug #2172713
Patch0:         Alien-pkgconf-0.19-Accept-pkgconf-1.9.patch
# This is a full-arch package because it stores data about arch-specific
# libpkgconf.so library and it stores them into an arch-specific directory.
# But it does not install any ELF, therefore disable debuginfo generation.
%global debug_package %{nil}
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.98
# FFI::CheckLib is optional but provides additional data to bake into a binary
# package
BuildRequires:  perl(FFI::CheckLib)
# script/system.pl is executed at build time
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::PP) >= 2.27400
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconf
# Upstream precludes pkgconfig(libpkgconf) >= 1.9.0 because
# PkgConfig-LibPkgConf-0.11 does not support it.
# But we have added the support in downstream.
# <https://github.com/PerlAlien/PkgConfig-LibPkgConf/issues/15>.
BuildRequires:  pkgconfig(libpkgconf) >= 1.5.2
# Run-time:
BuildRequires:  perl(File::ShareDir) >= 1.102
# Tests:
# An XS code is built by Test::Alien::xs_ok() in t/xs.t
BuildRequires:  perl-devel
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test2::V0) >= 0.000065
BuildRequires:  perl(Test::Alien) >= 0.08
# This RPM package ensures libpkgconf.so is installed on the system
Requires:       libpkgconf-devel(%{__isa}) = %(type -p pkgconf >/dev/null && pkgconf --exists libpkgconf && pkgconf --modversion libpkgconf || echo 0)
Requires:       perl(File::ShareDir) >= 1.102
Requires:       perl(JSON::PP) >= 2.27400

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((File::ShareDir|JSON::PP|Test::Alien|Test2::V0)\\)$

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
# An XS code is built by Test::Alien::xs_ok() in t/xs.t
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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
# ExtUtils::CBuilder::have_compiler() writes into CWD
# <https://github.com/Perl/perl5/issues/15697>.
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorarch}/auto/Alien
%{perl_vendorarch}/auto/Alien/pkgconf
%dir %{perl_vendorarch}/auto/share
%dir %{perl_vendorarch}/auto/share/dist
%{perl_vendorarch}/auto/share/dist/Alien-pkgconf
%dir %{perl_vendorarch}/Alien
%{perl_vendorarch}/Alien/pkgconf.pm
%{_mandir}/man3/Alien::pkgconf.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
