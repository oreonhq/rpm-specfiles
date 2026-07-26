%global source0_hash 879c3e79a2729ce768ebb7d36d4609e3a78a4ca2ec3a9f12286ca057e3d0db08

Name:           python-argon2-cffi
Version:        23.1.0
Release:        %autorelease
Summary:        The secure Argon2 password hashing algorithm

License:        MIT
URL:            https://argon2-cffi.readthedocs.io/
Source:         %{pypi_source argon2_cffi}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
CFFI-based Argon2 Bindings for Python.}

%description %_description

%package -n     python3-argon2-cffi
Summary:        %{summary}

%description -n python3-argon2-cffi %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n argon2_cffi-%{version}
# don't BR coverage, we will not measure it
sed -Ei 's/"coverage[^"]+", //' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files argon2

%check
%pytest

%files -n python3-argon2-cffi -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
