%global source0_hash 1b8179eb8f9c9c46bec055f57a89cdb9e031ca6bfdf9ab92e5b86fb3f9849c88

Name:          gr-hpsdr
URL:           https://github.com/Tom-McDermott/gr-hpsdr
Version:       3.0
Release:       41%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gnuradio-devel
BuildRequires: cppunit-devel
BuildRequires: doxygen
BuildRequires: pybind11-devel
BuildRequires: boost-filesystem
BuildRequires: boost-devel
BuildRequires: python3-devel
# gnuradio dependency
BuildRequires: spdlog-devel
BuildRequires: gmp-devel
BuildRequires: libunwind-devel
Summary:       GNU Radio modules for OpenHPSDR Hermes / Metis and Red Pitaya
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/Tom-McDermott/gr-hpsdr/issues/18
Patch0:        gr-hpsdr-3.0-soname-fix.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
GNU Radio modules for OpenHPSDR Hermes / Metis and Red Pitaya using the
OpenHpsdr protocol.

%package devel
Summary:          Development files for gr-hpsdr
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for gr-hpsdr.

%package doc
Summary:          Documentation files for gr-hpsdr
Requires:         %{name} = %{version}-%{release}
# Workaround for doxygen bug?
#BuildArch:        noarch

%description doc
Documentation files for gr-hpsdr.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%{_docdir}/%{name}
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%license license.txt
%doc README.md

%{_libdir}/*.so.*
%{python3_sitearch}/hpsdr
%{_datadir}/gnuradio/grc/blocks/*

%files devel
%{_includedir}/hpsdr
%{_libdir}/*.so
%{_libdir}/cmake/hpsdr

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
%autochangelog
