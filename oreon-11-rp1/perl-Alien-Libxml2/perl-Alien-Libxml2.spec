%global source0_hash 56aae7b339bbeb02f77c5801f57a821be5791b51f43bf7f9062bb3bfa444c328

Name:           perl-Alien-Libxml2
Version:        0.20
Release:        3%{?dist}
Summary:        Install the C libxml2 library on your system
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-Libxml2/
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Libxml2-%{version}.tar.gz

%global debug_package %{nil}

# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Alien::Build::MM) >= 2.37
BuildRequires:  perl(Alien::Build::Plugin::Download::GitLab)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(libxml-2.0)
# Run-time
BuildRequires:  perl(Alien::Base) >= 2.37
BuildRequires:  perl(Alien::Build) >= 2.37
BuildRequires:  perl(alienfile)
BuildRequires:  perl(base)
# Tests
BuildRequires:  perl(Config)
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Test::Alien)
BuildRequires:  perl(Test::More)
Requires:       perl(Alien::Base) >= 2.37
# This RPM package ensures libxml2 is installed on the system
Requires:       pkgconfig(libxml-2.0) = %(type -p pkgconf >/dev/null && pkgconf --exists libxml-2.0 && pkg-config --modversion libxml-2.0 || echo 0)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Alien::Base\\)$

%description
This module provides libxml2 for other modules to use.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Alien-Libxml2-%{version}

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
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t corpus %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Alien*
%{_mandir}/man3/Alien::Libxml2*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
