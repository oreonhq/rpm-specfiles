%global source0_hash 9f29e6a3dabdb75f2b39c949772c0ed26eab15308006669f3478cdab0d867c78

Name:           python-findpython
Version:        0.7.1
Release:        %autorelease

Summary:        A utility to find python versions on your system

License:        MIT
URL:            https://github.com/frostming/findpython
Source:         %{pypi_source findpython}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Findpython searches for python executables available on the system.}

%description %_description

%package -n     python3-findpython
Summary:        %{summary}

%description -n python3-findpython %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n findpython-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L findpython

%check
%pytest

%files -n python3-findpython -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/findpython

%changelog
%autochangelog
