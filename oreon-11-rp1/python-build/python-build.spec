%global source0_hash 302c22c3ba2a0fd5f3911918651341ebb3896176cbdec15bd421f80b1afc7647

%bcond extras %{undefined rhel}
%bcond tests %[%{undefined rhel} && %{with extras}]

Name:           python-build
Version:        1.5.0
Release:        %autorelease
Summary:        A simple, correct PEP517 package builder

License:        MIT
URL:            https://github.com/pypa/build
Source:         https://files.pythonhosted.org/packages/78/e0/df5e171f685f82f37b12e1f208064e24244911079d7b767447d1af7e0d70/build-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros >= 0-41

%description
A simple, correct PEP517 package builder.


%package -n     python3-build
Summary:        %{summary}

%description -n python3-build
A simple, correct PEP517 package builder.


%if %{with extras} || %{defined eln}
%pyproject_extras_subpkg -n python3-build virtualenv uv
%endif


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n build-%{version}
%pyproject_patch_dependency pytest-cov:ignore
%pyproject_patch_dependency covdefaults:ignore


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-g test} %{?with_extras:-x virtualenv,uv}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l build


%check
%pyproject_check_import
%if %{with tests}
%pytest -v -m "not network"
%endif


%files -n python3-build -f %{pyproject_files}
%doc README.md
%{_bindir}/pyproject-build


%changelog
%autochangelog
