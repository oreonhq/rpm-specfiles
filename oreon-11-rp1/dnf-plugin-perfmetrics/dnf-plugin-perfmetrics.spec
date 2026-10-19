%global source0_hash 2609e325b7da42acf54dc67c7cdf780351cf58073c7c4088ac39d67c6e7c0103
%{!?dnf_lowest_compatible: %global dnf_lowest_compatible 4.2.23}
%global srcname perfmetrics
Name:           dnf-plugin-%{srcname}
Version:        1.0
Release:        1%{?dist}
Summary:        DNF plugin for Performance Metrics
License:        GPL-2.0-or-later
BuildArch:      noarch
URL:            https://github.com/filbranden/dnf-plugins-perfmetrics
Source0:        https://github.com/filbranden/dnf-plugins-%{srcname}/archive/v%{version}/dnf-plugins-%{srcname}-%{version}.tar.gz
Patch0:         %{url}/commit/9243a252c1d8bf64bc71afdf5de378eca4236ea5.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  python3-devel
BuildRequires:  python3-dnf
BuildRequires:  python3-psutil
# /oreon:deps
%description

%package -n     python3-%{name}
Summary:        DNF plugin for Performance Metrics
Requires:       python3-dnf >= %{dnf_lowest_compatible}
Requires:       python3-psutil
%description -n python3-%{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n dnf-plugins-%{srcname}-%{version} -p1

%build

%cmake
%cmake_build
%install
%cmake_install
install -Ddpm0755 %{buildroot}%{_localstatedir}/log/dnf/perfmetrics
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-dnf-plugin-perfmetrics -f %{oreon_filedir}/python3-dnf-plugin-perfmetrics.list

%changelog

%autochangelog
