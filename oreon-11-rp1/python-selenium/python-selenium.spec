%global source0_hash 0bd564ee166980d419a8aaf4ac00289bc152afcf2eadca5efe8c8e36711853fd

%global srcname selenium

Name:          python-%{srcname}
Version:       4.20.0
Release:       %autorelease
Summary:       Python bindings for Selenium
License:       Apache-2.0
URL:           http://docs.seleniumhq.org/

Source0:       %pypi_source

BuildArch:     noarch

Patch1:        selenium-use-without-bundled-libs.patch

%description
The selenium package is used automate web browser interaction from Python.

Several browsers/drivers are supported (Firefox, Chrome, Internet Explorer,
PhantomJS), as well as the Remote protocol.

%package -n python3-%{srcname}
Summary:       Python bindings for Selenium

BuildRequires: pyproject-rpm-macros
BuildRequires: python3-devel
Requires:      python3-rdflib
BuildArch:     noarch

%description -n python3-%{srcname}
The selenium package is used automate web browser interaction from Python.

Several browsers/drivers are supported (Firefox, Chrome, Internet Explorer,
PhantomJS), as well as the Remote protocol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
find . -type f -name "*.py" -exec sed -i '1{/^#!/d;}' {} \;

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}
sed -ie '/x_ignore_nofocus.so$/d' %pyproject_files
rm -f %{buildroot}%{python3_sitelib}/selenium/webdriver/firefox/amd64/x_ignore_nofocus.so
rm -f %{buildroot}%{python3_sitelib}/selenium/webdriver/firefox/x86/x_ignore_nofocus.so

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %pyproject_files
%license LICENSE
%doc CHANGES README.rst

%changelog
%autochangelog
