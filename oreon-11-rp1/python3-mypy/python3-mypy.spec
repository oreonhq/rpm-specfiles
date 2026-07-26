%global source0_hash 4f0b58727dc296b92cfa3c404d31d52597de8bab0530c697f01f0d4397d6120c

Name:           python3-mypy
Version:        1.18.2
Release:        4%{?dist}
Summary:        A static type checker for Python

# The files under lib-python and lib-typing/3.2 are Python-licensed, but this
# package does not include those files
# mypy/typeshed is ASL 2.0
License:        MIT and Apache-2.0
URL:            https://github.com/python/mypy
Source0:        https://github.com/python/mypy/archive/v%{version}/mypy-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-typing-extensions
BuildRequires:  (python3-tomli if python3 < 3.11)
BuildRequires:  python3-pathspec
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-attrs
BuildRequires:  python3-filelock
BuildRequires:  python3-lxml
BuildRequires:  python3-psutil
Requires:  python3-typing-extensions

# Needed to generate the man pages
BuildRequires:  help2man
BuildRequires:  python3dist(mypy-extensions)

BuildArch:      noarch

%description
Mypy is an optional static type checker for Python.  You can add type
hints to your Python programs using the upcoming standard for type
annotations introduced in Python 3.5 beta 1 (PEP 484), and use mypy to
type check them statically. Find bugs in your programs without even
running them!

%python_extras_subpkg -n %{name} -i %{python3_sitelib}/mypy-*.dist-info dmypy,mypyc,reports,install-types,faster-cache

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n mypy-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mypy mypyc

# Generate man pages
mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'mypy %{version}-dev' \
        --no-discard-stderr -o %{buildroot}%{_mandir}/man1/mypy.1 \
        %{buildroot}%{_bindir}/mypy

PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'mypy stubgen %{version}-dev' \
        --no-discard-stderr -o %{buildroot}%{_mandir}/man1/stubgen.1 \
        %{buildroot}%{_bindir}/stubgen

%check
%pyproject_check_import
#%%pytest -k "not testI64BasicOps and not testI64ErrorValuesAndUndefined and not testI64DefaultArgValues and not testI64GlueMethodsAndInheritance and not testBoolOps"

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/mypy
%{_bindir}/mypyc
%{_bindir}/dmypy
%{_bindir}/stubgen
%{_bindir}/stubtest
%{_mandir}/man1/mypy.1*
%{_mandir}/man1/stubgen.1*

%changelog
%autochangelog
