%global source0_hash 7da7445af2ce15b90aad5ec4792f857cef5786d71f14377e9eb994d8b8337f2f

Name:           python-cram
Version:        0.7
Release:        27%{?dist}
Summary:        Simple testing framework for command line applications
License:        GPL-2.0-or-later
URL:            https://bitheap.org/cram/
Source:         %{pypi_source cram}
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Cram is a functional testing framework for command line applications. Cram
tests look like snippets of interactive shell sessions. Cram runs each command
and compares the command output in the test with the command's actual output.}

%description %_description

%package -n python3-cram
Summary:        %{summary}

%description -n python3-cram %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cram-%{version}

# Fix shebang in script for tests
%py3_shebang_fix scripts/cram

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cram

%check
# dist.t needs check-manifest which isn't packaged
# pep8.t needs pep8 which has been retired
PYTHONPATH=%{buildroot}%{python3_sitelib} PYTHON=%python3 scripts/cram -v tests

%files -n python3-cram -f %{pyproject_files}
%doc NEWS.rst README.rst TODO.md
%{_bindir}/cram

%changelog
%autochangelog
