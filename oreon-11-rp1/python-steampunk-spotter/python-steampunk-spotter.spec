%global source0_hash 209a0f9d1139bc1e734bd88786cb75865b5a9c6a67d650c8ae41accca03324bb
%{?!python3_pkgversion:%global python3_pkgversion 3}
%global srcname steampunk-spotter
%bcond check 1
Name:           python-%{srcname}
Version:        6.5.0
Release:        1%{?dist}
Summary:        Scan, analyze, enhance, and provide insights for your playbooks using Spotter
License:        Apache-2.0
URL:            https://spotter.steampunk.si/
Source0:        https://gitlab.com/xlab-steampunk/steampunk-spotter-client/spotter-cli/-/archive/%{version}/spotter-cli-%{version}.tar.bz2
BuildArch:      noarch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-steampunk-spotter = %{version}-%{release}
# /oreon:deps
%description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Scan, analyze, enhance, and provide insights for your playbooks using Spotter
%description -n python%{python3_pkgversion}-%{srcname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n spotter-cli-%{version}
# work around _ ERROR collecting tests/integration/scan_export_collection_exclude/collection/library/test_info.py _ import file mismatch
mv tests/integration/scan_export_collection_exclude/collection/library/test_info{,_exclude}.py

%build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/steampunk_spotter* usr/lib64/python3*/site-packages/steampunk_spotter* usr/bin/*

%check

%pyproject_check_import
%if %{with check}
%pytest
%endif
%files
%files -n python3-steampunk-spotter -f %{oreon_filedir}/python3-steampunk-spotter.list

%changelog

%autochangelog
