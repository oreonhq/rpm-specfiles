%global source0_hash 0911e0161ea4c4df9b4c92e629de9e751b5940213a58a862821bcda6c72270c9
Name:           python-poi-tracker
Version:        0.0.1
Release:        1%{?dist}
Summary:        Tool for tracking packages of interest
License:        GPL-2.0-or-later
URL:            https://pagure.io/michel-slm/poi-tracker
Source0:        https://files.pythonhosted.org/packages/source/p/poi_tracker/poi_tracker-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-poi-tracker = %{version}-%{release}
# /oreon:deps
%description

%package -n     poi-tracker
Summary:        Tool for tracking packages of interest
%description -n poi-tracker

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir poi_tracker-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles poi-tracker usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%files
%files -n poi-tracker -f %{oreon_filedir}/poi-tracker.list

%changelog

%autochangelog
