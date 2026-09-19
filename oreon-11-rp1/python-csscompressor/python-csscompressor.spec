%global source0_hash afa22badbcf3120a4f392e4d22f9fff485c044a1feda4a950ecc5eba9dd31a05

Name:           python-csscompressor
Version:        0.9.5
Release:        %autorelease
Summary:        Python port of YUI CSS Compressor

License:        BSD-3-Clause
URL:            https://github.com/sprymix/csscompressor
Source:         %{pypi_source csscompressor}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package is an almost exact port of YUI CSS Compressor to Python that
passes all the original unittests.}

%description %_description

%package -n     python3-csscompressor
Summary:        %{summary}

%description -n python3-csscompressor %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n csscompressor-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l csscompressor

%check
%pytest -v

%files -n python3-csscompressor -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
