%global source0_hash 7fbc547d65fe3520ec3ededc8e2963afd9275863818dcfbf17ded8457274321c

%global pypi_name secure_cookie
%global src_name secure-cookie

Name:		python-%{pypi_name}
Version:	0.2.0
Release:	19%{?dist}
Summary:	Provides interfaces for secure cookies and sessions in WSGI applications
License:	BSD-3-Clause
URL:		https://pypi.org/project/%{src_name}
Source0:	%{pypi_source %{src_name}}

BuildArch:	noarch

%global common_desc\
Provides interfaces for secure cookies and sessions in WSGI applications.\
Secure cookies are cryptographically signed (but not encrypted) to prevent\
tampering. Sessions are data associated with a given user across requests\
and responses.

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:		Provides interfaces for secure cookies and sessions in WSGI applications
BuildRequires:	python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{src_name}-%{version}
# Remove bundled egg-info
rm -rf %{src_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst CHANGES.rst
%license LICENSE.rst

%changelog
%autochangelog
