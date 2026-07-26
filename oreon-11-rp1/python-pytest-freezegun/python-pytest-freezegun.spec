%global source0_hash 38eb50fd3284c7353ccd4fcd3cbe149f97a3636c6e7f37b033797ebe6eb09a4d

Name:           python-pytest-freezegun
Version:        0.4.2
Release:        %autorelease
Summary:        Wrap pytest tests with fixtures in freeze_time

License:        MIT
URL:            https://github.com/ktosiek/pytest-freezegun
Source0:        %{url}/archive/%{version}/pytest-freezegun-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

%global _description %{expand:
This is a pytest plugin that let you wrap tests with fixtures in freeze_time.

Features:

- Freeze time in both the test and fixtures
- Access the freezer when you need it}

%description %_description

%package -n python3-pytest-freezegun
Summary:        %{summary}

%description -n python3-pytest-freezegun %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pytest-freezegun-%{version}

%generate_buildrequires
# tox config contains coverage, so we'll execute pytest directly instead
# since this a pytest plugin, pytetst is a runtime dependency anyway
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_freezegun

%check
%pytest -v

%files -n python3-pytest-freezegun -f %{pyproject_files}
%doc README.rst CHANGELOG.md
%license LICENSE

%changelog
%autochangelog
