%global source0_hash 5fa714cb14516cd4d6d02b073bf8e394f0098da07bd5eb910586624e6b8ae50e

%bcond check 0

Name:           python-immutabledict
Version:        4.2.1
Release:        %autorelease
Summary:        Drop-in replacement for dictionaries where immutability is desired

License:        MIT
URL:            https://github.com/corenting/immutabledict
Source0:        %{url}/archive/v%{version}/immutabledict-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with check}
BuildRequires:  python3-pytest
%endif

%global _description %{expand:
Implements the complete mapping interface and can be used as a drop-in
replacement for dictionaries where immutability is desired. The immutabledict
constructor mimics dict, and all of the expected interfaces (iter, len, repr,
hash, getitem) are provided.}

%description %{_description}

%package -n python3-immutabledict
Summary:        %{summary}

%description -n python3-immutabledict %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n immutabledict-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files immutabledict

%if %{with check}
%check
%pytest
%endif

%files -n python3-immutabledict -f %{pyproject_files}
# Explicit license until poetry adds proper metadata
# https://github.com/python-poetry/poetry/issues/1350
%license LICENSE
%doc README.md

%changelog
%autochangelog
