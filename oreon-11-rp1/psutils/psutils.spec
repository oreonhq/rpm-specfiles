%global source0_hash 6f8339fd5322df5c782bfb355d9f89e513353220fca0700a5a28775404d7e98b

# Unbundle gnulib
%bcond psutils_enables_unbundling_gnulib %{undefined rhel}

Name:       psutils
Version:    2.10
Release:    10%{?dist}
Summary:    PostScript utilities
# COPYING:          GPLv3 text
# epsffit.1:        GPLv3+
# epsffit.in.in:    GPLv3+
# extractres.in.in: psutils
# includeres.in.in: psutils
# psbook.1:         GPLv3+
# psbook.in.in:     GPLv3+
# psjoin.1:         GPLv3+
# psjoin.in.in:     GPLv3+
# psnup.in.in:      GPLv3+
# psresize.1:       GPLv3+
# psresize.in.in:   GPLv3+
# psselect.1:       GPLv3+
# psselect.in.in:   GPLv3+
# pstops.1:         GPLv3+
# pstops.in.in:     GPLv3+
# PSUtils.pm:       GPLv3+
# README:           GPLv3+
## In tests subpackage
# aclocal.m4:       FSFULLR
# build-aux/compile:        GPLv2+ with Autoconf exception
# build-aux/config.guess:   GPLv3+ with Autoconf exception
# build-aux/config.sub:     GPLv3+ with Autoconf exception
# build-aux/depcomp:        GPLv2+ with Autoconf exception
# build-aux/install-sh:     MIT
# build-aux/missing:        GPLv2+ with Autoconf exception
# build-aux/mdate-sh:       GPLv2+ with Autoconf exception
# build-aux/test-driver:    GPLv2+ with Autoconf exception
# build-aux/texinfo.tex:    GPLv3+ with TeX exception
# configure:                FSFULLR
# m4/00gnulib.m4:           FSFULLR
# m4/ax_check_gnu_make.m4:  FSFAP
# m4/gnulib-common.m4:      FSFULLR
# m4/gnulib-comp.m4:        GPLv3+ with Autoconf exception
# m4/relocatable-lib.m4:    FSFULLR
# Makefile.in:              FSFULLR
## Not in any binary package
# INSTALL:                  FSFAP
# old-scripts/fixwfwps:     See LICENSE
# pre-inst-env.in:          GPLv2+
License:    GPL-3.0-or-later
URL:        https://github.com/rrthomas/%{name}
Source:        https://github.com/rrthomas/psutils/releases/download/v2.10/psutils-2.10.tar.gz
BuildArch:      noarch
BuildRequires:  autoconf
BuildRequires:  automake >= 1.11
BuildRequires:  bash
# coreutils for chmod in Makefile.am
BuildRequires:  coreutils
# gcc is a default autoconf dependency and populates EXEEXT variable used in
# Makefile.am.
BuildRequires:  gcc
%if %{with psutils_enables_unbundling_gnulib}
BuildRequires:  gnulib-devel
%endif
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  sed
# Run-time:
BuildRequires:  paper
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(base)
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
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  diffutils
# Only for building
Provides:       bundled(gnulib)%(perl -ne 'if($. == 1 and /\A(\d+)-(\d+)-(\d+)/) {print qq{ = $1$2$3}}' %{_defaultdocdir}/gnulib/ChangeLog 2>/dev/null)
# psutils-perl was merged into psutils-2.03-1.fc34
Provides:       %{name}-perl = %{version}-%{release}
Obsoletes:      %{name}-perl < %{version}-%{release}
Requires:       paper

# Filter private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(PSUtils\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(PSUtils\\)

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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a aclocal.m4 build-aux config.status configure configure.ac m4 Makefile* tests %{buildroot}%{_libexecdir}/%{name}
printf '#!/bin/sh\nexec "$@"\n' > %{buildroot}%{_libexecdir}/%{name}/pre-inst-env
chmod +x %{buildroot}%{_libexecdir}/%{name}/pre-inst-env
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Makefile writes into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset PSUTILS_UNINSTALLED
make -j "$(getconf _NPROCESSORS_ONLN)" check-TESTS
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset PSUTILS_UNINSTALLED
make check %{?_smp_mflags}

%files
%license COPYING
# ChangeLog is not helpful
# old-scripts excluded intentionally
%doc README
%{_bindir}/epsffit
%{_bindir}/extractres
%{_bindir}/includeres
%{_bindir}/psbook
%{_bindir}/psjoin
%{_bindir}/psnup
%{_bindir}/psresize
%{_bindir}/psselect
%{_bindir}/pstops
%{_datadir}/%{name}
%{_mandir}/man1/epsffit.1*
%{_mandir}/man1/extractres.1*
%{_mandir}/man1/includeres.1*
%{_mandir}/man1/psbook.1*
%{_mandir}/man1/psjoin.1*
%{_mandir}/man1/psnup.1*
%{_mandir}/man1/psresize.1*
%{_mandir}/man1/psselect.1*
%{_mandir}/man1/pstops.1*
%{_mandir}/man1/psutils.1*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.10-10
- Prepare for Oreon 11 (RP1)
