%global source0_hash 2e48ee864884ec4a3a34bfa8c9ab9999f688286eb714a15a43ec9d068c36557b

%global srcname cairocffi

Name:           python-cairocffi
Version:        1.7.1
Release:        %autorelease
Summary:        cffi-based cairo bindings for Python
License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/cairocffi/
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
# required to run the test suite
BuildRequires:  cairo
BuildRequires:  gdk-pixbuf2
BuildRequires:  xwayland-run
# Both weston and mutter appear to work. We pick weston explicitly, here and in
# the xwfb-run invocation, to accommodate different defaults in Fedora and EL.
# Details: https://src.fedoraproject.org/rpms/python-cairocffi/pull-request/14
BuildRequires:  weston

%global _description\
cairocffi is a CFFI-based drop-in replacement for Pycairo, a set of\
Python bindings and object-oriented API for cairo.  Cairo is a 2D\
vector graphics library with support for multiple backends including\
image buffers, PNG, PostScript, PDF, and SVG file output.

%description %_description

%package -n python3-cairocffi
Summary:        cffi-based cairo bindings for Python
Requires:       cairo
# required by cairocffi.pixbuf
Requires:       gdk-pixbuf2
Requires:       glib2
Requires:       gtk3

%description -n python3-cairocffi %_description

%pyproject_extras_subpkg -n python3-cairocffi xcb

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cairocffi-%{version} -p1
sed -i -e "s/, 'ruff'//" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test,xcb

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cairocffi

%check
# test_xcb.py needs a display
%global __pytest xwfb-run -c weston -- /usr/bin/pytest
%pytest -v --pyargs cairocffi

%files -n python3-cairocffi -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
