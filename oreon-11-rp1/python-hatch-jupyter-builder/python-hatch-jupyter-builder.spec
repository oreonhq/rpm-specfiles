%global source0_hash 79278198d124c646b799c5e8dca8504aed9dcaaa88d071a09eb0b5c2009a58ad
Name:           python-hatch-jupyter-builder
Version:        0.9.1
Release:        1%{?dist}
Summary:        A hatch plugin to help build Jupyter packages
License:        BSD-3-Clause
URL:            https://pypi.org/project/hatch-jupyter-builder/
Source0:        https://files.pythonhosted.org/packages/source/h/hatch_jupyter_builder/hatch_jupyter_builder-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.3.1
BuildRequires:  python3dist(jupyterlab) == 3.*
Requires:       python3-hatch-jupyter-builder = %{version}-%{release}
# /oreon:deps
%package -n       python3-hatch-jupyter-builder+docs
Summary:        Metapackage for python3-hatch-jupyter-builder docs extras
Requires:       python3-hatch-jupyter-builder = %{version}-%{release}
Requires:       python3dist(sphinx) >= 1.5
Provides:       python3dist(hatch-jupyter-builder[docs]) = %{version}-%{release}

%description -n python3-hatch-jupyter-builder+docs
Metapackage for python3-hatch-jupyter-builder docs extras.

%package -n       python3-hatch-jupyter-builder+examples
Summary:        Metapackage for python3-hatch-jupyter-builder examples extras
Requires:       python3-hatch-jupyter-builder = %{version}-%{release}
Provides:       python3dist(hatch-jupyter-builder[examples]) = %{version}-%{release}

%description -n python3-hatch-jupyter-builder+examples
Metapackage for python3-hatch-jupyter-builder examples extras.

%package -n       python3-hatch-jupyter-builder+test
Summary:        Metapackage for python3-hatch-jupyter-builder test extras
Requires:       python3-hatch-jupyter-builder = %{version}-%{release}
Requires:       python3dist(pytest) >= 4.6
Provides:       python3dist(hatch-jupyter-builder[test]) = %{version}-%{release}

%description -n python3-hatch-jupyter-builder+test
Metapackage for python3-hatch-jupyter-builder test extras.

%description

%package -n     python3-hatch-jupyter-builder
Summary:        A hatch plugin to help build Jupyter packages
# oreon:reqs
Requires:       python3dist(ipywidgets) >= 7.0.0
# /oreon:reqs
%description -n python3-hatch-jupyter-builder

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir hatch_jupyter_builder-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-hatch-jupyter-builder usr/lib/python3*/site-packages/hatch_jupyter_builder* usr/lib64/python3*/site-packages/hatch_jupyter_builder* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/hatch_jupyter_builder* usr/lib64/python3*/site-packages/hatch_jupyter_builder* usr/bin/*

%check

%pytest -k "not test_hatch_build"
%files
%files -n python3-hatch-jupyter-builder -f %{oreon_filedir}/python3-hatch-jupyter-builder.list

%changelog

%autochangelog
