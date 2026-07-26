%global source0_hash f2c355371827ecff026b91358ebbe2b1c1a0eb0d216bf2fa78a2c2261f6beb50

# git ls-remote git://github.com/bistromath/gr-air-modes.git
%global git_commit 9e2515a56609658f168f0c833a14ca4d2332713e
%global git_date 20200807

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:             gr-air-modes
URL:              http://github.com/bistromath/gr-air-modes
Version:          0
Release:          0.123.%{git_suffix}%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:          GPL-3.0-or-later
BuildRequires:    cmake
BuildRequires:    gcc-c++
BuildRequires:    python3-devel
BuildRequires:    python3-numpy
BuildRequires:    python3-scipy
BuildRequires:    gnuradio-devel
BuildRequires:    sqlite-devel
BuildRequires:    uhd-devel
BuildRequires:    boost-devel
BuildRequires:    graphviz
BuildRequires:    python3-zmq
BuildRequires:    gmp-devel
BuildRequires:    python3-pyqtgraph
BuildRequires:    libunwind-devel
BuildRequires:    pybind11-devel
BuildRequires:    python3-PyQt4-devel
# gnuradio dependency
BuildRequires:    spdlog-devel
# TODO: check whether qwt is needed
# needs porting to qt5
#BuildRequires:    qwt-qt5-devel
Requires:         python3-numpy
Requires:         python3-scipy
Requires:         python3-zmq
# TODO: needs porting to qt5
#Requires:         qwt-qt5
Summary:          SDR receiver for Mode S transponder signals (ADS-B)
Source0:          https://github.com/bistromath/gr-air-modes/archive/%{git_commit}/%{name}-%{git_suffix}.tar.gz
# https://github.com/bistromath/gr-air-modes/issues/111
Patch0:           gr-air-modes-0-gnuradio-3.9.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

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

# remove hashbangs
pushd %{buildroot}%{python3_sitearch}/air_modes
for f in *.py
do
  sed -i '/^[ \t]*#!\/usr\/bin\/\(env\|python\)/ d' $f
done
popd

%ldconfig_scriptlets

%files
%doc COPYING README
%{_bindir}/uhd_modes.py
%{_bindir}/modes_gui
%{_bindir}/modes_rx
%{_libdir}/*.so.*
%{python3_sitearch}/*

%files devel
%{_includedir}/gr_air_modes
%{_libdir}/*.so
%{_libdir}/cmake/{air_modes,gr-air_modes}/*.cmake

%changelog
%autochangelog
