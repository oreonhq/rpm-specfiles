%global source0_hash b4b2cfa1b65d98307ca24361f5b30fe785b53c3fd07b7a47e89acb5e6ac638cb

Name:           python-notebook-shim
Version:        0.2.4
Release:        9%{?dist}
Summary:        A shim layer for notebook traits and config
License:        BSD-3-Clause
URL:            https://pypi.org/project/notebook-shim/
Source:         %{pypi_source notebook_shim}

BuildArch:      noarch
BuildRequires:  python3-devel
# https://github.com/jupyter/notebook_shim/issues/28
BuildRequires:  python3-pytest-jupyter

%global _description %{expand:
This project provides a way for JupyterLab and other frontends
to switch to Jupyter Server for their Python Web application backend.}

%description %_description

%package -n     python3-notebook-shim
Summary:        %{summary}

Requires:  python-jupyter-filesystem

%description -n python3-notebook-shim %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n notebook_shim-%{version}

# pytest-tornasync will never be available in Fedora
# and upstream will switch to pytest-jupyter soon
sed -i "/pytest-tornasync/d" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files notebook_shim

install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_server_config.d/notebook_shim.json

%check
%pytest

%files -n python3-notebook-shim -f %{pyproject_files}
%doc README.md
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_server_config.d/notebook_shim.json

%changelog
%autochangelog
