%global source0_hash d5e2dc3e300f08a9e02129d8fc0eaf7d46a62bb5a66a861168b0438e45710021

%global pypi_name puremagic

Name:           python-%{pypi_name}
Version:        1.30
Release:        %autorelease
Summary:        Pure python implementation of magic file detection

%global forgeurl https://github.com/cdgriffith/puremagic
%global tag %{version}
%forgemeta

License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Pure Python module that will identify a file based on its magic numbers.

It does NOT try to match files on non-magic string. In other words it
will not search for a string within a certain window of bytes like
others might.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

# Remove unnecessary shebangs
sed -r \
    -e '/^#!/d' \
    -i puremagic/__init__.py puremagic/__main__.py puremagic/main.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pytest -r fEs
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS.rst CHANGELOG.md README.rst

%changelog
%autochangelog
