%global source0_hash ad8dc86dee3d05d70a686892a8864ec7fa797397785d59ede6aa7183475a681b
%bcond doc_pdf 1
Name:           python-simple-websocket
Version:        1.1.0
Release:        1%{?dist}
Summary:        Simple WebSocket server and client for Python
BuildArch:      noarch
License:        MIT
URL:            https://github.com/miguelgrinberg/simple-websocket
Source0:        https://github.com/miguelgrinberg/simple-websocket/archive/v%{version}/simple-websocket-%{version}.tar.gz
%if %{with doc_pdf}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-simple-websocket = %{version}-%{release}
# /oreon:deps
%package -n       python3-simple-websocket+dev
Summary:        Metapackage for python3-simple-websocket dev extras
Requires:       python3-simple-websocket = %{version}-%{release}
Provides:       python3dist(simple-websocket[dev]) = %{version}-%{release}

%description -n python3-simple-websocket+dev
Metapackage for python3-simple-websocket dev extras.

%package -n       python3-simple-websocket+docs
Summary:        Metapackage for python3-simple-websocket docs extras
Requires:       python3-simple-websocket = %{version}-%{release}
Provides:       python3dist(simple-websocket[docs]) = %{version}-%{release}

%description -n python3-simple-websocket+docs
Metapackage for python3-simple-websocket docs extras.

%description
Simple WebSocket server and client for Python

%package -n     python3-simple-websocket
Summary:        Simple WebSocket server and client for Python
%description -n python3-simple-websocket
Simple WebSocket server and client for Python.

%package        doc
Summary:        Documentation for simple-websocket
%description    doc
Documentation for simple-websocket.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir simple-websocket-%{version}
%oreon_prep
%build

%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}/src" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif
%install
%pyproject_install
%oreon_autofiles python3-simple-websocket usr/lib/python3*/site-packages/simple_websocket* usr/lib64/python3*/site-packages/simple_websocket* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/simple_websocket* usr/lib64/python3*/site-packages/simple_websocket* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%py3_check_import simple_websocket
%pytest || :
%files
%files -n python3-simple-websocket -f %{oreon_filedir}/python3-simple-websocket.list
%files -n python-simple-websocket-doc -f %{oreon_filedir}/python-simple-websocket-doc.list

%changelog

%autochangelog
