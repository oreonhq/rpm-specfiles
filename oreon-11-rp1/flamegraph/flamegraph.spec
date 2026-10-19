%global source0_hash b1ba3aaaf296ab72ced4dca84514377a4b2c8122831d743f726c106d3d339c2a
%global commit      41fee1f99f9276008b7cd112fca19dc3ea84ac32
%global date        20241020
%global forgeurl    https://github.com/brendangregg/FlameGraph
%bcond_without php
Name:           flamegraph
Version:        1.0
Summary:        Stack trace visualizer
%forgemeta
Release:        1%{?dist}
License:        CDDL-1.0
URL:            http://www.brendangregg.com/flamegraphs.html
VCS:            git:%{forgeurl}.git
Source0:        %{forgeurl}/archive/%{commit}/FlameGraph-%{commit}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  help2man
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(open)
BuildRequires:  perl-generators
BuildRequires:  php-cli
BuildRequires:  python3-devel
# /oreon:deps
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
License:        CDDL-1.0 AND Apache-2.0 AND BSD-2-Clause AND GPL-2.0-or-later
Requires:       %{name} = %{version}-%{release}
%description    stackcollapse
A set of scripts that collapse stack traces produced by various tools for
consumption by flamegraph, as well as some miscellaneous support scripts.

%package        stackcollapse-perf
Summary:        Stack collapser for perf output
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
mkdir -p %{buildroot}%{_bindir}
cp -p *.{awk,pl,py} jmaps %{buildroot}%{_bindir}
%if %{with php}
cp -p *.php %{buildroot}%{_bindir}
%endif
mkdir -p %{buildroot}%{_mandir}/man1
cp -p *.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

sed -i 's/ pid tid//' test.sh
./test.sh
%files -f %{oreon_filedir}/main.list
%files -n flamegraph-demos -f %{oreon_filedir}/flamegraph-demos.list
%files -n flamegraph-stackcollapse -f %{oreon_filedir}/flamegraph-stackcollapse.list
%files -n flamegraph-stackcollapse-perf -f %{oreon_filedir}/flamegraph-stackcollapse-perf.list
%files -n flamegraph-stackcollapse-php -f %{oreon_filedir}/flamegraph-stackcollapse-php.list

%changelog

%autochangelog
