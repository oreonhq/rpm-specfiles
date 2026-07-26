%global source0_hash 28efc48023862654ffd405eec9869b5d0ec362698e2280672f5007cda95b2d50

Name:           perl-Acme-Alien-DontPanic
%global cpan_version 2.7200
Version:        2.720.0
Release:        9%{?dist}
Summary:        Test module for Alien::Base
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Acme-Alien-DontPanic
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Acme-Alien-DontPanic-%{cpan_version}.tar.gz
# Full-arch for files storing architecture-specific paths
%global debug_package %{nil}
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
# Alien::Build::MM version from Alien::Build in Makefile.PL
BuildRequires:  perl(Alien::Build::MM) >= 2.59
# Alien::Build::Plugin::Digest::Negotiate not used
BuildRequires:  perl(Alien::Build::Plugin::Build::Autoconf)
BuildRequires:  perl(Alien::Build::Plugin::Probe::CommandLine)
BuildRequires:  perl(alienfile)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Use a system dontpanic library instead of downloading it from the Internet at
# build time.
BuildRequires:  pkgconfig(dontpanic)
# Run-time:
BuildRequires:  perl(Alien::Base) >= 2.59
BuildRequires:  perl(base)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Inline) >= 0.56
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(Inline::CPP)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Test::Alien) >= 0.05
BuildRequires:  perl(Test::Alien::Diag)
# Optional tests:
# Test::More not helpful
Requires:       perl(Alien::Base) >= 2.59
# The maning of the package is have dontpanic library installed and
# application being able to build against it. Because we use system dontpanic
# library instead of bundling one that had been dowloaded and compiled at
# build time, we need to explicitly run-require the developmental files of the
# library.
Requires:       pkgconfig(dontpanic)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Alien::Base|Test2::V0)\\)$

%description
This Perl module is a toy module to test the efficacy of the Alien::Base system.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Inline::C)
Requires:       perl(Inline::CPP)
Requires:       perl(Test2::V0) >= 0.000121

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Acme-Alien-DontPanic-%{cpan_version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
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
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Acme
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
