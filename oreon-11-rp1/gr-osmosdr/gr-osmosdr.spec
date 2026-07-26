%global source0_hash c9c99cae27cbadd0a5eabd5eb28bc5d8179cede12a8ab3b3a594fe932c46c97c

#%%global git_commit 2fedabec385a91af71468b179f0050f74e17f51e
#%%global git_date 20231108

#%%global git_short_commit %%(echo %%{git_commit} | cut -c -8)
#%%global git_suffix %%{git_date}git%%{git_short_commit}

%{?filter_setup:
%filter_provides_in %{python3_sitearch}/osmosdr/.*\.so$
%filter_setup
}

Name:          gr-osmosdr
URL:           http://sdr.osmocom.org/trac/wiki/GrOsmoSDR
Version:       0.2.5
Release:       25%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: gnuradio-devel
BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: pybind11-devel
BuildRequires: libunwind-devel
BuildRequires: rtl-sdr-devel
BuildRequires: uhd-devel
BuildRequires: hackrf-devel
BuildRequires: gr-funcube-devel
BuildRequires: gmp-devel
BuildRequires: gr-iqbal-devel
BuildRequires: airspyone_host-devel
BuildRequires: SoapySDR-devel
BuildRequires: python3-mako
# gnuradio dependency
BuildRequires: spdlog-devel
BuildRequires: fftw-devel
BuildRequires: libosmo-dsp-devel
BuildRequires: libsndfile-devel
BuildRequires: python3-six
Summary:       Common software API for various radio hardware
#Source0:       https://github.com/osmocom/gr-osmosdr/archive/%%{git_commit}/%%{name}-%%{git_commit}.tar.gz
#Source0:       https://github.com/osmocom/gr-osmosdr/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0:        https://gitea.osmocom.org/sdr/gr-osmosdr/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://osmocom.org/issues/5144
Patch0:        gr-osmosdr-0.2.3-airspy-multi-dev.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:   %{ix86}

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

%files
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%doc AUTHORS COPYING
%{_bindir}/*
%{_libdir}/*.so.*
%{python3_sitearch}/osmosdr
%{_datadir}/gnuradio/grc/blocks/*

%files devel
%{_includedir}/osmosdr
%{_libdir}/*.so
%{_libdir}/cmake/osmosdr/*.cmake

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
%autochangelog
