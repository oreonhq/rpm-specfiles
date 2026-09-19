%global source0_hash a2c026226f1a1eaace81362fda27b3df479693aefe19f160d6c4c3a032add498

%global srcname %(echo %{name} | sed 's/^python-//')
Name:           python-fqdn
Version:        1.5.1
Release:        21%{?dist}
Summary:        Validates fully-qualified domain names against RFC 1123
BuildArch:      noarch
License:        MPL-2.0
URL:            https://github.com/ypcrts/fqdn
Source0:        https://github.com/ypcrts/fqdn/archive/refs/tags/v%{version}/fqdn-%{version}.tar.gz

%global _description %{expand:
Validates fully-qualified domain names against RFC 1123, so that they
are acceptable to modern browsers.}
%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# Remove coverage for fedora packaging.
sed -e '/pytest-cov/d' tox.ini
sed -e 's/--cov=[^[:blank:]]\+//' 'tox.ini'

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
