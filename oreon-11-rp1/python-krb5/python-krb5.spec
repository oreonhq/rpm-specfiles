%global source0_hash ed5f13d5031489b10d8655c0ada28a81c2391b3ecb8a08c6d739e1e5835bc450

Name:           python-krb5
Version:        0.7.1
Release:        %autorelease
Summary:        Kerberos API bindings for Python
License:        MIT
URL:            https://github.com/jborean93/pykrb5
Source:         %{pypi_source krb5}

BuildRequires:  gcc
BuildRequires:  krb5-devel
# for /usr/sbin/kdb5_util in tests
BuildRequires:  krb5-server
# for /usr/bin/kinit in tests
BuildRequires:  krb5-workstation

%global _description %{expand:
This library provides Python functions that wraps the Kerberos 5 C API.  Due to
the complex nature of this API it is highly recommended to use something like
python-gssapi which exposes the Kerberos authentication details through GSSAPI.}

%description %_description

%package -n python3-krb5
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-k5test

%description -n python3-krb5 %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n krb5-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l krb5

%check
%pytest --verbose

%files -n python3-krb5 -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
