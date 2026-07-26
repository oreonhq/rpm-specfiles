%global source0_hash none

%{!?dnf_lowest_compatible: %global dnf_lowest_compatible 4.2.23}
%global srcname flunk_dependent_remove

%global _description %{expand:
Do not allow "dnf -y remove" to expand the list of packages to remove to
include packages which require one of the explicitly listed packages.
Fail the request instead. This is implemented via a DNF plugin.}

Name:           dnf-plugin-%{srcname}
Version:        1.0
Release:        23%{?dist}
Summary:        DNF plugin to prevent removing packages recursively via automation
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
BuildArch:      noarch
Source0:        %{srcname}.py
Source1:        LICENSE
BuildRequires:  python3-devel
BuildRequires:  python3-dnf >= %{dnf_lowest_compatible}

%description    %{_description}

%package -n     python3-%{name}
Summary:        %{summary}
Requires:       python3-dnf >= %{dnf_lowest_compatible}

%description -n python3-%{name} %{_description}

%prep
cp -p %SOURCE1 .

%install
install -D -m0644 %{SOURCE0} \
  %{buildroot}/%{python3_sitelib}/dnf-plugins/%{srcname}.py

%files -n       python3-%{name}
%license LICENSE
%{python3_sitelib}/dnf-plugins/%{srcname}.py
%{python3_sitelib}/dnf-plugins/__pycache__/*

%changelog
%autochangelog
