%global source0_hash faff25f77218335752f35f23c5fe6e4a392a7bd99a5939ccb9b8fbf594636cf3
Name:           python-jupyter-events
Version:        0.12.1
Release:        1%{?dist}
Summary:        Jupyter Event System library
License:        ...
URL:            http://jupyter.org
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter_events/jupyter_events-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.5
Requires:       python3-jupyter-events = %{version}-%{release}
# /oreon:deps
%package -n       python3-jupyter-events+docs
Summary:        Metapackage for python3-jupyter-events docs extras
Requires:       python3-jupyter-events = %{version}-%{release}
Requires:       python3dist(sphinx) >= 8
Requires:       python3dist(pydata-sphinx-theme) >= 0.16
Provides:       python3dist(jupyter-events[docs]) = %{version}-%{release}

%description -n python3-jupyter-events+docs
Metapackage for python3-jupyter-events docs extras.

%package -n       python3-jupyter-events+test
Summary:        Metapackage for python3-jupyter-events test extras
Requires:       python3-jupyter-events = %{version}-%{release}
Requires:       python3dist(pytest-asyncio) >= 0.19.0
Requires:       python3dist(pytest) >= 7.0
Provides:       python3dist(jupyter-events[test]) = %{version}-%{release}

%description -n python3-jupyter-events+test
Metapackage for python3-jupyter-events test extras.

%package -n       python3-jupyter-events+cli
Summary:        Metapackage for python3-jupyter-events cli extras
Requires:       python3-jupyter-events = %{version}-%{release}
Provides:       python3dist(jupyter-events[cli]) = %{version}-%{release}

%description -n python3-jupyter-events+cli
Metapackage for python3-jupyter-events cli extras.

%description

%package -n     python3-jupyter-events
Summary:        Jupyter Event System library
# oreon:reqs
Requires:       python3dist(jsonschema[format-nongpl]) >= 4.18.0
Requires:       python3dist(python-json-logger) >= 2.0.4
Requires:       python3dist(pyyaml) >= 5.3
Requires:       python3dist(rfc3986-validator) >= 0.1.1
Requires:       python3dist(traitlets) >= 5.3
# /oreon:reqs
%description -n python3-jupyter-events

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir jupyter_events-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jupyter-events usr/lib/python3*/site-packages/jupyter_events* usr/lib64/python3*/site-packages/jupyter_events* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jupyter_events* usr/lib64/python3*/site-packages/jupyter_events* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jupyter-events -f %{oreon_filedir}/python3-jupyter-events.list

%changelog

%autochangelog
