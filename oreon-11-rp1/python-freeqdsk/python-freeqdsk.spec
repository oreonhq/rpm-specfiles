%global source0_hash 7b40430f8368a9ac130d441d43aa50944b4165c8c44fc49b752836bd8e822b4b

Name:           python-freeqdsk
Version:        0.5.2
Release:        %{autorelease}
Summary:        Read and write G-EQDSK, A-EQDSK, and P-EQDSK file formats

License:        MIT
URL:            https://github.com/freegs-plasma/FreeQDSK
Source:         %pypi_source freeqdsk

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Read and write G-EQDSK, A-EQDSK, and P-EQDSK file formats, which are
used to describe the tokamak fusion devices.
}

%description %_description

%package -n python3-freeqdsk
Summary:        %{summary}

%description -n python3-freeqdsk %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n freeqdsk-%{version}

%generate_buildrequires
%pyproject_buildrequires -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files freeqdsk

%check
%pytest

%files -n python3-freeqdsk -f %{pyproject_files}
%doc README.*

%changelog
%autochangelog
