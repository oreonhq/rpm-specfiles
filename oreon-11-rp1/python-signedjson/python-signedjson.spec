%global source0_hash cd91c56af53f169ef032c62e9c4a3292dc158866933318d0592e3462db3d6492

%global srcname signedjson
%global _description %{expand:
Features:
* More than one entity can sign the same object.
* Each entity can sign the object with more than one key making it easier
  to rotate keys
* ED25519 can be replaced with a different algorithm.
* Unprotected data can be added to the object under the "unsigned" key.}

Name:           python-%{srcname}
Version:        1.1.4
Release:        11%{?dist}
Summary:        Sign JSON with Ed25519 signatures

License:        Apache-2.0
URL:            https://github.com/matrix-org/python-signedjson
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%check
%pytest -v

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md

%changelog
%autochangelog
