%global source0_hash 60d696200ddae28677e7d88cdebd6e960294e85adefbaafe0f6e5d0e7b4c1963

Name:           python-types-psutil
Version:        7.0.0.20251001
Release:        %autorelease
Summary:        Typing stubs for psutil

License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source:         %{pypi_source types_psutil}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a PEP 561 type stub package for the psutil package. It can be used by
type-checking tools like mypy, pyright, pytype, PyCharm, etc. to check code
that uses psutil.}

%description %_description

%package -n     python3-types-psutil
Summary:        %{summary}

%description -n python3-types-psutil %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n types_psutil-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L psutil-stubs

%files -n python3-types-psutil -f %{pyproject_files}

%changelog
%autochangelog
