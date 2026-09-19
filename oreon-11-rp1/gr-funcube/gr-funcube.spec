%global source0_hash 396570e51e95b2336f96fd84abfa063071cbdb98781e3fba9520da1406cb4cb2

# git ls-remote git://github.com/dl1ksv/gr-funcube.git
%global git_commit cbda6c6cd5de9731734985aa6f67ea85a2b0e193
%global git_date 20240726

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:          gr-funcube
URL:           https://github.com/dl1ksv/gr-funcube
Version:       3.10.0~rc3^%{git_suffix}
Release:       13%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gnuradio-devel
BuildRequires: hidapi-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: pybind11-devel
BuildRequires: libunwind-devel
BuildRequires: alsa-lib-devel
BuildRequires: libusbx-devel
BuildRequires: python3-devel
# gnuradio dependency
BuildRequires: spdlog-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: portaudio-devel
BuildRequires: gmp-devel
BuildRequires: libsndfile-devel
# for _udevrulesdir macro
BuildRequires: systemd-rpm-macros
Obsoletes:     gr-fcdproplus < 3.8.0-5.20200807git06069c2e
Summary:       GNURadio support for FUNcube Dongle Pro and FUNcube Dongle Pro+
Source0:       %{url}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
Source1:       10-funcube.rules

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
GNURadio support for FUNcube Dongle Pro and FUNcube Dongle Pro+.

%package devel
Summary:       Development files for gr-funcube
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for gr-funcube.

%package doc
Summary:       Documentation files for gr-funcube
Requires:      %{name} = %{version}-%{release}
# Workaround for rhbz#1814356
#BuildArch:    noarch

%description doc
Documentation files for gr-funcube.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_commit}

# Create a sysusers.d config file
cat >gr-funcube.sysusers.conf <<EOF
g rtlsdr -
EOF

%build
%cmake -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%{_docdir}/%{name}
%cmake_build

%check
# Temporary disabled until resolved ppc64le problems
#cd %{_vpath_builddir}
#make test

%install
%cmake_install

# udev rule
install -Dpm 0644 %{S:1} %{buildroot}%{_udevrulesdir}/10-funcube.rules

install -m0644 -D gr-funcube.sysusers.conf %{buildroot}%{_sysusersdir}/gr-funcube.conf

%ldconfig_scriptlets

%files
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%license COPYING
%doc README.md
%{_libdir}/*.so.*
%{python3_sitearch}/funcube
%{_datadir}/gnuradio/grc/blocks/*
%{_udevrulesdir}/10-funcube.rules
%{_sysusersdir}/gr-funcube.conf

%files devel
%{_includedir}/funcube
%{_libdir}/*.so
%{_libdir}/cmake/funcube

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
%autochangelog
