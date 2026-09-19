%global source0_hash b85c45fd4d3d92e8b18e9a5ee2da84517e8fff658e3ef5755c885b1c2a27c1fe

%global srcname types-cryptography
%global modname types_cryptography

Name:           python-%{srcname}
Version:        3.3.23
Release:        %autorelease
Summary:        Typing stubs for cryptography
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%global _description %{expand:
This is a PEP 561 type stub package for the cryptography package. It can be used
by type-checking tools like mypy, PyCharm, pytype etc. to check code that uses
cryptography. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/cryptography. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.}

%description %{_description}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%if 0%{?fedora}
%check
%py3_check_import cryptography-stubs
%endif

%files -n  python%{python3_pkgversion}-%{srcname}
%doc CHANGELOG.md
%{python3_sitelib}/cryptography-stubs
%{python3_sitelib}/%{modname}-%{version}.dist-info/

%changelog
%autochangelog
