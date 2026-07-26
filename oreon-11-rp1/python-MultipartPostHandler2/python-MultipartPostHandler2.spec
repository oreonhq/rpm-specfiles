%global source0_hash 8cb2c10aa857c1dae70cacc9bcfe9fc38c5f4971c850becca6b3f52bbcca29b7

# Tests requiring Internet connections are disabled by default
# pass --with internet to run them (e.g. when doing a local rebuild
# for sanity checks before committing)
%bcond_with internet

%global pypi_name MultipartPostHandler2
Name:           python-%{pypi_name}
Version:        0.1.5
Release:        42%{?dist}
Summary:        A handler for urllib2 to enable multipart form uploading
# License note in MultipartPostHandler.py
License:        LGPL-2.1-or-later
URL:            http://pypi.python.org/pypi/%{pypi_name}/%{version}
Source0:        http://pypi.python.org/packages/source/M/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# Several Python3 specific things, needs to be applied after 2to3!
Patch1:         %{name}-python3.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%description
This is MultipartPostHandler plus a fix for UTF-8 systems.
Enables the use of multipart/form-data for posting forms.

%package -n python3-%{pypi_name}
Summary:        %{summary}

Obsoletes:  python-%{pypi_name} < 0.1.5-12
Obsoletes:  python2-%{pypi_name} < 0.1.5-12

%description -n python3-%{pypi_name}
This is MultipartPostHandler plus a fix for UTF-8 systems.
Enables the use of multipart/form-data for posting forms.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}
rm -rf doc # no real doc there

%py3_shebang_fix .
%patch -P 1 -p1

# also change the URL in the Py2 example
sed -i 's|http://www.google.com|https://getfedora.org/|' examples/MultipartPostHandler-example.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files 'MultipartPostHandler*'

%if %{with internet}
%check
%pyproject_check_import

# do it form a different folder
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} examples/MultipartPostHandler-example.py > py3.html
# with internet
%endif 

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.txt examples/MultipartPostHandler-example.py

%changelog
%autochangelog
