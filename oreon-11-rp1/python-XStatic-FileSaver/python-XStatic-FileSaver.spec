%global source0_hash e43121a9adf3a9ceb2066db07fafb7d3b02100d3fbc0b86dcd52aa92a652a8b7

%global pypi_name XStatic-FileSaver

Name:           python-%{pypi_name}
Version:        1.3.2.0
Release:        28%{?dist}
Summary:        FilseSaver (XStatic packaging standard)

License:        MIT
URL:            https://github.com/eligrey/FileSaver.js
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
FilseSaver JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

%package -n xstatic-filesaver-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-filesaver-common
FilseSaver JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the JavaScript files.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-filesaver-common

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
FilseSaver JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Patch to use webassets directory
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/filesaver'|" xstatic/pkg/filesaver/__init__.py

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}/%{_jsdir}/filesaver
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/filesaver/data/FileSaver.js %{buildroot}/%{_jsdir}/filesaver
rmdir %{buildroot}%{python3_sitelib}/xstatic/pkg/filesaver/data/

%files -n xstatic-filesaver-common
%doc README.txt
%{_jsdir}/filesaver

%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/filesaver
%{python3_sitelib}/XStatic_FileSaver-%{version}-py3.*.egg-info
%{python3_sitelib}/XStatic_FileSaver-%{version}-py3.*-nspkg.pth

%changelog
%autochangelog
