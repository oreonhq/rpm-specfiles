%global source0_hash 7de0efcc361c573f2537ee7ceabdb3bc64b19b61304cfa25e828caa7db8ae1a4

# python-cattrs is too old in Fedora 40:
%bcond cattrs %{undefined fc40}

Name:           python-ufoLib2
Version:        0.18.1
Release:        5%{?dist}
Summary:        A library to deal with UFO font sources

License:        Apache-2.0
URL:            https://github.com/fonttools/ufoLib2
Source:         %{pypi_source ufolib2 %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

# Required for running tests
BuildRequires:  python3dist(pytest)

%global _description %{expand:
ufoLib2 is meant to be a thin representation of the Unified Font Object (UFO)
version 3 data model, intended for programmatic manipulation and fast batch
processing of UFOs.}

%description %_description

%package -n python3-ufoLib2
Summary:        %{summary}

%description -n python3-ufoLib2 %_description

%pyproject_extras_subpkg -n python3-ufoLib2 lxml%{?with_cattrs: converters json msgpack}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ufolib2-%{version}

%generate_buildrequires
%pyproject_buildrequires -x lxml%{?with_cattrs:,converters,json,msgpack}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l ufoLib2

%check
%pyproject_check_import %{?!with_cattrs:-e ufoLib2.converters -e ufoLib2.serde.json -e ufoLib2.serde.msgpack}
%pytest -v

%files -n python3-ufoLib2 -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
