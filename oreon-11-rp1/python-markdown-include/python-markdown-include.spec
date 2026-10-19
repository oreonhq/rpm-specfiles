%global source0_hash 1d0623e0fc2757c38d35df53752768356162284259d259c486b4ab6285cdbbe3
Name:           python-markdown-include
Version:        0.8.1
Release:        1%{?dist}
Summary:        A Python-Markdown extension which provides an 'include' function
License:        GPL-3.0-only AND GPL-2.0-or-later
URL:            https://github.com/cmacmackin/markdown-include
Source0:        https://files.pythonhosted.org/packages/source/m/markdown-include/markdown-include-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
This is an extension to Python-Markdown which provides an “include” function,
similar to that found in LaTeX (and also the C pre-processor and Fortran). It
was originally written for the FORD Fortran auto-documentation generator.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-markdown-include = %{version}-%{release}
# /oreon:deps
%package -n       python3-markdown-include+tests
Summary:        Metapackage for python3-markdown-include tests extras
Requires:       python3-markdown-include = %{version}-%{release}
Provides:       python3dist(markdown-include[tests]) = %{version}-%{release}

%description -n python3-markdown-include+tests
Metapackage for python3-markdown-include tests extras.

%description %{common_description}

%package -n     python3-markdown-include
Summary:        A Python-Markdown extension which provides an 'include' function
# oreon:reqs
Requires:       python3dist(markdown) >= 3.0
# /oreon:reqs
%description -n python3-markdown-include %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir markdown-include-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-markdown-include usr/lib/python3*/site-packages/markdown_include* usr/lib64/python3*/site-packages/markdown_include* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/markdown_include* usr/lib64/python3*/site-packages/markdown_include* usr/bin/*

%check

%pytest
%files
%files -n python3-markdown-include -f %{oreon_filedir}/python3-markdown-include.list

%changelog

%autochangelog
