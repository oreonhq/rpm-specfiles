%global source0_hash abf61f45ba4dbb7123920554d87f4fd923948025621d61454c808315fb265233

%bcond_without tests
%bcond_without doc_pdf

%global pypi_name succulent

%global _description %{expand:
Sending sensor measurements, data, or GPS positions from embedded devices,
microcontrollers, and smartwatches to the central server is sometimes
complicated and tricky. Setting up the primary data collection scripts
can be time-consuming (selecting a protocol, framework, API, testing it, etc.).
Usually, scripts are written for a specific task; thus, they are not easily
adaptive to other tasks. succulent is a pure Python framework that simplifies
the configuration, management, collection, and preprocessing of data collected
via POST requests. }

Name:           python-%{pypi_name}
Version:        0.4.3
Release:        1%{?dist}
Summary:        Collect POST requests

License:        MIT
URL:            https://github.com/firefly-cpp/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli
BuildRequires:  python3-pytest

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  %{py3_dist sphinxcontrib-bibtex}
%endif

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        Documentation and examples for %{name}

%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# Drop version pinning (we use the versions available in Fedora)
for DEP in $(tomcli get -F newline-keys pyproject.toml tool.poetry.dependencies)
do
  tomcli set pyproject.toml replace tool.poetry.dependencies.${DEP} ".*" "*"
done

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files succulent

%check
%if %{with tests}
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md CITATION.cff

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/succulent.pdf
%endif

%changelog
%autochangelog
