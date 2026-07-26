%global source0_hash ad8dc86dee3d05d70a686892a8864ec7fa797397785d59ede6aa7183475a681b

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           python-simple-websocket
Version:        1.1.0
Release:        7%{?dist}
Summary:        Simple WebSocket server and client for Python

BuildArch:      noarch
License:        MIT
URL:            https://github.com/miguelgrinberg/simple-websocket
Source:         %{url}/archive/v%{version}/simple-websocket-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

# Documentation
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%description
Simple WebSocket server and client for Python

%package -n     python3-simple-websocket
Summary:        %{summary}

%description -n python3-simple-websocket
Simple WebSocket server and client for Python.

%package        doc
Summary:        Documentation for simple-websocket

%description    doc
Documentation for simple-websocket.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n simple-websocket-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}/src" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files -l simple_websocket

%check
%py3_check_import simple_websocket
%pytest || :

%files -n python3-simple-websocket -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE
%doc CHANGES.md
%if %{with doc_pdf}
%doc docs/_build/latex/simple-websocket.pdf
%endif
%doc examples/

%changelog
%autochangelog
