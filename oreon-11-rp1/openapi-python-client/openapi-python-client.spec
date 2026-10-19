%global source0_hash 68f50afa07f828e2b153ce9cc34b4c856e705ae5edc6f226ffeb2561fb56e182
Name:           openapi-python-client
Version:        0.29.1
Release:        1%{?dist}
Summary:        Generate modern Python clients from OpenAPI
License:        MIT
URL:            https://github.com/openapi-generators/openapi-python-client
Source0:        https://github.com/openapi-generators/%{name}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:        openapi-python-client.man1
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) < 3.0.0
BuildRequires:  python3dist(poetry-core) >= 2.0.0
Requires:       python3-openapi-python-client = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{name}
Summary:        Generate modern Python clients from OpenAPI
%description -n python3-%{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n openapi-python-client-%{version}
# Remove upper bounds from dependencies
# https://bugzilla.redhat.com/show_bug.cgi?id=2405298
sed -i 's/,<[0-9.]*"/"/g' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1
cp %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1
gzip %{buildroot}%{_mandir}/man1/%{name}.1
%oreon_autofiles main usr/lib/python3*/site-packages/openapi_python_client* usr/lib64/python3*/site-packages/openapi_python_client* usr/bin/*

%check

%pyproject_check_import
%pytest tests
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%doc README.md CHANGELOG.md
%files
%files -n python3-openapi-python-client -f %{oreon_filedir}/python3-openapi-python-client.list

%changelog

%autochangelog
