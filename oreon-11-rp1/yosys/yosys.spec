%global source0_hash 5f180b52ec87f9c696dc1acc705b7e05aa4b7e5fd824f1a45f4fe2c06c9e884e

%global commit0 3bc26ff4d055adfbba8b424508ab4a36405ffc0b
%global shortcommit0 %%(c=%%{commit0}; echo ${c:0:7})

%global snapdate 20260304

Name:           yosys
Version:        0.63
Release:        1.%{snapdate}git%{shortcommit0}%{?dist}
Summary:        Yosys Open SYnthesis Suite, including Verilog synthesizer
License:        ISC and MIT
URL:            http://www.clifford.at/yosys/

Source0:        https://github.com/YosysHQ/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Source1:        https://github.com/mdaines/viz.js/releases/download/0.0.3/viz.js

# man pages written for Debian:
Source2:        http://http.debian.net/debian/pool/main/y/yosys/yosys_0.52-2.debian.tar.xz
# requested that upstream include those man pages:
#   https://github.com/YosysHQ/yosys/issues/278

# Fedora-specific patch:
# Change the substitution done when making yosys-config so that it outputs
# CXXFLAGS with -I/usr/include/yosys
Patch1:         0001-fedora-yosys-cfginc-patch.patch

# Fedora-specific patch:
# When invoking yosys-config for examples in "make docs", need to use
# relative path for includes, as they're not installed in build host
# filesystem.
Patch2:         0002-fedora-yosys-mancfginc-patch.patch

# Fedora-specific patch:
# Use relative path (instead of assuming a bundled submodule) when
# referencing the cxxopts.hpp include file.
Patch3:         0003-fedora-yosys-cxxopts-patch.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  cxxopts-devel
BuildRequires:  bison flex readline-devel pkgconfig
BuildRequires:  tcl-devel libffi-devel
BuildRequires:  yosyshq-abc >= 0.63
BuildRequires:  iverilog >= 12.0
BuildRequires:  python%{python3_pkgversion}
BuildRequires:  python3-devel
BuildRequires:  txt2man
BuildRequires:  gtkwave
BuildRequires:  gtest-devel

# required for documentation:
BuildRequires: graphviz
BuildRequires: latexmk
BuildRequires: libfaketime
BuildRequires: pdf2svg
BuildRequires: python3-click
BuildRequires: python3-furo
BuildRequires: python3-sphinx-latex
BuildRequires: python3-sphinxcontrib-bibtex
BuildRequires: python3-sphinx-inline-tabs
BuildRequires: texlive-comment
BuildRequires: texlive-pgfplots
BuildRequires: texlive-standalone
BuildRequires: rsync

Requires:       %{name}-share = %{version}-%{release}
Requires:       graphviz python-click python-xdot
Requires:       yosyshq-abc >= 0.63

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval :
ExcludeArch: %{ix86}
# abc use broken on all Big Endian CPUs, specifically s390x (see BZ 1937362, 1937395):
ExcludeArch: s390x

%description
Yosys is a framework for Verilog RTL synthesis. It currently has
extensive Verilog-2005 support and provides a basic set of synthesis
algorithms for various application domains.

%package doc
Summary:        Documentation for Yosys synthesizer

%description doc
Documentation for Yosys synthesizer.

%package share
Summary:        Architecture-independent Yosys files
BuildArch:      noarch

%description share
Architecture-independent Yosys files.

%package devel
Summary:        Development files to build Yosys synthesizer plugins
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       tcl-devel

%description devel
Development files to build Yosys synthesizer plugins.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit0}

# Ensure that Makefile doesn't wget viz.js
cp %{SOURCE1} .

# Get man pages from Debian
%setup -q -T -D -a 2 -n %{name}-%{commit0}

# Remove '/usr/bin/env', without changing timestamps, in all python shebangs:
for f in `find . -name \*.py`
do
    sed 's|/usr/bin/env python3|/usr/bin/python3|' $f >$f.new
    touch -r $f $f.new
    mv $f.new $f
done

%build
make config-gcc
%make_build PREFIX="%{_prefix}" ABCEXTERNAL=%{_bindir}/abc PRETTY=0 all
#manual
make ABCEXTERNAL=%{_bindir}/abc DOC_TARGET=latexpdf SPHINXOPTS='' docs

date=$(stat -c %y debian/man/yosys-smtbmc.txt | cut -d' ' -f1)
txt2man -d $date -t YOSYS-SMTBMC debian/man/yosys-smtbmc.txt >yosys-smtbmc.1

%install
%make_install PREFIX="%{_prefix}" ABCEXTERNAL=%{_bindir}/abc STRIP=/bin/true

# move include files to includedir
install -d -m0755 %{buildroot}%{_includedir}
mv %{buildroot}%{_datarootdir}/%{name}/include %{buildroot}%{_includedir}/%{name}

# install man mages
install -d -m0755 %{buildroot}%{_mandir}/man1
install -m 0644 yosys-smtbmc.1 debian/yosys{,-config,-filterlib}.1 %{buildroot}%{_mandir}/man1

# install documentation
install -d -m0755 %{buildroot}%{_docdir}/%{name}
install -m 0644 docs/build/latex/yosyshqyosys.pdf %{buildroot}%{_docdir}/%{name}

%py_byte_compile %{python3} %{buildroot}%{_datadir}/yosys/python3

%check
make test ABCEXTERNAL=%{_bindir}/abc SEED=314159265359

%files
# license texts requested upstream:
#   https://github.com/YosysHQ/yosys/issues/263
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-filterlib
%{_bindir}/%{name}-smtbmc
%{_bindir}/%{name}-witness
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-filterlib.1*
%{_mandir}/man1/%{name}-smtbmc.1*

%files share
%{_datarootdir}/%{name}

%files doc
%{_docdir}/%{name}

%files devel
%{_bindir}/%{name}-config
%{_includedir}/%{name}
%{_mandir}/man1/%{name}-config.1*

%changelog
%autochangelog
