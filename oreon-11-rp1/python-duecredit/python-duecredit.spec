%global source0_hash 7b5c1ae10927f9e02cf4d54e2c74a8aa00cd29c38d637defe3c948d3d8e9f33a
%bcond matplotlib 1
%bcond numpy 1
%bcond pandas 1
%bcond scipy 1
%bcond sklearn 1
%bcond statsmodels 1
%bcond pymvpa2 0
%bcond psychopy 0
Name:           python-duecredit
Version:        0.11.2
Release:        1%{?dist}
Summary:        Automated collection and reporting of citations
License:        BSD-2-Clause-Views
URL:            https://github.com/duecredit/duecredit
Source0:        https://files.pythonhosted.org/packages/source/d/duecredit/duecredit-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-duecredit = %{version}-%{release}
# /oreon:deps
%package -n       python3-duecredit+tests
Summary:        Metapackage for python3-duecredit tests extras
Requires:       python3-duecredit = %{version}-%{release}
Provides:       python3dist(duecredit[tests]) = %{version}-%{release}

%description -n python3-duecredit+tests
Metapackage for python3-duecredit tests extras.

%description
\
duecredit is being conceived to address the problem of inadequate citation of
scientific software and methods, and limited visibility of donation requests
for open-source software.

It provides a simple framework (at the moment for Python only) to embed
publication or other references in the original code so they are automatically
collected and reported to the user at the necessary level of reference detail,
i.e. only references for actually used functionality will be presented back if
software provides multiple citeable implementations.

%package -n python3-duecredit
Summary:        Automated collection and reporting of citations
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}
%if %{with matplotlib}
BuildRequires:  %{py3_dist matplotlib}
%endif
%if %{with numpy}
BuildRequires:  %{py3_dist numpy}
%endif
%if %{with pandas}
BuildRequires:  %{py3_dist pandas}
%endif
%if %{with scipy}
BuildRequires:  %{py3_dist scipy}
%endif
%if %{with sklearn}
BuildRequires:  %{py3_dist scikit-learn}
%endif
%if %{with statsmodels}
BuildRequires:  %{py3_dist statsmodels}
%endif
%if %{with pymvpa2}
BuildRequires:  %{py3_dist pymvpa2}
%endif
%if %{with psychopy}
BuildRequires:  %{py3_dist psychopy}
%endif
BuildRequires:  help2man
# oreon:reqs
Requires:       python3dist(citeproc-py) >= 0.5
# /oreon:reqs
%description -n python3-duecredit
\
duecredit is being conceived to address the problem of inadequate citation of
scientific software and methods, and limited visibility of donation requests
for open-source software.

It provides a simple framework (at the moment for Python only) to embed
publication or other references in the original code so they are automatically
collected and reported to the user at the necessary level of reference detail,
i.e. only references for actually used functionality will be presented back if
software provides multiple citeable implementations.

%package doc
Summary:        Documentation for %{name}
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n duecredit-%{version}

# remove coverage stuff
sed -i '/--cov/ d' tox.ini

%build

%pyproject_wheel
%install
%pyproject_install
mkdir man
%{py3_test_envvars} help2man --section 1 --no-discard-stderr \
--no-info --output man/duecredit.1 duecredit
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 man/duecredit.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles python3-duecredit usr/lib/python3*/site-packages/duecredit* usr/lib64/python3*/site-packages/duecredit* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/duecredit* usr/lib64/python3*/site-packages/duecredit* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

k="${k-}${k+ and }not test_noincorrect_import_if_no_lxml_numpy[kwargs1-env2]"
%{pytest} duecredit/tests --ignore=duecredit/tests/test_io.py -rs -k "${k-}"
%files
%files -n python3-duecredit -f %{oreon_filedir}/python3-duecredit.list
%files -n python-duecredit-doc -f %{oreon_filedir}/python-duecredit-doc.list

%changelog

%autochangelog
