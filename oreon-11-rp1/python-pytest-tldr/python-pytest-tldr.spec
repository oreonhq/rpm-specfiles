%global source0_hash 43f43fe758569df620c433a79d3cbee698e77268efebbc6e22ce1e66095a0881

%global srcname pytest-tldr

Name:           python-%{srcname}
Version:        0.2.5
Release:        %autorelease
Summary:        Pytest plugin that limits the output to just the things you need

License:        BSD-3-Clause
URL:            https://github.com/freakboy3742/pytest-tldr
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This package provides a pytest plugin that limits the output of pytest to just
the things you need to see.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_tldr

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.rst

%changelog
%autochangelog
