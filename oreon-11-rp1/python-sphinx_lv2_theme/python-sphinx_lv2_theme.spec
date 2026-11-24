# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d524b3d2e568c115132a86e132ea95d403d3b3e79f5565e44c64931f1e23bb81
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global pypi_name sphinx_lv2_theme

%global common_description %{expand:
This is a minimal pure-CSS theme for Sphinx that uses the documentation
style of the LV2 plugin specification and related projects.

This theme is geared toward producing beautiful API documentation for C, C++,
and Python that is documented using the standard Sphinx domains.
The output does not use Javascript at all, and some common features are not
implemented, so this theme should not be considered a drop-in replacement
for typical Sphinx themes.}

Name:           python-%{pypi_name}
Version:        1.4.6
Release:        1%{?dist}
Summary:        A minimal pure-CSS theme for Sphinx
License:        ISC
URL:            https://gitlab.com/lv2/%{pypi_name}
Source0:        %{url}/-/archive/v%{version}/%{pypi_name}-v%{version}.tar.bz2

BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  python%{python3_pkgversion}-devel

%description %{common_description}

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{pypi_name} %{common_description}

%prep
%oreon_sha256
%autosetup -p1 -n %{pypi_name}-v%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n  python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
