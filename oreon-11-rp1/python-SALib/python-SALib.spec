%global source0_hash 067b67415259421cece5bbd41bbcff8ebe5e48fefadf95218c2660a79118cd05

%bcond tests 1

%global forgeurl https://github.com/SALib/SALib

Name:           python-SALib
Version:        1.5.1
Release:        %autorelease
Summary:        Tools for global sensitivity analysis

%forgemeta

# SPDX
License:        MIT
URL:            https://salib.readthedocs.io
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  git-core

%global _description %{expand:
Python implementations of commonly used sensitivity analysis methods. Useful in
systems modeling to calculate the effects of model inputs or exogenous factors
on outputs of interest.}

%description %_description

%package -n python3-salib
Summary:        %{summary}

%py_provides python3-SALib

%description -n python3-salib %_description

%pyproject_extras_subpkg -n python3-salib distributed

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1 -S git

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^([[:blank:]])(.*\bpytest-cov\b)/\1# \2/' pyproject.toml

# Make sure this is the last step in `%%prep` or hatch-vcs will yell
git add --all
git commit -m '[RPM]: Changes for %{version}'
git tag v%{version}

%generate_buildrequires
%pyproject_buildrequires -x distributed %{?with_tests:-x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l SALib

%check
%if %{with tests}
%pytest
%endif

%files -n python3-salib -f %{pyproject_files}
%doc CHANGELOG.md
%doc CITATION.cff
%doc CITATIONS.rst
%doc FAQ.md
%doc README-advanced.md
%doc README.rst
%{_bindir}/salib

%changelog
%autochangelog
