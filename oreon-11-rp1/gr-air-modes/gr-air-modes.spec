%global source0_hash f2c355371827ecff026b91358ebbe2b1c1a0eb0d216bf2fa78a2c2261f6beb50
%global git_commit 9e2515a56609658f168f0c833a14ca4d2332713e
%global git_date 20200807
%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}
Name:             gr-air-modes
URL:              http://github.com/bistromath/gr-air-modes
Version:          3.6
Release:        1%{?dist}
License:          GPL-3.0-or-later
Requires:         python3-numpy
Requires:         python3-scipy
Requires:         python3-zmq
Summary:        SDR receiver for Mode S transponder signals (ADS-B)
Source0:        https://github.com/bistromath/%{name}/archive/%{git_commit}/%{name}-%{git_date}git%{git_short_commit}.tar.gz
Patch0:           gr-air-modes-0-gnuradio-3.9.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gnuradio-devel
BuildRequires:  graphviz
BuildRequires:  libunwind-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-PyQt4-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pyqtgraph
BuildRequires:  python3-scipy
BuildRequires:  python3-zmq
BuildRequires:  spdlog-devel
BuildRequires:  sqlite-devel
BuildRequires:  uhd-devel
# /oreon:deps
%description
Software defined radio receiver for Mode S transponder signals, including
ADS-B reports.

%package devel
Summary:          Development files for gr-air-modes
Requires:         %{name} = %{version}-%{release}
%description devel
Development files for gr-air-modes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_commit}

%build

%cmake
%cmake_build
%install
%cmake_install
pushd %{buildroot}%{python3_sitearch}/air_modes
for f in *.py
do
  sed -i '/^[ \t]*#!\/usr\/bin\/\(env\|python\)/ d' $f
done
popd
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gr-air-modes-devel -f %{oreon_filedir}/gr-air-modes-devel.list

%changelog

%autochangelog
