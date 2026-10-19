%global source0_hash b4b2cfa1b65d98307ca24361f5b30fe785b53c3fd07b7a47e89acb5e6ac638cb
Name:           python-notebook-shim
Version:        0.2.4
Release:        1%{?dist}
Summary:        A shim layer for notebook traits and config
License:        BSD-3-Clause
URL:            https://pypi.org/project/notebook-shim/
Source0:        https://files.pythonhosted.org/packages/source/n/notebook_shim/notebook_shim-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.0
Requires:       python3-notebook-shim = %{version}-%{release}
# /oreon:deps
%package -n       python3-notebook-shim+test
Summary:        Metapackage for python3-notebook-shim test extras
Requires:       python3-notebook-shim = %{version}-%{release}
Provides:       python3dist(notebook-shim[test]) = %{version}-%{release}

%description -n python3-notebook-shim+test
Metapackage for python3-notebook-shim test extras.

%description

%package -n     python3-notebook-shim
Summary:        A shim layer for notebook traits and config
Requires:  python-jupyter-filesystem
# oreon:reqs
Requires:       python3dist(jupyter-server) < 3
Requires:       python3dist(jupyter-server) >= 1.8
# /oreon:reqs
%description -n python3-notebook-shim

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n notebook_shim-%{version}

# pytest-tornasync will never be available in Fedora
# and upstream will switch to pytest-jupyter soon
sed -i "/pytest-tornasync/d" pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_server_config.d/notebook_shim.json
%oreon_autofiles python3-notebook-shim usr/lib/python3*/site-packages/notebook_shim* usr/lib64/python3*/site-packages/notebook_shim* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/notebook_shim* usr/lib64/python3*/site-packages/notebook_shim* usr/bin/*

%check

%pytest
%files
%files -n python3-notebook-shim -f %{oreon_filedir}/python3-notebook-shim.list

%changelog

%autochangelog
