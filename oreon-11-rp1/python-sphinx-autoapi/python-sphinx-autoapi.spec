%global source0_hash 1ff2992b7d5e39ccf92413098a376e0f91e7b4ca532c4f3e71298dbc8a4a9900

%global srcname sphinx-autoapi
%global srcname_ sphinx_autoapi

Name:           python-%{srcname}
Version:        3.6.1
Release:        %autorelease
Summary:        Sphinx API documentation generator

License:        MIT
URL:            https://github.com/readthedocs/sphinx-autoapi
Source:         %pypi_source %{srcname_}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Sphinx AutoAPI is a Sphinx extension for generating complete API documentation
without needing to load, run, or import the project being documented.

In contrast to the traditional Sphinx autodoc, which requires manual authoring
and uses code imports, AutoAPI finds and generates documentation by parsing
source code.}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname_}-%{version} -p1
# This symlink is lost from the sdist.
ln -s ../pyexample/example tests/python/pymovedconfpy/example

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Switch to -l when flit supports PEP639 (3.11, probably.)
%pyproject_save_files -L autoapi

%check
%{pytest} -m 'not network'

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE.rst

%changelog
%autochangelog
