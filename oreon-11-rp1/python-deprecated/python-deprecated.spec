%global source0_hash b1b50e0ff0c1fddaa5708a2c6b0a6588bb09b892825ab2b214ac9ea9d92a5223

Name:           python-deprecated
Version:        1.3.1
Release:        2%{?dist}
Summary:        Python decorator to deprecate old python classes, functions or methods
License:        MIT
URL:            https://github.com/laurent-laporte-pro/deprecated
Source:         %{pypi_source deprecated}
BuildArch:      noarch

%global _description %{expand:
Python @deprecated decorator to deprecate old python classes,
functions or methods.}

%description %{_description}

%package -n python3-deprecated
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-deprecated %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n deprecated-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l deprecated

%check
%pytest

%files -n python3-deprecated -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
