%global source0_hash b1ba3aaaf296ab72ced4dca84514377a4b2c8122831d743f726c106d3d339c2a

# Upstream has only made one release, but there have been lots of bug fixes
# since, so we use a git checkout.
%global commit      41fee1f99f9276008b7cd112fca19dc3ea84ac32
%global date        20241020
%global forgeurl    https://github.com/brendangregg/FlameGraph

%if 0%{?fedora} >= 41
%ifarch %{ix86}
%bcond_with    php
%else
%bcond_without php
%endif
%else
%bcond_without php
%endif

# The subpackage layout was designed with the following points in mind:
# 1. The scripts are very small, so packing them together doesn't hurt much.
#    On the other hand, doing a fine-grained separation into subpackages
#    results in the metadata taking up a huge percentage of the packages.
# 2. The demo graphs are large, on the other hand, and few people will want to
#    see them, so they get their own package.
# 3. Most users only want flamegraph.pl, so it gets its own package.
# 4. The perf scripts have an external dependency on binutils, and the php
#    script has an external dependency on php, so they get their own packages.
# 5. All the rest are lumped together, due to the considerations in #1.  They
#    have varying licenses and purposes, it is true, but we lump them together
#    anyway for space efficiency reasons.

Name:           flamegraph
Version:        1.0
Summary:        Stack trace visualizer

%forgemeta

Release:        23%{?dist}
License:        CDDL-1.0
URL:            http://www.brendangregg.com/flamegraphs.html
VCS:            git:%{forgeurl}.git
Source:         %{forgesource}
BuildArch:      noarch

BuildRequires:  help2man
BuildRequires:  perl-generators
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(open)
BuildRequires:  python3-devel

%description
Flame graphs visualize profiled code.  Stack samples can be captured using
Linux perf_events, FreeBSD pmcstat (hwpmc), DTrace, SystemTap, and many other
profilers.  This package contains only the visualizer script, flamegraph.pl.

%package        demos
Summary:        Demos of graphs produced by flamegraph

%description    demos
Demonstration graphs produced by flamegraph.

%package        stackcollapse
Summary:        Stack collapsers and support scripts
# The project as a whole is CDDL-1.0.  Exceptions to this license are:
# Apache-2.0: files.pl
# BSD-2-Clause: stackcollapse-pmc.pl, stackcollapse-sample.awk
# GPL-2.0-or-later: difffolded.pl, stackcollapse-bpftrace.pl,
#     stackcollapse-go.pl, stackcollapse-jstack.pl
License:        CDDL-1.0 AND Apache-2.0 AND BSD-2-Clause AND GPL-2.0-or-later
Requires:       %{name} = %{version}-%{release}

%description    stackcollapse
A set of scripts that collapse stack traces produced by various tools for
consumption by flamegraph, as well as some miscellaneous support scripts.

%package        stackcollapse-perf
Summary:        Stack collapser for perf output
# pkgsplit-perf.pl and range-perf.pl are Apache-2.0.
# The rest are CDDL-1.0.
License:        CDDL-1.0 AND Apache-2.0
Requires:       %{name} = %{version}-%{release}
Requires:       binutils

%description    stackcollapse-perf
Scripts for collapsing perf output for consumption by flamegraph.

%if %{with php}
%package        stackcollapse-php
Summary:        Stack collapser for PHP
License:        GPL-2.0-or-later
BuildRequires:  php-cli
Requires:       %{name} = %{version}-%{release}

%description    stackcollapse-php
A script for collapsing PHP trace output for consumption by flamegraph.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Do not use env
sed -i.orig 's,bin/env ,bin/,' stackcollapse-pmc.pl
fixtimestamp stackcollapse-pmc.pl

# Fix end of line encodings
sed -i.orig 's/\r//' stackcollapse-vtune.pl
fixtimestamp stackcollapse-vtune.pl

# Add missing executable bits
chmod a+x stackcollapse-ibmjava.pl stackcollapse-vtune.pl

# Fix python shebangs
%py3_shebang_fix *.py

