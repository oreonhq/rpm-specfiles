%global source0_hash de8610639996f1567952d763a5a41af8af37f2575a41f9852a38f947eb82a3b9

%global pypi_name widgetsnbextension

Name:           python-%{pypi_name}
Version:        4.0.15
Release:        %autorelease
Summary:        Interactive HTML widgets for Jupyter notebooks

License:        BSD-3-Clause
URL:            http://ipython.org
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python-jupyter-filesystem

%description
Interactive HTML widgets for Jupyter notebooks.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(notebook) >= 4.4.1
Requires:       python-jupyter-filesystem

# sagemath included the files of this package
# https://bugzilla.redhat.com/show_bug.cgi?id=1856311
Conflicts:      sagemath-jupyter < 9.1-2

%description -n python3-%{pypi_name}
Interactive HTML widgets for Jupyter notebooks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# Move config file from /usr/etc to /etc
mkdir -p %{buildroot}%{_sysconfdir}/jupyter/nbconfig/notebook.d/
mv {%{buildroot}%{_prefix}/etc,%{buildroot}%{_sysconfdir}}/jupyter/nbconfig/notebook.d/widgetsnbextension.json

%files -n python3-%{pypi_name} -f %{pyproject_files}
%{_datadir}/jupyter/nbextensions/jupyter-js-widgets/
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/notebook.d/widgetsnbextension.json

%changelog
%autochangelog
