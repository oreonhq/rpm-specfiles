%global source0_hash 1b8179eb8f9c9c46bec055f57a89cdb9e031ca6bfdf9ab92e5b86fb3f9849c88
Name:          gr-hpsdr
URL:           https://github.com/Tom-McDermott/gr-hpsdr
Version:       3.0
Release:        1%{?dist}
License:       GPL-3.0-or-later
Summary:        GNU Radio modules for OpenHPSDR Hermes / Metis and Red Pitaya
Source0:        https://github.com/Tom-McDermott/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:        gr-hpsdr-3.0-soname-fix.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  boost-filesystem
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gnuradio-devel
BuildRequires:  libunwind-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  spdlog-devel
# /oreon:deps
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
%description doc
Documentation files for gr-hpsdr.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%{_docdir}/%{name}
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gr-hpsdr-devel -f %{oreon_filedir}/gr-hpsdr-devel.list
%files -n gr-hpsdr-doc -f %{oreon_filedir}/gr-hpsdr-doc.list

%changelog

%autochangelog
