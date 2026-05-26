%if 0%{?fedora} >= 44 || 0%{?rhel} >= 10
%global with_rules 0
%else
%global with_rules 1
%endif

Name:           cppcheck
Version:        2.20.0
Release:        1%{?dist}
Summary:        Tool for static C/C++ code analysis
License:        GPL-3.0-or-later
URL:            http://cppcheck.sourceforge.io/
Source0:        https://github.com/danmar/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Fix location of translations
Patch0:         cppcheck-2.11-translations.patch
# oreon url source checksums begin
%global source0_sha256 7be7992439339017edb551d8e7d2315f9bb57c402da50c2cee9cd0e2724600a1
%global source0_file 2.20.0.tar.gz
# oreon url source checksums end


BuildRequires:  gcc-c++
%if %{with_rules}
BuildRequires:  pcre-devel
%endif
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt
BuildRequires:  pandoc
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  tinyxml2-devel >= 2.1.0
BuildRequires:  zlib-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-linguist
BuildRequires:  make
BuildRequires:  boost-devel

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/2.20.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7be7992439339017edb551d8e7d2315f9bb57c402da50c2cee9cd0e2724600a1" || { echo "oreon: Source0 SHA256 mismatch for 2.20.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q
%patch -P 0 -p1 -b .translations
# Make sure bundled tinyxml2 is not used
rm -r externals/tinyxml2
# Generate the Qt online-help file
cd gui/help
$(qmake6 -query QT_HOST_LIBEXECS)/qhelpgenerator online-help.qhcp -o online-help.qhc

%build
# Manuals
make DB2MAN=/usr/share/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl man
pandoc man/manual.md -o man/manual.html -s --number-sections --toc
pandoc man/reference-cfg-format.md -o man/reference-cfg-format.html -s --number-sections --toc

# Binaries
# Upstream doesn't support shared libraries (unversioned solib)
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DUSE_MATCHCOMPILER=ON \
%if %{with_rules}
  -DHAVE_RULES=yes \
%else
  -DHAVE_RULES=no \
%endif
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
# Install desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/cppcheck-gui.desktop
# Install logo
install -D -p -m 644 gui/cppcheck-gui.png %{buildroot}%{_datadir}/pixmaps/cppcheck-gui.png
# Install the Qt online-help file
install -D -p -m 644 gui/help/online-help.qhc %{buildroot}%{_datadir}/Cppcheck/help/online-help.qhc
install -D -p -m 644 gui/help/online-help.qch %{buildroot}%{_datadir}/Cppcheck/help/online-help.qch
# Install htmlreport
install -D -p -m 755 htmlreport/cppcheck-htmlreport %{buildroot}%{_bindir}/cppcheck-htmlreport
# Restore execute permission of python files
grep -l "#\!/usr/bin/env python3" %{buildroot}%{_datadir}/Cppcheck/addons/*.py | xargs chmod +x

%check
# Ugh. -GC 2026-01-05
%ifnarch i686
# Do not run tests in parallel to avoid sometimes failing tests (observed under x86_64):
# TestCmdlineParser, TestCppcheck, TestFileLister, TestSettings, TestSuppressions
%ctest --parallel 1
%endif

%files
%doc AUTHORS man/manual.html man/reference-cfg-format.html
%license COPYING
%{_datadir}/Cppcheck/
%{_bindir}/cppcheck
%{_mandir}/man1/cppcheck.1*

%files gui
%{_bindir}/cppcheck-gui
%{_datadir}/applications/cppcheck-gui.desktop
%{_datadir}/pixmaps/cppcheck-gui.png
%{_datadir}/icons/hicolor/64x64/apps/cppcheck-gui.png
%{_datadir}/icons/hicolor/scalable/apps/cppcheck-gui.svg

%files htmlreport
%{_bindir}/cppcheck-htmlreport

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.20.0-1
- Prepare for Oreon 11 (RP1)
