%global source0_hash b81a69338c3d1a532062a2851b0d51723beafa69d4d382b713be230a02bd618a

%global pypi_name teletype

Name:           python-%{pypi_name}
Version:        1.3.4
Release:        %autorelease
Summary:        High-level cross platform Python tty library

License:        MIT
URL:            https://github.com/jkwill87/teletype
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
teletype is a high-level cross platform tty library compatible with Python
3.7+. It provides a consistent interface between the terminal and cmd.exe by
building on top of terminfo and msvcrt and has no dependencies.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

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
%pyproject_check_import -e teletype.codes.windows -e teletype.io.windows %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
