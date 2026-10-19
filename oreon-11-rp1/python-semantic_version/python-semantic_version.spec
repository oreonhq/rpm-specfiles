%global source0_hash e234480908f633d2d80fdd97e87699135b2ed2fc9876b7f41d1d4a2d3262a0c4
Name:           python-semantic_version
Version:        2.10.0
Release:        1%{?dist}
Summary:        Library implementing the 'SemVer' scheme
License:        BSD-2-Clause
URL:            https://github.com/rbarrois/python-semanticversion
Source0:        https://github.com/rbarrois/python-semanticversion/archive/refs/tags/2.10.0.tar.gz#/python-semanticversion-2.10.0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-semantic_version = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-semantic_version
Summary:        Library implementing the 'SemVer' scheme
%description -n python3-semantic_version

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir python-semanticversion-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-semantic_version usr/lib/python3*/site-packages/semantic_version* usr/lib64/python3*/site-packages/semantic_version* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/semantic_version* usr/lib64/python3*/site-packages/semantic_version* usr/bin/*

%check

%pytest
%files
%files -n python3-semantic_version -f %{oreon_filedir}/python3-semantic_version.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.10.0-1
- Prepare for Oreon 11 (RP1)
