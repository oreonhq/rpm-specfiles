%global source0_hash 906912b7ab410d9a7f351202839c3cd73a2ac077bd0071c861c31f0eef760287

%global pypi_name klein

Name:           python-%{pypi_name}
Version:        23.5.0
Release:        12%{?dist}
Summary:        Python microframework built on werkzeug + twisted.web

License:        MIT
URL:            https://github.com/twisted/klein
Source0:        %{pypi_source}
BuildArch:      noarch
Patch0:         imp-removal.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(hyperlink)
BuildRequires:  python3dist(incremental)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(tubes)
BuildRequires:  python3dist(twisted) >= 15.5
BuildRequires:  python3dist(werkzeug)
BuildRequires:  python3dist(zope-interface)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description
Klein is a Web Micro-Framework built on Twisted and Werkzeug.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Klein is a Web Micro-Framework built on Twisted and Werkzeug.

%package -n python-%{pypi_name}-doc
Summary:        klein documentation

%description -n python-%{pypi_name}-doc
Documentation for klein

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p0

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import -t

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
