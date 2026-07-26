%global source0_hash 30fa9e6ad507df49d3c6a2f88894256bcf90f18e240a00764da6ecab1db24895

Name:           python-tox-uv
Version:        1.29.0
Release:        %autorelease
Summary:        Integration of uv with tox

License:        MIT
URL:            https://github.com/tox-dev/tox-uv
Source:         %{pypi_source tox_uv}

# as with python-tox, those tests run on the CI only, as they need internet access
%bcond ci_tests 0

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
tox-uv is a tox plugin, which replaces virtualenv and pip with uv in your tox
environments. Note that you will get both the benefits (performance)
or downsides (bugs) of uv.

Installing this package changes the behavior of tox.
It also complicates usage of tox with a Python version not supported by uv.
Use `tox --runner virtualenv` to disable this plugin.}

%description %_description

%package -n     python3-tox-uv
Summary:        %{summary}

%description -n python3-tox-uv %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n tox_uv-%{version}
# Remove unpackaged (devpi-process) and coverage test dependencies
sed -Ei '/"(devpi-process|covdefaults|diff-cover|pytest-cov)/d' pyproject.toml
# Relax some build/test dependencies
sed -Ei 's/"(hatch(ling|-vcs)|pytest(-mock)?)>=[^"]+"/"\1"/' pyproject.toml
%if %{defined fc42}
# https://src.fedoraproject.org/rpms/python-tox-uv/pull-request/48#comment-289650
sed -Ei 's/("packaging>=)25"/\124\.2"/' pyproject.toml
%endif

%generate_buildrequires
%pyproject_buildrequires -g test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l tox_uv

%check
# only works with the package actually installed
k="${k-}${k+ and }not test_tox_version"

%if %{without ci_tests}
# requires internet
k="${k-}${k+ and }not test_uv_install"
k="${k-}${k+ and }not test_uv_package_editable_legacy"
k="${k-}${k+ and }not test_uv_package_no_pyproject"
k="${k-}${k+ and }not test_uv_package_requirements"
k="${k-}${k+ and }not test_uv_package_workspace"
k="${k-}${k+ and }not test_uv_python_set"
%endif

%pytest -v "${k:+-k $k}"

%files -n python3-tox-uv -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
