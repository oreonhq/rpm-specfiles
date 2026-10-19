%global source0_hash b540b6bd4f88682840d52fcfaf55281bb8a5203abe388353bae9d3b0defeb5ae
Name:           python-docs-theme
Version:        2026.9.1
Release:        1%{?dist}
Summary:        The Sphinx theme for the CPython docs and related projects
License:        PSF-2.0
URL:            https://github.com/python/python-docs-theme/
Source0:        https://github.com/python/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-docs-theme = %{version}-%{release}
# /oreon:deps
%description
Python Docs Sphinx Theme is the theme for the Python documentation.

%package -n     python3-docs-theme
Summary:        The Sphinx theme for the CPython docs and related projects
# oreon:reqs
Requires:       python3dist(sphinx) >= 7.3
# /oreon:reqs
%description -n python3-docs-theme
Python Docs Sphinx Theme is the theme for the Python documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-docs-theme usr/lib/python3*/site-packages/docs_theme* usr/lib64/python3*/site-packages/docs_theme* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/docs_theme* usr/lib64/python3*/site-packages/docs_theme* usr/bin/*

%files
%files -n python3-docs-theme -f %{oreon_filedir}/python3-docs-theme.list

%changelog

%autochangelog
