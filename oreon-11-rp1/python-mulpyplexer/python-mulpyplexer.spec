%global source0_hash 144e9e9bf66d3988f60542c9d3d4c94857438f7908f60e53f4c1cb1622fbbd30

%global pypi_name mulpyplexer

Name:           python-%{pypi_name}
Version:        0.09
Release:        23%{?dist}
Summary:        Module that multiplexes interactions with lists of Python objects

License:        BSD-2-Clause
URL:            https://github.com/zardus/mulpyplexer
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel

%global _description %{expand:
Mulpyplexer is a piece of code that can multiplex interactions with lists of
python objects.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mulpyplexer

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
