%global source0_hash 4d88e5ed0cf0b280a2928321136a47b929549f6b80d431eadbcc554368d6f216

%{?python_enable_dependency_generator}
%global modname backlash

Name:               python-backlash
Version:            0.4.0
Release:            6%{?dist}
Summary:            Standalone WebOb port of the Werkzeug Debugger

License:            MIT
URL:                https://pypi.io/project/backlash
Source0:            %pypi_source backlash

BuildArch:          noarch

%global _description\
backlash is a standalone version of the Werkzeug Debugger based on WebOb\
adapted to support for Python3.\
\
backlash has born as a future replacement for WebError in upcoming TurboGears2\
versions.

%description %_description

%package -n python3-backlash
Summary:            Standalone WebOb port of the Werkzeug Debugger with Python3 support meant to replace WebError in TurboGears2
%{?python_provide:%python_provide python3-backslash}
Requires:           open-sans-fonts

%description -n python3-backlash %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

# Fix license tag
#sed -i 's/license = "MIT"/license = { text = "MIT" }/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x tests}

%build
%pyproject_wheel

%install
%pyproject_install
ln -sfv /usr/share/fonts/open-sans/OpenSans-Regular.ttf %{buildroot}/%{python3_sitelib}/%{modname}/statics/opensans.ttf
%pyproject_save_files backlash

%check
%pyproject_check_import

%files -n python3-backlash -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
