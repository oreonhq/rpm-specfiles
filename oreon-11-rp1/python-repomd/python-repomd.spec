%global source0_hash 30bd9c329ba465e5b6c5e14ab008260c53fac61e138040b34b19489f3971d7aa

Name:           python-repomd
Version:        0.2.1
Release:        26%{?dist}
Summary:        Library for reading dnf/yum repositories
License:        MIT
URL:            https://github.com/carlwgeorge/repomd
Source:         %{pypi_source repomd}
BuildArch:      noarch

%global _description %{expand:
This library provides an object-oriented interface to get information out of
dnf/yum repositories.}

%description %{_description}

%package -n python3-repomd
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-repomd %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n repomd-%{version}
rm setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l repomd

%check
%pytest --verbose

%files -n python3-repomd -f %{pyproject_files}

%changelog
%autochangelog
