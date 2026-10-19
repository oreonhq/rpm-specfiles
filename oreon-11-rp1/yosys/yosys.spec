%global source2_hash 5f180b52ec87f9c696dc1acc705b7e05aa4b7e5fd824f1a45f4fe2c06c9e884e
%global source1_hash 0eb4139c4a6067e73585338e32e9f7515490edd885d16147322a48e43b120012
%global source0_hash ec72812661d0385cb54b6bc37d5a0d7c6fc98cfe971365bf450a226c991b9c28
%global commit0 3bc26ff4d055adfbba8b424508ab4a36405ffc0b
%global shortcommit0 %%(c=%%{commit0}; echo ${c:0:7})
%global snapdate 20260304
Name:           yosys
Version:        0.69
Release:        1%{?dist}
Summary:        Yosys Open SYnthesis Suite, including Verilog synthesizer
License:        ISC and MIT
URL:            http://www.clifford.at/yosys/
Source0:        https://github.com/YosysHQ/%{name}/archive/%{commit0}/%{name}-3bc26ff.tar.gz
Source1:        https://github.com/mdaines/viz.js/releases/download/0.0.3/viz.js
Source2:        http://http.debian.net/debian/pool/main/y/yosys/yosys_0.52-2.debian.tar.xz
Patch1:         0001-fedora-yosys-cfginc-patch.patch
Patch2:         0002-fedora-yosys-mancfginc-patch.patch
Patch3:         0003-fedora-yosys-cxxopts-patch.patch
Requires:       %{name}-share = %{version}-%{release}
Requires:       graphviz python-click python-xdot
Requires:       yosyshq-abc >= 0.69
ExcludeArch: %{ix86}
ExcludeArch: s390x
# oreon:deps
BuildRequires:  bison
BuildRequires:  cxxopts-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  gtest-devel
BuildRequires:  gtkwave
BuildRequires:  iverilog
BuildRequires:  latexmk
BuildRequires:  libfaketime
BuildRequires:  libffi-devel
BuildRequires:  make
BuildRequires:  pdf2svg
BuildRequires:  pkgconfig
BuildRequires:  python3-click
BuildRequires:  python3-devel
BuildRequires:  python3-furo
BuildRequires:  python3-sphinx-inline-tabs
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-sphinxcontrib-bibtex
BuildRequires:  python3.15
BuildRequires:  readline-devel
BuildRequires:  rsync
BuildRequires:  tcl-devel
BuildRequires:  texlive-comment
BuildRequires:  texlive-pgfplots
BuildRequires:  texlive-standalone
BuildRequires:  txt2man
BuildRequires:  yosyshq-abc
# /oreon:deps
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
make ABCEXTERNAL=%{_bindir}/abc DOC_TARGET=latexpdf SPHINXOPTS='' docs
date=$(stat -c %y debian/man/yosys-smtbmc.txt | cut -d' ' -f1)
txt2man -d $date -t YOSYS-SMTBMC debian/man/yosys-smtbmc.txt >yosys-smtbmc.1
%install
%make_install PREFIX="%{_prefix}" ABCEXTERNAL=%{_bindir}/abc STRIP=/bin/true
install -d -m0755 %{buildroot}%{_includedir}
mv %{buildroot}%{_datarootdir}/%{name}/include %{buildroot}%{_includedir}/%{name}
install -d -m0755 %{buildroot}%{_mandir}/man1
install -m 0644 yosys-smtbmc.1 debian/yosys{,-config,-filterlib}.1 %{buildroot}%{_mandir}/man1
install -d -m0755 %{buildroot}%{_docdir}/%{name}
install -m 0644 docs/build/latex/yosyshqyosys.pdf %{buildroot}%{_docdir}/%{name}
%py_byte_compile %{python3} %{buildroot}%{_datadir}/yosys/python3
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make test ABCEXTERNAL=%{_bindir}/abc SEED=314159265359
%files -f %{oreon_filedir}/main.list
%files -n yosys-doc -f %{oreon_filedir}/yosys-doc.list
%files -n yosys-share -f %{oreon_filedir}/yosys-share.list
%files -n yosys-devel -f %{oreon_filedir}/yosys-devel.list

%changelog

%autochangelog
