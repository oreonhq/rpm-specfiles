%global source0_hash c9c99cae27cbadd0a5eabd5eb28bc5d8179cede12a8ab3b3a594fe932c46c97c
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/osmosdr/.*\.so$
%filter_setup
}
Name:          gr-osmosdr
URL:           http://sdr.osmocom.org/trac/wiki/GrOsmoSDR
Version:       0.2.6
Release:        1%{?dist}
License:       GPL-3.0-or-later
Summary:        Common software API for various radio hardware
Source0:        https://gitea.osmocom.org/sdr/gr-osmosdr/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:        gr-osmosdr-0.2.3-airspy-multi-dev.patch
ExcludeArch:   %{ix86}
# oreon:deps
BuildRequires:  SoapySDR-devel
BuildRequires:  airspyone_host-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gnuradio-devel
BuildRequires:  gr-funcube-devel
BuildRequires:  gr-iqbal-devel
BuildRequires:  graphviz
BuildRequires:  hackrf-devel
BuildRequires:  libosmo-dsp-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libunwind-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-mako
BuildRequires:  python3-six
BuildRequires:  rtl-sdr-devel
BuildRequires:  spdlog-devel
BuildRequires:  uhd-devel
# /oreon:deps
%description
Primarily gr-osmosdr supports the OsmoSDR hardware, but it also
offers a wrapper functionality for FunCube Dongle,  Ettus UHD
and rtl-sdr radios. By using gr-osmosdr source you can take
advantage of a common software api in your application(s)
independent of the underlying radio hardware.

%package devel
Summary:       Development files for gr-osmosdr
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for gr-osmosdr.

# Made doc arch due to bug in doxygen
%package doc
Summary:       Documentation files for gr-osmosdr
Requires:      %{name} = %{version}-%{release}
%description doc
Documentation files for gr-osmosdr.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#%%autosetup -p1 -n %%{name}-%%{git_commit}
#%%autosetup -p1
%autosetup -p1 -n %{name}

# TODO fix the lib location nicer way
sed -i 's|/lib/|/%{_lib}/|g' CMakeLists.txt

%build

%cmake -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%{_docdir}/%{name}
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gr-osmosdr-devel -f %{oreon_filedir}/gr-osmosdr-devel.list
%files -n gr-osmosdr-doc -f %{oreon_filedir}/gr-osmosdr-doc.list

%changelog

%autochangelog
