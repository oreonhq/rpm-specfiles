%global source0_hash e322802ebfd5fe79368efd864aeb87b063566ae61911dccb2714e28a45ed7561

%bcond_without optional_tests

Name:           python-sphinxcontrib-websupport
Version:        1.2.7
Release:        %autorelease
Summary:        Sphinx API for Web Apps

License:        BSD-2-Clause
URL:            https://github.com/sphinx-doc/sphinxcontrib-websupport
Source:        https://files.pythonhosted.org/packages/source/s/sphinxcontrib-websupport/sphinxcontrib-websupport-1.2.7.tar.gz
# Compatibility with Sphinx 9+
Patch:          https://github.com/sphinx-doc/sphinxcontrib-websupport/pull/91.patch
BuildArch:      noarch

%description
sphinxcontrib-websupport provides a Python API to easily integrate Sphinx
documentation into your Web application.

%package -n     python3-sphinxcontrib-websupport
Summary:        %{summary}
BuildRequires:  python3-devel

%if %{with optional_tests}
# Optional tests dep, undeclared upstream, can be skipped if needed
BuildRequires:  python3-xapian
%endif

%description -n python3-sphinxcontrib-websupport
sphinxcontrib-websupport provides a Python API to easily integrate Sphinx
documentation into your Web application.

%pyproject_extras_subpkg -n python3-sphinxcontrib-websupport whoosh

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n sphinxcontrib_websupport-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinxcontrib

%check
%tox

%files -n python3-sphinxcontrib-websupport -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.7-1
- Prepare for Oreon 11 (RP1)
