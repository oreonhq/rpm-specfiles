%global source0_hash 7837e807ba0791d86aa90b5c1ead0afccb901aab8a5f3d07fc2d1a3972d58ff7

%global pypi_name asciitree

Name:       python-%{pypi_name}
Version:    0.3.3
Release:    37%{?dist}
Summary:    Draws ASCII trees

License:    MIT
URL:        https://github.com/mbr/asciitree
Source0:    https://github.com/mbr/asciitree/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:  noarch

%description
Sometimes you just want to draw ascii trees in your terminal.

Read the documentation at https://pythonhosted.org/asciitree

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name}
Sometimes you just want to draw ascii trees in your terminal.

Read the documentation at https://pythonhosted.org/asciitree

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
%{pytest}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
