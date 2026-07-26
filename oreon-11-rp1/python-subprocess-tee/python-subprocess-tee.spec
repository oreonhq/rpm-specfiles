%global source0_hash b3c124993f8b88d1eb1c2fde0bc2069787eac720ba88771cba17e8c93324825d

%global forgeurl https://github.com/pycontribs/subprocess-tee

%bcond_without tests

Name:           python-subprocess-tee
Version:        0.4.1
%forgemeta
Release:        %autorelease
Summary:        A subprocess.run that works like tee, being able to display output in real time while still capturing it
URL:            %{forgeurl}
Source:         %{pypi_source subprocess-tee}
Patch:          0001-Remove-unnecessary-test-deps.patch
License:        MIT
BuildArch:      noarch

BuildRequires: python3-devel

%global common_description %{expand:
This package provides an drop-in alternative to subprocess.run that captures
the output while still printing it in real time, just the way tee does.
}

%description %{common_description}

%package -n python3-subprocess-tee
Summary: %summary

%description -n python3-subprocess-tee %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n subprocess-tee-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files subprocess_tee

%if %{with tests}
%check
# We don't want to depend on enrich
%pytest test -k "not test_molecule" --ignore test/test_rich.py
%endif

%files -n python3-subprocess-tee -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
