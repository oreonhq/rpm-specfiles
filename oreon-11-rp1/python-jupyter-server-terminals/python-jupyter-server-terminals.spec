%global source0_hash bbda128ed41d0be9020349f9f1f2a4ab9952a73ed5f5ac9f1419794761fb87f5

Name:           python-jupyter-server-terminals
Version:        0.5.4
Release:        %autorelease
Summary:        A Jupyter Server Extension Providing Terminals
License:        BSD-3-Clause
URL:            https://jupyter.org
Source:         %{pypi_source jupyter_server_terminals}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Jupyter Server Terminals is a Jupyter Server Extension
providing support for terminals.}

%description %_description

%package -n     python3-jupyter-server-terminals
Summary:        %{summary}

Requires:  python-jupyter-filesystem

%description -n python3-jupyter-server-terminals %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n jupyter_server_terminals-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jupyter_server_terminals

install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_server_config.d/jupyter_server_terminals.json

%check
# The dependency on jupyter-server creates a dependency loop
# we cannot break yet.
# %%pytest

%files -n python3-jupyter-server-terminals -f %{pyproject_files}
%doc README.md
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_server_config.d/jupyter_server_terminals.json

%changelog
%autochangelog
