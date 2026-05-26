%global srcname itsdangerous

Name:           python-%{srcname}
Version:        2.2.0
Release:        7%{?dist}
Summary:        Library for passing trusted data to untrusted environments
License:        BSD-3-Clause
URL:            https://itsdangerous.palletsprojects.com
Source0:        https://files.pythonhosted.org/packages/source/i/itsdangerous/itsdangerous-2.2.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 e0050c0b7da1eea53ffaf149c0cfbb5c6e2e2b69c4bef22c81fa6eb73e5f6173
%global source0_file itsdangerous-2.2.0.tar.gz
# oreon url source checksums end
BuildArch:      noarch

%global _description %{expand:
Itsdangerous is a Python library for passing data through untrusted
environments (for example, HTTP cookies) while ensuring the data is not
tampered with.

Internally itsdangerous uses HMAC and SHA1 for signing by default and bases the
implementation on the Django signing module. It also however supports JSON Web
Signatures (JWS).}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
# for tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(freezegun)

%description -n python3-%{srcname} %{_description}


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/itsdangerous-2.2.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e0050c0b7da1eea53ffaf149c0cfbb5c6e2e2b69c4bef22c81fa6eb73e5f6173" || { echo "oreon: Source0 SHA256 mismatch for itsdangerous-2.2.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files itsdangerous


%check
%pytest -Wdefault


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc CHANGES.rst README.md


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.0-7
- Prepare for Oreon 11 (RP1)
