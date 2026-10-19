%global source0_hash none
%{!?dnf_lowest_compatible: %global dnf_lowest_compatible 4.2.23}
%global srcname flunk_dependent_remove
Name:           dnf-plugin-%{srcname}
Version:        1.0
Release:        1%{?dist}
Summary:        DNF plugin to prevent removing packages recursively via automation
License:        GPL-2.0-only
BuildArch:      noarch
Source0:        %{srcname}.py
Source1:        LICENSE
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-dnf
# /oreon:deps
%description

%package -n     python3-%{name}
Summary:        DNF plugin to prevent removing packages recursively via automation
Requires:       python3-dnf >= %{dnf_lowest_compatible}
%description -n python3-%{name}

%prep

cp -p %SOURCE1 .

%install
install -D -m0644 %{SOURCE0} \
  %{buildroot}/%{python3_sitelib}/dnf-plugins/%{srcname}.py
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-dnf-plugin-flunk_dependent_remove -f %{oreon_filedir}/python3-dnf-plugin-flunk_dependent_remove.list

%changelog

%autochangelog
