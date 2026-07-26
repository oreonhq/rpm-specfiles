%global source0_hash 3196b2d9eb05c57d2fb0f3cf16c04ce04bbdc662431477f42331200b52b4fc37

%global pypi_name mackup

%bcond tests 1

Name:           python-%{pypi_name}
Version:        0.10.2
Release:        %autorelease
Summary:        Keep your application settings in sync

License:        GPL-3.0-only
URL:            https://github.com/lra/mackup
# pypi_source does not have license and tests
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  procps-ng
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(six)
%endif

%global _description %{expand:
Mackup:
- Backs up your application settings in a safe directory (e.g. Dropbox)
- Syncs your application settings among all your workstations
- Restores your configuration on any fresh install in one command line

By only tracking pure configuration files, it keeps the cruft out of your
freshly new installed workstation (no cache, temporary and locally specific
files are transferred).

Mackup makes setting up the environment easy and simple, saving time for your
family, great ideas, and all the cool stuff you like. }

%description %{_description}

%package -n     %{pypi_name}
Summary:        %{summary}
Requires:       procps-ng

%description -n %{pypi_name} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%if %{with tests}
%pytest -v
%endif

%files -n %{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/mackup

%changelog
%autochangelog
