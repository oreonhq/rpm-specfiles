%global source0_hash 14b2e1eb528d77bc0f4c5bd1a7ebc05e02b5b41beefb7e8567c9675b8b13bcf4
%global pypi_name ujson

Name:           python-ujson
Version:        5.12.0
Release:        %autorelease
Summary:        Ultra fast JSON encoder and decoder written in pure C

License:        BSD-3-Clause AND TCL
URL:            https://github.com/ultrajson/ultrajson
Source:         %{pypi_source ujson}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(double-conversion)
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
UltraJSON is an ultra fast JSON encoder and decoder written in pure C with
bindings for Python.}

%description %{_description}

%package -n python3-ujson
Summary:        %{summary}

%description -n python3-ujson %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n ujson-%{version} -p1
rm -rv src/ujson/deps

%generate_buildrequires
%pyproject_buildrequires

%build
export UJSON_BUILD_NO_STRIP=1
export UJSON_BUILD_DC_INCLUDES="$(pkg-config --variable=includedir double-conversion)/double-conversion"
export UJSON_BUILD_DC_LIBS="$(pkg-config --libs double-conversion)"
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ujson

%check
%pytest -v

%files -n python3-ujson -f %{pyproject_files}
%doc README.md
%dir %{python3_sitearch}/ujson-stubs
%{python3_sitearch}/ujson-stubs/__init__.pyi

%changelog
%autochangelog
