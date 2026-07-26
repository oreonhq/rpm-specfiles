%global source0_hash 9882bd889f27da78add4dd6f881d25697efc740bf840274e749988d25496c8e1

%global srcname pyclipper

Name:           python-%{srcname}
Version:        1.4.0
Release:        %autorelease
Summary:        Cython wrapper for the C++ translation of the Angus Johnson's Clipper library

License:        MIT
URL:            https://pypi.org/project/pyclipper
Source:         %pypi_source %{srcname}

# Unbundle Clipper library from build entirely, so we can use the system copy.
Patch:          0001-Unbundle-Clipper-library-from-build-entirely.patch

BuildRequires:  gcc-c++
BuildRequires:  polyclipping-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
Pyclipper is a Cython wrapper exposing public functions and classes of the C++
translation of the Angus Johnson's Clipper library.

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
Pyclipper is a Cython wrapper exposing public functions and classes of the C++
translation of the Angus Johnson's Clipper library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

# Remove bundled polyclipping.
rm src/clipper.{cpp,hpp}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest}

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
