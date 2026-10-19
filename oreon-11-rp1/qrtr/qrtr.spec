%global source0_hash 7a82bf80246fe71287b13c66c0466208822e8337fcd4aaf302eee6c5fcb48a52
Name:           qrtr
Version:        1.2
Release:        1%{?dist}
Summary:        Service listing daemon for Qualcomm IPC Router
License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://github.com/linux-msm/qrtr
Source0:        https://github.com/linux-msm/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      pd-mapper < 1.0-6
Provides:       pd-mapper < 1.0-6
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  systemd
# /oreon:deps
%description
This package provides the userspace component for the Qualcomm IPC Router
protocol, which maintains a service listing and allows peforming lookups.

%package        libs
Summary:        Shared libraries for %{name}
%description    libs
This packages provides shared libraries for %{name}.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
This packages provides development headers and libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dsystemd-unit-prefix=%{_unitdir} -Dqrtr-ns=disabled
%meson_build
%install
%meson_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n qrtr-libs -f %{oreon_filedir}/qrtr-libs.list
%files -n qrtr-devel -f %{oreon_filedir}/qrtr-devel.list

%changelog

%autochangelog
