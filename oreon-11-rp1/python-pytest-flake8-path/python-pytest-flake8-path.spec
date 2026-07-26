%global source0_hash bd049b867079b22e3ca9021cfd80fa8096ce481588747803b6bebf0c355012a4

%global srcname pytest-flake8-path

Name:           python-%{srcname}
Version:        1.5.0
Release:        11%{?dist}
Summary:        A pytest fixture for testing flake8 plugins

License:        MIT
URL:            https://github.com/adamchainz/pytest-flake8-path
Source0:        https://github.com/adamchainz/pytest-flake8-path/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
pytest-flake8-path is the successor to pytest-flake8dir. pytest-flake8dir was
based upon pytest’s tmpdir fixture, which returned a legacy py.path.local
object. Since version 3.9.0, pytest has provided the tmp_path fixture, which
returns a standard library pathlib.Path object. pytest-flake8-path is a
rewrite of pytest-flake8dir to use tmp_path instead of tmpdir.}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires requirements/requirements.in

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_flake8_path

%check
%pytest

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc HISTORY.rst README.rst

%changelog
%autochangelog