%build
# Build man pages.  Some scripts produce no useful output with --help.
HELP2MANFLAGS="-N --version-string=%{version} --no-discard-stderr"
for fil in aix-perf.pl difffolded.pl files.pl flamegraph.pl range-perf.pl \
           stackcollapse-chrome-tracing.py stackcollapse-elfutils.pl \
           stackcollapse-go.pl stackcollapse-ibmjava.pl \
           stackcollapse-java-exceptions.pl stackcollapse-jstack.pl \
           stackcollapse-perf.pl stackcollapse-vtune-mc.pl \
%if %{with php}
           stackcollapse-xdebug.php \
%endif
           ; do
  help2man $HELP2MANFLAGS ./$fil > $fil.1
done

%install
# Install the scripts
mkdir -p %{buildroot}%{_bindir}
cp -p *.{awk,pl,py} jmaps %{buildroot}%{_bindir}
%if %{with php}
cp -p *.php %{buildroot}%{_bindir}
%endif

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -p *.1 %{buildroot}%{_mandir}/man1

%check
# The output of the pid and tid tests depends on the architecture on which
# the tests are run, and the JDK version.  Skip those tests.
sed -i 's/ pid tid//' test.sh
./test.sh

%files
%doc README.md
%license docs/cddl1.txt
%{_bindir}/flamegraph.pl
%{_mandir}/man1/flamegraph.pl.1*

%files          demos
%doc demos/*

%files          stackcollapse
%{_bindir}/difffolded.pl
%{_bindir}/files.pl
%{_bindir}/jmaps
%{_bindir}/stackcollapse.pl
%{_bindir}/stackcollapse-aix.pl
%{_bindir}/stackcollapse-bpftrace.pl
%{_bindir}/stackcollapse-chrome-tracing.py
%{_bindir}/stackcollapse-elfutils.pl
%{_bindir}/stackcollapse-faulthandler.pl
%{_bindir}/stackcollapse-gdb.pl
%{_bindir}/stackcollapse-go.pl
%{_bindir}/stackcollapse-ibmjava.pl
%{_bindir}/stackcollapse-instruments.pl
%{_bindir}/stackcollapse-java-exceptions.pl
%{_bindir}/stackcollapse-jstack.pl
%{_bindir}/stackcollapse-ljp.awk
%{_bindir}/stackcollapse-pmc.pl
%{_bindir}/stackcollapse-recursive.pl
%{_bindir}/stackcollapse-sample.awk
%{_bindir}/stackcollapse-stap.pl
%{_bindir}/stackcollapse-vsprof.pl
%{_bindir}/stackcollapse-vtune.pl
%{_bindir}/stackcollapse-vtune-mc.pl
%{_bindir}/stackcollapse-wcp.pl
%{_mandir}/man1/difffolded.pl.1*
%{_mandir}/man1/files.pl.1*
%{_mandir}/man1/stackcollapse-chrome-tracing.py.1*
%{_mandir}/man1/stackcollapse-elfutils.pl.1*
%{_mandir}/man1/stackcollapse-go.pl.1*
%{_mandir}/man1/stackcollapse-ibmjava.pl.1*
%{_mandir}/man1/stackcollapse-java-exceptions.pl.1*
%{_mandir}/man1/stackcollapse-jstack.pl.1*
%{_mandir}/man1/stackcollapse-perf.pl.1*
%{_mandir}/man1/stackcollapse-vtune-mc.pl.1*

%files          stackcollapse-perf
%{_bindir}/aix-perf.pl
%{_bindir}/pkgsplit-perf.pl
%{_bindir}/range-perf.pl
%{_bindir}/stackcollapse-perf.pl
%{_bindir}/stackcollapse-perf-sched.awk
%{_mandir}/man1/aix-perf.pl.1*
%{_mandir}/man1/range-perf.pl.1*
%{_mandir}/man1/stackcollapse-perf.pl.1*

%if %{with php}
%files          stackcollapse-php
%{_bindir}/stackcollapse-xdebug.php
%{_mandir}/man1/stackcollapse-xdebug.php.1*
%endif

%changelog
%autochangelog
