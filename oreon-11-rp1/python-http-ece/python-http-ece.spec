%global source0_hash 99972952ad3251e8a02cd7dfe08f2b99dcd327f94827a498254a86f1343e0340

%global modname http-ece

Name:               python-http-ece
Version:            1.2.1
Release:            7%{?dist}
Summary:            A simple implementation of the encrypted content-encoding

License:            MIT
URL:                https://github.com/web-push-libs/encrypted-content-encoding
Source0:            %{url}/archive/%{version}/encrypted-content-encoding-%{version}.tar.gz
BuildArch:          noarch

%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-pytest
BuildRequires:      python%{python3_pkgversion}-pytest-cov
BuildRequires:      python%{python3_pkgversion}-coverage
BuildRequires:      python%{python3_pkgversion}-cryptography

%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_version} version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n encrypted-content-encoding-%{version} -p1

%generate_buildrequires
cd python
%pyproject_buildrequires

%build
cd python
%pyproject_wheel

%install
cd python
%pyproject_install
%pyproject_save_files -l http_ece -L

%check
%pyproject_check_import

cd python
%pytest

%files -n python%{python3_pkgversion}-%{modname} -f %{pyproject_files}
%doc python/README.rst python/*.md

%changelog
%autochangelog
