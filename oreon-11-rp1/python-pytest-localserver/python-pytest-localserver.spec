%global source0_hash 2607197f390912ab25525d129ac43c3c875049257368b3fe09b5cd03dcc526af

Name:           python-pytest-localserver
Version:        0.10.0
Release:        %autorelease
Summary:        pytest plugin to test server connections locally

License:        MIT
URL:            https://github.com/pytest-dev/pytest-localserver
# The package uses setuptools_scm, GitHub tarball will not work
Source0:        %{pypi_source pytest_localserver}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
pytest-localserver is a plugin for the pytest testing framework which enables
you to test server connections locally.}

%description %_description

%package -n python3-pytest-localserver
Summary:        %{summary}

%description -n python3-pytest-localserver %_description

%pyproject_extras_subpkg -n python3-pytest-localserver smtp

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pytest_localserver-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_localserver

%check
%tox

%files -n python3-pytest-localserver -f %{pyproject_files}
%doc README.rst CHANGES
%license LICENSE

%changelog
%autochangelog
