%global source0_hash b3e56b332933b67fcb0aa87d6c2c9e5b5ba99146969b9d5879474706f6080b61

%global srcname readchar

Name:           python-%{srcname}
Version:        4.0.5
Release:        %autorelease
Summary:        Library to easily read single chars and key strokes

License:        MIT
URL:            https://github.com/magmax/python-readchar
# The PyPI tarball doesn't include tests so use GitHub instead
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov

%global _description %{expand:
This is package provides a library to easily read single chars and keystrokes.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
