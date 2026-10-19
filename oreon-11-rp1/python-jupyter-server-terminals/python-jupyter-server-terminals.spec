%global source0_hash bbda128ed41d0be9020349f9f1f2a4ab9952a73ed5f5ac9f1419794761fb87f5
Name:           python-jupyter-server-terminals
Version:        0.5.4
Release:        1%{?dist}
Summary:        A Jupyter Server Extension Providing Terminals
License:        BSD-3-Clause
URL:            https://jupyter.org
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter_server_terminals/jupyter_server_terminals-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.5
Requires:       python3-jupyter-server-terminals = %{version}-%{release}
# /oreon:deps
%package -n       python3-jupyter-server-terminals+test
Summary:        Metapackage for python3-jupyter-server-terminals test extras
Requires:       python3-jupyter-server-terminals = %{version}-%{release}
Requires:       python3dist(jupyter-server) >= 2.0.0
Requires:       python3dist(pytest-jupyter[server]) >= 0.5.3
Requires:       python3dist(pytest) >= 7.0
Provides:       python3dist(jupyter-server-terminals[test]) = %{version}-%{release}

%description -n python3-jupyter-server-terminals+test
Metapackage for python3-jupyter-server-terminals test extras.

%package -n       python3-jupyter-server-terminals+docs
Summary:        Metapackage for python3-jupyter-server-terminals docs extras
Requires:       python3-jupyter-server-terminals = %{version}-%{release}
Requires:       python3dist(mistune) < 4.0
Provides:       python3dist(jupyter-server-terminals[docs]) = %{version}-%{release}

%description -n python3-jupyter-server-terminals+docs
Metapackage for python3-jupyter-server-terminals docs extras.

%description

%package -n     python3-jupyter-server-terminals
Summary:        A Jupyter Server Extension Providing Terminals
Requires:  python-jupyter-filesystem
# oreon:reqs
Requires:       python3dist(pywinpty) >= 2.0.3
Requires:       python3dist(terminado) >= 0.8.3
# /oreon:reqs
%description -n python3-jupyter-server-terminals

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir jupyter_server_terminals-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_server_config.d/jupyter_server_terminals.json
%oreon_autofiles python3-jupyter-server-terminals usr/lib/python3*/site-packages/jupyter_server_terminals* usr/lib64/python3*/site-packages/jupyter_server_terminals* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jupyter_server_terminals* usr/lib64/python3*/site-packages/jupyter_server_terminals* usr/bin/*

%check

%files
%files -n python3-jupyter-server-terminals -f %{oreon_filedir}/python3-jupyter-server-terminals.list

%changelog

%autochangelog
