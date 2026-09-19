%global source0_hash 2609e325b7da42acf54dc67c7cdf780351cf58073c7c4088ac39d67c6e7c0103

%{!?dnf_lowest_compatible: %global dnf_lowest_compatible 4.2.23}
%global srcname perfmetrics

%global _description %{expand:
This plug-in will record performance metrics for DNF and store them in JSON
files under /var/log/dnf/perfmetrics.}

Name:           dnf-plugin-%{srcname}
Version:        1.0
Release:        %autorelease
Summary:        DNF plugin for Performance Metrics
License:        GPL-2.0-or-later
BuildArch:      noarch
URL:            https://github.com/filbranden/dnf-plugins-perfmetrics
Source0:        %{url}/archive/v%{version}/dnf-plugins-%{srcname}-%{version}.tar.gz
# Don't use the deprecated Python distutils module in CMake
Patch0:         %{url}/commit/9243a252c1d8bf64bc71afdf5de378eca4236ea5.patch

BuildRequires:  cmake
BuildRequires:  python3-devel
BuildRequires:  python3-dnf >= %{dnf_lowest_compatible}
BuildRequires:  python3-psutil

%description    %{_description}

%package -n     python3-%{name}
Summary:        %{summary}
Requires:       python3-dnf >= %{dnf_lowest_compatible}
Requires:       python3-psutil

%description -n python3-%{name} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n dnf-plugins-%{srcname}-%{version} -p1

%build
%cmake
%cmake_build

%install
%cmake_install
install -Ddpm0755 %{buildroot}%{_localstatedir}/log/dnf/perfmetrics

%files -n       python3-%{name}
%license COPYING
%doc README.md
%{python3_sitelib}/dnf-plugins/%{srcname}.py
%{python3_sitelib}/dnf-plugins/__pycache__/*
%config(noreplace) %{_sysconfdir}/dnf/plugins/%{srcname}.conf
%dir %{_localstatedir}/log/dnf/perfmetrics

%changelog
%autochangelog
