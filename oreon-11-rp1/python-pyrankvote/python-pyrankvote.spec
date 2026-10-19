%global source0_hash e8a6c71035755a135c6baa150b523d497a9b5d0679cbf08d2f7facfdaee03103
Name:           python-pyrankvote
Version:        2.0.6
Release:        1%{?dist}
Summary:        Library for different ranked voting methods
License:        MIT
URL:            https://github.com/jontingvold/pyrankvote
Source0:        https://github.com/jontingvold/pyrankvote/archive/v%{version}/pyrankvote-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyrankvote = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyrankvote
Summary:        Library for different ranked voting methods
%description -n python3-pyrankvote

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pyrankvote-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyrankvote usr/lib/python3*/site-packages/pyrankvote* usr/lib64/python3*/site-packages/pyrankvote* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyrankvote* usr/lib64/python3*/site-packages/pyrankvote* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-pyrankvote -f %{oreon_filedir}/python3-pyrankvote.list

%changelog

%autochangelog
