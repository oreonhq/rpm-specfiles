%global source0_hash 170ac7aad9c8f61c4400b7ec64d2b944c2158ad328d725818095c42950a3675c

%global pypi_name sphinx_py3doc_enhanced_theme
%global srcname sphinx-py3doc-enhanced-theme
%global pkgname sphinx-theme-py3doc-enhanced
%global desc Theme based on the theme of https://docs.python.org/3/ with some responsive\
enhancements.

Name:           python-%{pkgname}
Version:        2.4.0
Release:        19%{?dist}
Summary:        Theme based on the theme of https://docs.python.org/3/

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %pypi_source %{srcname}

BuildArch:      noarch

%description
%desc

%package -n     python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
Provides:       python%{python3_pkgversion}-%{pypi_name} = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{pkgname}
%desc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python%{python3_pkgversion}-%{pkgname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
