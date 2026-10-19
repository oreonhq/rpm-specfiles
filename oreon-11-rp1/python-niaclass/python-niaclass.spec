%global source0_hash a57c3db2fbc89729745e2f68a386dc9ed5bd56e026b64b75838db1a1168623bb
%bcond tests 1
%bcond doc_pdf 1
Name:           python-niaclass
Version:        0.2.4
Release:        1%{?dist}
Summary:        Python framework for building classifiers using nature-inspired algorithms
License:        MIT
URL:            https://github.com/firefly-cpp/NiaClass
Source0:        https://github.com/firefly-cpp/NiaClass/archive/%{version}/NiaClass-%{version}.tar.gz
BuildArch:      noarch
%if %{with doc_pdf}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-niaclass = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-niaclass
Summary:        Python framework for building classifiers using nature-inspired algorithms
%description -n python3-niaclass

%package doc
Summary:        Documentation and examples for python-niaclass
%description doc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n NiaClass-%{version}
# The SemVer pins on dependencies are far too strict to be practical. Convert
# them to lower bounds.
sed -r -i 's/( = ")\^/\1>=/' pyproject.toml
# Similarly, we cannot respect an upper bound on the Python interpreter
# version.
sed -r -i 's/^(python = "[^"]+),[[:blank:]]*<[^"]+"/\1"/' pyproject.toml

%build

%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif
%install
%pyproject_install
%oreon_autofiles python3-niaclass usr/lib/python3*/site-packages/niaclass* usr/lib64/python3*/site-packages/niaclass* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/niaclass* usr/lib64/python3*/site-packages/niaclass* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%if %{with tests}
%pytest
%endif
%files
%files -n python3-niaclass -f %{oreon_filedir}/python3-niaclass.list
%files -n python-niaclass-doc -f %{oreon_filedir}/python-niaclass-doc.list

%changelog

%autochangelog
