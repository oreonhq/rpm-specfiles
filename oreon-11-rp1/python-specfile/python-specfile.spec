%global source0_hash 2538321e754b546fef82ec2f853c328a4d5d56334dd3ac15b618f9b803282537

%bcond_without tests

%global desc %{expand:
Python library for parsing and manipulating RPM spec files.
Main focus is on modifying existing spec files, any change should result
in a minimal diff.}

%global base_version 0.41.1
%global package_version %{base_version}%{?prerelease:~%{prerelease}}
%global pypi_version    %{base_version}%{?prerelease}

Name:           python-specfile
Version:        %{package_version}
Release:        1%{?dist}

Summary:        A library for parsing and manipulating RPM spec files
License:        MIT
URL:            https://github.com/packit/specfile

Source0:        %{pypi_source specfile %{pypi_version}}

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  git-core
%endif

Recommends:     oreon-rpm-config

%description
%{desc}

%package -n python%{python3_pkgversion}-specfile
Summary:        %{summary}

%description -n python%{python3_pkgversion}-specfile
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n specfile-%{pypi_version}

sed -i 's/setuptools_scm\[toml\]>=7/setuptools_scm[toml]/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires %{?with_tests: -x testing}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files specfile

%if %{with tests}
%check
%pytest --verbose tests/unit tests/integration
%endif

%files -n python%{python3_pkgversion}-specfile -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
