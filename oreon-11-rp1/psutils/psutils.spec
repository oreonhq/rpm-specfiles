%global source0_hash 3ff76cc9f9fb535ec553d1591de56d6dbaa0d9f4df86778f6a49731ebd764cdf
%bcond psutils_enables_unbundling_gnulib %{undefined rhel}
Name:       psutils
Version:    3.3.17
Release:        1%{?dist}
Summary:        PostScript utilities
License:    GPL-3.0-or-later
URL:        https://github.com/rrthomas/%{name}
Source0:        https://github.com/rrthomas/psutils/releases/download/v3.3.17/psutils-3.3.17.tar.gz
BuildArch:      noarch
%if %{with psutils_enables_unbundling_gnulib}
%endif
Provides:       bundled(gnulib)%(perl -ne 'if($. == 1 and /\A(\d+)-(\d+)-(\d+)/) {print qq{ = $1$2$3}}' %{_defaultdocdir}/gnulib/ChangeLog 2>/dev/null)
Provides:       %{name}-perl = %{version}-%{release}
Obsoletes:      %{name}-perl < %{version}-%{release}
Requires:       paper
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(PSUtils\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(PSUtils\\)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  diffutils
BuildRequires:  gcc
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  paper
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Utilities for manipulating PostScript documents.
Page selection and rearrangement are supported, including arrangement into
signatures for booklet printing, and page merging for n-up printing.

%package tests
Summary:        Tests for %{name}
License:        GPL-3.0-or-later and FSFULLR and MIT and FSFAP
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       diffutils
Requires:       make
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%if %{with psutils_enables_unbundling_gnulib}
gnulib-tool --import --no-changelog relocatable-perl
%endif
autoreconf -fi

%build

%configure --disable-relocatable
%{make_build}
%install
%{make_install}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a aclocal.m4 build-aux config.status configure configure.ac m4 Makefile* tests %{buildroot}%{_libexecdir}/%{name}
printf '#!/bin/sh\nexec "$@"\n' > %{buildroot}%{_libexecdir}/%{name}/pre-inst-env
chmod +x %{buildroot}%{_libexecdir}/%{name}/pre-inst-env
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset PSUTILS_UNINSTALLED
make -j "$(getconf _NPROCESSORS_ONLN)" check-TESTS
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset PSUTILS_UNINSTALLED
make check %{?_smp_mflags}
%files -f %{oreon_filedir}/main.list
%files -n psutils-tests -f %{oreon_filedir}/psutils-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.10-10
- Prepare for Oreon 11 (RP1)
