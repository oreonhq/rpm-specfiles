%global source0_hash 396570e51e95b2336f96fd84abfa063071cbdb98781e3fba9520da1406cb4cb2
%global git_commit cbda6c6cd5de9731734985aa6f67ea85a2b0e193
%global git_date 20240726
%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}
Name:          gr-funcube
URL:           https://github.com/dl1ksv/gr-funcube
Version:       3.10.0~rc3^%{git_suffix}
Release:        1%{?dist}
License:       GPL-3.0-or-later
Obsoletes:     gr-fcdproplus < 3.8.0-5.20200807git06069c2e
Summary:        GNURadio support for FUNcube Dongle Pro and FUNcube Dongle Pro+
Source0:        https://github.com/dl1ksv/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
Source1:       10-funcube.rules
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gnuradio-devel
BuildRequires:  graphviz
BuildRequires:  hidapi-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libunwind-devel
BuildRequires:  libusbx-devel
BuildRequires:  portaudio-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  spdlog-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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

%install
%cmake_install
install -Dpm 0644 %{S:1} %{buildroot}%{_udevrulesdir}/10-funcube.rules
install -m0644 -D gr-funcube.sysusers.conf %{buildroot}%{_sysusersdir}/gr-funcube.conf
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gr-funcube-devel -f %{oreon_filedir}/gr-funcube-devel.list
%files -n gr-funcube-doc -f %{oreon_filedir}/gr-funcube-doc.list

%changelog

%autochangelog
