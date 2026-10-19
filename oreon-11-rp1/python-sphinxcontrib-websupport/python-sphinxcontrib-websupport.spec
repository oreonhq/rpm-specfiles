%global source0_hash e322802ebfd5fe79368efd864aeb87b063566ae61911dccb2714e28a45ed7561
%bcond_without optional_tests
Name:           python-sphinxcontrib-websupport
Version:        1.2.7
Release:        1%{?dist}
Summary:        Sphinx API for Web Apps
License:        BSD-2-Clause
URL:            https://github.com/sphinx-doc/sphinxcontrib-websupport
Source0:        https://files.pythonhosted.org/packages/source/s/sphinxcontrib_websupport/sphinxcontrib_websupport-1.2.7.tar.gz
Patch:          https://github.com/sphinx-doc/sphinxcontrib-websupport/pull/91.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.7
Requires:       python3-sphinxcontrib-websupport = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinxcontrib-websupport+test
Summary:        Metapackage for python3-sphinxcontrib-websupport test extras
Requires:       python3-sphinxcontrib-websupport = %{version}-%{release}
Provides:       python3dist(sphinxcontrib-websupport[test]) = %{version}-%{release}

%description -n python3-sphinxcontrib-websupport+test
Metapackage for python3-sphinxcontrib-websupport test extras.

%package -n       python3-sphinxcontrib-websupport+whoosh
Summary:        Metapackage for python3-sphinxcontrib-websupport whoosh extras
Requires:       python3-sphinxcontrib-websupport = %{version}-%{release}
Provides:       python3dist(sphinxcontrib-websupport[whoosh]) = %{version}-%{release}

%description -n python3-sphinxcontrib-websupport+whoosh
Metapackage for python3-sphinxcontrib-websupport whoosh extras.

%package -n       python3-sphinxcontrib-websupport+lint
Summary:        Metapackage for python3-sphinxcontrib-websupport lint extras
Requires:       python3-sphinxcontrib-websupport = %{version}-%{release}
Provides:       python3dist(sphinxcontrib-websupport[lint]) = %{version}-%{release}

%description -n python3-sphinxcontrib-websupport+lint
Metapackage for python3-sphinxcontrib-websupport lint extras.

%description
sphinxcontrib-websupport provides a Python API to easily integrate Sphinx
documentation into your Web application.

%package -n     python3-sphinxcontrib-websupport
Summary:        Sphinx API for Web Apps
BuildRequires:  python3-devel
%if %{with optional_tests}
BuildRequires:  python3-xapian
%endif
# oreon:reqs
Requires:       python3dist(sphinx) >= 5
# /oreon:reqs
%description -n python3-sphinxcontrib-websupport
sphinxcontrib-websupport provides a Python API to easily integrate Sphinx
documentation into your Web application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sphinxcontrib_websupport-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinxcontrib-websupport usr/lib/python3*/site-packages/sphinxcontrib_websupport* usr/lib64/python3*/site-packages/sphinxcontrib_websupport* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinxcontrib_websupport* usr/lib64/python3*/site-packages/sphinxcontrib_websupport* usr/bin/*

%check

%tox
%files
%files -n python3-sphinxcontrib-websupport -f %{oreon_filedir}/python3-sphinxcontrib-websupport.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.7-1
- Prepare for Oreon 11 (RP1)
