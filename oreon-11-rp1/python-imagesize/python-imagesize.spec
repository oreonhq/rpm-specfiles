%bcond_without tests

%global pypi_name imagesize
%global sum  Python module for analyzing image file headers and returning image sizes

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/shibukawa/imagesize_py
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 8e8358c4a05c304f1fccf7ff96f036e7243a189e9e42e90851993c558cfe9ee3
%global source0_file imagesize-2.0.0.tar.gz
# oreon url source checksums end
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-devel
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
%endif

%description
The imagesize package parses image file headers and returns the image sizes.

* PNG
* JPEG
* JPEG2000
* GIF

This is a pure Python library.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
The imagesize package parses image file headers and returns the image sizes.

* PNG
* JPEG
* JPEG2000
* GIF

This is a pure Python library.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/imagesize-2.0.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8e8358c4a05c304f1fccf7ff96f036e7243a189e9e42e90851993c558cfe9ee3" || { echo "oreon: Source0 SHA256 mismatch for imagesize-2.0.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%if %{with tests}
# test_get_filelike requires internet connection, hence we disable it
%pytest -v -k 'not test_get_filelike'
%endif

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.0-1
- Prepare for Oreon 11 (RP1)
