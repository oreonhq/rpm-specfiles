%global source0_hash 26ef9df924cd874a825d92d6bc01a5a869a4a28d2f2ebba61d3b5b19c60120f0
%bcond bootstrap 0
Name:           python-poetry-plugin-export
Version:        1.10.0
Release:        1%{?dist}
Summary:        Poetry plugin to export the dependencies to various formats
License:        MIT
URL:            https://python-poetry.org/
Source0:        https://files.pythonhosted.org/packages/source/p/poetry_plugin_export/poetry_plugin_export-%{version}.tar.gz
BuildArch:      noarch
%if %{without bootstrap}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 2.0
Requires:       python3-poetry-plugin-export = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-poetry-plugin-export
Summary:        Poetry plugin to export the dependencies to various formats
# oreon:reqs
Requires:       python3dist(poetry) (>=2.1.0
Requires:       python3dist(poetry) < 3.0.0)
Requires:       python3dist(poetry-core) (>=2.1.0
Requires:       python3dist(poetry-core) < 3.0.0)
Requires:       python3dist(tomlkit) (>=0.11.4
Requires:       python3dist(tomlkit) < 1.0.0)
# /oreon:reqs
%description -n python3-poetry-plugin-export

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir poetry_plugin_export-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-poetry-plugin-export usr/lib/python3*/site-packages/poetry_plugin_export* usr/lib64/python3*/site-packages/poetry_plugin_export* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/poetry_plugin_export* usr/lib64/python3*/site-packages/poetry_plugin_export* usr/bin/*
%if %{without bootstrap}
%check

%pytest
%endif
%files
%files -n python3-poetry-plugin-export -f %{oreon_filedir}/python3-poetry-plugin-export.list

%changelog

%autochangelog
