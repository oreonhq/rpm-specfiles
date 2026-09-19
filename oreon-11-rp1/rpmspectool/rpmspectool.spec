%global source0_hash 4a9eae6169a6ae8a56c6de0985935dad05d3cb087fc5b92f06d9739e215b0327

%bcond testcoverage 0

Name:           rpmspectool
Version:        1.100.0
Release:        %autorelease
Summary:        Utility for dealing with RPM spec files

License:        GPL-3.0-or-later
URL:            https://github.com/nphilipp/rpmspectool
Source0:        %{pypi_source %{name}}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  sed
# The dependencies needed for testing don’t get auto-generated.
BuildRequires:  python3dist(pytest)
%if %{with testcoverage}
BuildRequires:  python3dist(pytest-cov)
%endif

Requires:       python3-%{name} = %{version}-%{release}

%generate_buildrequires
%{pyproject_buildrequires}

%global _description %{expand:
The rpmspectool utility lets users expand and download sources and patches in
RPM spec files.}

%description %_description

%package -n python3-%{name}
Summary:        %{summary}

%description -n python3-%{name} %_description

This package contains the Python package used by the rpmspectool CLI.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%if %{without testcoverage}
cat << PYTESTINI > pytest.ini
[pytest]
addopts =
PYTESTINI
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}
sed -i -e 's|^\(.*/COPYING\)|%%license \1|g' %{pyproject_files}

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
cp shell-completions/bash/rpmspectool %{buildroot}%{_datadir}/bash-completion/completions/

%check
%pytest -v

%files
%license COPYING
%doc README.md
%{_bindir}/rpmspectool
%{_datadir}/bash-completion/

%files -n python3-%{name} -f %{pyproject_files}

%changelog
%autochangelog
