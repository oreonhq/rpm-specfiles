%global source0_hash 2814ff0d8a92271dadc222afb4e17fc949413b105c20d7cfe5515f941cdda386

%global pypi_name banal

Name:           python-%{pypi_name}
Version:        1.0.6
Release:        %autorelease
Summary:        Commons of stupid, simple Python micro functions

License:        MIT
URL:            https://github.com/pudo/banal
Source:         %url/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global common_description %{expand:
Commons of Python micro-functions. This basically an out-sourced, shared utils
module with a focus on functions that buffer type uncertainties in Python.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
