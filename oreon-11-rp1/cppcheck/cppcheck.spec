%global source0_hash d74945deb2d50393430e07596b766f8a779512c7f60dac2a30ea64e059ece57b
%if 0%{?fedora} >= 44 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%global with_rules 0
%else
%global with_rules 1
%endif
Name:           cppcheck
Version:        2.22.0
Release:        1%{?dist}
Summary:        Tool for static C/C++ code analysis
License:        GPL-3.0-or-later
URL:            http://cppcheck.sourceforge.io/
Source0:        https://github.com/danmar/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         cppcheck-2.11-translations.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Cppcheck is a static analysis tool for C/C++ code. Unlike C/C++
compilers and many other analysis tools it does not detect syntax
errors in the code. Cppcheck primarily detects the types of bugs that
the compilers normally do not detect. The goal is to detect only real
errors in the code (i.e. have zero false positives).

%package gui
Summary:        Graphical user interface for cppcheck
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description gui
This package contains the graphical user interface for cppcheck.

%package htmlreport
Summary:        HTML reporting for cppcheck
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-pygments
%description htmlreport
This package contains the Python utility for generating html reports
from xml files first generated using cppcheck.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P 0 -p1 -b .translations
# Make sure bundled tinyxml2 is not used
rm -r externals/tinyxml2
# Generate the Qt online-help file
cd gui/help
$(qmake6 -query QT_HOST_LIBEXECS)/qhelpgenerator online-help.qhcp -o online-help.qhc

%build

make DB2MAN=/usr/share/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl man
pandoc man/manual.md -o man/manual.html -s --number-sections --toc
pandoc man/reference-cfg-format.md -o man/reference-cfg-format.html -s --number-sections --toc
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DUSE_MATCHCOMPILER=ON \
  -DHAVE_RULES=yes \
  -DBUILD_GUI=1 \
  -DUSE_QT6=1 \
  -DBUILD_SHARED_LIBS:BOOL=OFF \
  -DBUILD_TESTS=yes \
  -DFILESDIR=%{_datadir}/Cppcheck \
  -DUSE_BUNDLED_TINYXML2=OFF \
  -DENABLE_OSS_FUZZ=OFF \
  -DUSE_BOOST=1
%ifarch i686
export RPM_BUILD_NCPUS=1
%endif
%cmake_build
%install
%cmake_install
install -D -p -m 644 cppcheck.1 %{buildroot}%{_mandir}/man1/cppcheck.1
desktop-file-validate %{buildroot}%{_datadir}/applications/cppcheck-gui.desktop
install -D -p -m 644 gui/cppcheck-gui.png %{buildroot}%{_datadir}/pixmaps/cppcheck-gui.png
install -D -p -m 644 gui/help/online-help.qhc %{buildroot}%{_datadir}/Cppcheck/help/online-help.qhc
install -D -p -m 644 gui/help/online-help.qch %{buildroot}%{_datadir}/Cppcheck/help/online-help.qch
install -D -p -m 755 htmlreport/cppcheck-htmlreport %{buildroot}%{_bindir}/cppcheck-htmlreport
grep -l "#\!/usr/bin/env python3" %{buildroot}%{_datadir}/Cppcheck/addons/*.py | xargs chmod +x
%oreon_autofiles cppcheck-gui usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cppcheck-htmlreport usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ifnarch i686
%ctest --parallel 1
%endif
%files -f %{oreon_filedir}/main.list
%files -n cppcheck-gui -f %{oreon_filedir}/cppcheck-gui.list
%files -n cppcheck-htmlreport -f %{oreon_filedir}/cppcheck-htmlreport.list

%changelog

%autochangelog
