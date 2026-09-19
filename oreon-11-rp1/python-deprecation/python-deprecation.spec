%global source0_hash 72b3bde64e5d778694b0cf68178aed03d15e15477116add3fb773e581f9518ff

Name:           python-deprecation
Version:        2.1.0
Release:        22%{?dist}
Summary:        A library to handle automated deprecations

License:        Apache-2.0
URL:            https://deprecation.readthedocs.io/
Source:         %{pypi_source deprecation}

# Make unittest optional for python3.5+
# https://github.com/briancurtin/deprecation/pull/57
# Rebased on the PyPI sdist, which lacks some of the files touched by the PR.
Patch:          deprecation-2.1.0-unittest2.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
The deprecation library provides a deprecated decorator and a
fail_if_not_removed decorator for your tests. Together, the two enable the
automation of several things:

 1. The docstring of a deprecated method gets the deprecation details appended
    to the end of it. If you generate your API docs direct from your source,
    you don’t need to worry about writing your own notification. You also don’t
    need to worry about forgetting to write it. It’s done for you.

 2. Rather than having code live on forever because you only deprecated it but
   never actually moved on from it, you can have your tests tell you when it’s
   time to remove the code. The @deprecated decorator can be told when it’s
   time to entirely remove the code, which causes @fail_if_not_removed to raise
   an AssertionError, causing either your unittest or py.test tests to fail.

See http://deprecation.readthedocs.io/ for the full documentation.}

%description %{_description}

%package -n     python3-deprecation
Summary:        %{summary}

%description -n python3-deprecation %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n deprecation-%{version} -p1
# Remove pre-built HTML documentation to show that its pre-compiled and
# pre-minified JavaScript is not packaged.
rm -rv docs/_build/

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l deprecation

%check
%{py3_test_envvars} %{python3} -m unittest discover -v

%files -n python3-deprecation -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
