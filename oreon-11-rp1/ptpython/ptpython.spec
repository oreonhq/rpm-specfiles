%global source0_hash 11651778236de95c582b42737294e50a66ba4a21fa01c0090ea70815af478fe0
Name:           ptpython
Version:        3.0.32
Release:        1%{?dist}
Summary:        Python REPL build on top of prompt_toolkit
License:        BSD-3-Clause
URL:            https://github.com/prompt-toolkit/ptpython
Source0:        https://files.pythonhosted.org/packages/source/p/ptpython/ptpython-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
Ptpython is an advanced Python REPL built on top of the prompt_toolkit library.
It features syntax highlighting, multiline editing (the up arrow works),
autocompletion, mouse support, support for color schemes, support for bracketed
paste, both Vi and Emacs key bindings, support for double width (Chinese)
characters, and many other things.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 68
Requires:       python3-ptpython = %{version}-%{release}
# /oreon:deps
%package -n       python3-ptpython+ptipython
Summary:        Metapackage for python3-ptpython ptipython extras
Requires:       python3-ptpython = %{version}-%{release}
Provides:       python3dist(ptpython[ptipython]) = %{version}-%{release}

%description -n python3-ptpython+ptipython
Metapackage for python3-ptpython ptipython extras.

%description %{common_description}

%package -n ptpython3
Summary:        Python REPL build on top of prompt_toolkit
BuildRequires:  python3-devel
Provides:       ptpython = %{version}-%{release}
%py_provides    python3-ptpython
%description -n ptpython3 %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
find -name \*.py | xargs sed -i -e '1 {/^#!\//d}'

%build

%pyproject_wheel
%install
%pyproject_install
%if %{without ptipython}
rm %{buildroot}%{_bindir}/ptipython*
%oreon_autofiles ptpython3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%pyproject_check_import -e ptpython.contrib.asyncssh_repl %{!?with_ptipython:-e ptpython.ipython}
%files
%files -n ptpython3 -f %{oreon_filedir}/ptpython3.list

%changelog

%autochangelog
