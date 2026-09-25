%global source0_hash 129a341b0a85a7db7879e22acd66902fda67882db771754574338898b2d5d86f

# TODO adjust once this is implemented:
# https://bugzilla.redhat.com/show_bug.cgi?id=1935266
%global modname  jaraco
%global projname %{modname}.context
%global pkgname  %{modname}-context
%global srcname  %{modname}_context

%bcond_without tests
# Change the build backend in EPEL9 because `setuptools>=61.2`
# is needed for PEP621
%if 0%{?epel} == 9
%bcond_without hatch
%else
%bcond_with    hatch
%endif

Name:           python-%{pkgname}
Version:        6.1.0
Release:        %autorelease
Summary:        Context managers by jaraco

License:        MIT
URL:            https://github.com/jaraco/%{projname}
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with hatch}
BuildRequires:  tomcli
%endif

%global _description %{expand:
Context managers by jaraco.}

%description %_description

%package     -n python3-%{pkgname}
Summary:        %{summary}

%description -n python3-%{pkgname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%if %{with hatch}
tomcli set pyproject.toml lists str "build-system.requires" "hatchling" "hatch-vcs"
tomcli set pyproject.toml str "build-system.build-backend" "hatchling.build"
tomcli set pyproject.toml str "tool.hatch.version.source" "vcs"
tomcli set pyproject.toml lists str "tool.hatch.build.targets.wheel.packages" %{modname}
%endif

%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -x test
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%if %{with tests}
%pytest -k "not context.repo_context"
%else
%pyproject_check_import
%endif

%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE
%doc README.rst NEWS.rst

%changelog
%autochangelog
