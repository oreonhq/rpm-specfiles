%global source0_hash 4c81d917d1bfaf418ddacbb9dad848ff941b5f75466660e5168d4b89506496d8

%global forgeurl https://github.com/marcomusy/vedo
Version:        2024.5.2
%forgemeta

%bcond check 1

Name:           python-vedo
Release:        %autorelease
Summary:        A python module for scientific analysis and visualization of 3D objects

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A python module for scientific analysis of 3D objects and point clouds based on
VTK and numpy.}

%description %_description

%package -n     python3-vedo
Summary:        %{summary}

%description -n python3-vedo %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n vedo-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files vedo

%py3_shebang_fix %{buildroot}%{python3_sitelib}

%check
%if %{with check}
%{py3_test_envvars} %{python3} tests/common/test_*.py
%endif

%files -n python3-vedo -f %{pyproject_files}
%{_bindir}/vedo

%changelog
%autochangelog
