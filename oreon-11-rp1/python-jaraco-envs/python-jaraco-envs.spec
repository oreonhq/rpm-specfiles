%global source0_hash 809195c406640db256ee01eebf4f6a369dd85759d8178c3921704308dd0360f5

# doc dependencies are not packaged
%bcond_with docs

Name:           python-jaraco-envs
Version:        2.6.0
Release:        %autorelease
Summary:        Classes for orchestrating Python (virtual) environments

License:        MIT
URL:            https://github.com/jaraco/jaraco.envs
Source0:        %{pypi_source jaraco.envs}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Classes for orchestrating Python (virtual) environments.

%package -n     python3-jaraco-envs
Summary:        %{summary}

%description -n python3-jaraco-envs
Classes for orchestrating Python (virtual) environments.

%if %{with docs}
%package -n python-jaraco-envs-doc
Summary:        jaraco-envs documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(jaraco-packaging)
BuildRequires:  python3dist(rst-linker)

%description -n python-jaraco-envs-doc
Documentation for jaraco-envs
%endif # with docs

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n jaraco.envs-%{version}
# Remove dev-only dependencies. Upstream later split the `test` dependencies out of it
# https://github.com/jaraco/skeleton/issues/138
sed -E -i '/pytest-/d' setup.cfg
sed -E -i '/python_implementation/d' setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x testing

%build
%pyproject_wheel
%if %{with docs}
# generate html docs
%{python3} -m sphinx docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif # with docs

%install
%pyproject_install
%pyproject_save_files -l jaraco

%check
# envs.VirtualEnv: Requires internet connection
%pytest -k "not envs.VirtualEnv"

%files -n python3-jaraco-envs -f %{pyproject_files}
%doc README.rst

%if %{with docs}
%files -n python-jaraco-envs-doc
%doc html
%license LICENSE
%endif # with docs

%changelog
%autochangelog
