%global source0_hash e292ec8b9cfa64c26b592faf9b7cfc72c4f4b0eb0d533f045a46061e75c5ce99

Name:           python-pyformlang
Version:        1.0.11
Release:        %autorelease
Summary:        A python framework for formal grammars

License:        MIT
URL:            https://github.com/Aunsiels/pyformlang
Source:         %{pypi_source pyformlang}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
A python framework for formal grammars.}

%description %_description

%package -n     python3-pyformlang
Summary:        %{summary}

%description -n python3-pyformlang %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pyformlang-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pyformlang

%check
%pyproject_check_import
%pytest

%files -n python3-pyformlang -f %{pyproject_files}

%changelog
%autochangelog
