%global source0_hash 52e316b03783886a8a2abdc228f7071680ba65894545cd2085ebe3cf88684a0e

%global pypi_name types-decorator
%global pypi_version 5.1.8.20240310

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        6%{?dist}
Summary:        Typing stubs for decorator

License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
 Typing stubs for decoratorThis is a [PEP 561]( type stub package for the
[decorator]( package. It can be used by type-checking tools like [mypy](
[pyright]( [pytype]( PyCharm, etc. to check code that uses decorator.This
version of types-decorator aims to provide accurate annotations for
decorator5.1.*. The source for this package can be found at All fixes for types
and metadata should be...

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
 Typing stubs for decoratorThis is a [PEP 561]( type stub package for the
[decorator]( package. It can be used by type-checking tools like [mypy](
[pyright]( [pytype]( PyCharm, etc. to check code that uses decorator.This
version of types-decorator aims to provide accurate annotations for
decorator5.1.*. The source for this package can be found at All fixes for types
and metadata should be...

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%{python3_sitelib}/decorator-stubs
%{python3_sitelib}/types_decorator-%{version}.dist-info/

%changelog
%autochangelog
