%global source0_hash 0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466

Name:           python-typing-extensions
Version:        4.15.0
Release:        4%{?dist}
Summary:        Backported and Experimental Type Hints for Python

License:        PSF-2.0
URL:            https://pypi.org/project/typing-extensions/
Source:        https://github.com/python/typing_extensions/archive/refs/tags/v4.15.0.tar.gz
# fix test on 3.14
# https://github.com/python/typing_extensions/pull/683
Patch:          https://github.com/python/typing_extensions/pull/683.patch

# Remove no_type_check_decorator from __all__ for Python >= 3.15
# https://github.com/python/typing_extensions/pull/699
Patch:          https://github.com/python/typing_extensions/commit/2638b86aad.patch

# Remove no_type_check_decorator from _typing_names, followup of the above
# https://github.com/python/typing_extensions/pull/723
Patch:          https://github.com/python/typing_extensions/pull/723.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-test

%global _description %{expand:
The typing_extensions module serves two related purposes:

- Enable use of new type system features on older Python versions. For example,
  typing.TypeGuard is new in Python 3.10, but typing_extensions allows users on
  previous Python versions to use it too.

- Enable experimentation with new type system PEPs before they are accepted and
  added to the typing module.

typing_extensions is treated specially by static type checkers such as mypy and
pyright. Objects defined in typing_extensions are treated the same way as
equivalent forms in typing.}

%description %_description


%package -n python3-typing-extensions
Summary:       %{summary}

%description -n python3-typing-extensions %_description


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n typing_extensions-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l typing_extensions


%check
cd src
%{py3_test_envvars} %{python3} -m unittest discover


%files -n python3-typing-extensions -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.15.0-4
- Prepare for Oreon 11 (RP1)
