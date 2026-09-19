%global source0_hash adc1976c0106919e9338db20102b91009256dcfec924a66928d7297026f72477

Name:           pycmd
Version:        1.2
Release:        42%{?dist}
Summary:        Tools for managing/searching Python related files
License:        MIT
URL:            https://pypi.python.org/pypi/pycmd
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Pycmd is a collection of command line tools for helping with Python
development.}

%description %_description

%package -n python3-pycmd
Summary:        Tools for managing/searching Python related files
Requires:       python3-setuptools
Requires:       python3-py >= 1.4.0

%description -n python3-pycmd %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# remove shebangs from all scripts
find %{buildroot}%{python3_sitelib} -name '*.py' \
     -exec sed -i -e '1{/^#!/d}' {} \;

%pyproject_save_files -l pycmd

%files -n python3-pycmd -f %{pyproject_files}
%doc README.txt
%doc CHANGELOG
%license LICENSE
%{_bindir}/py.cleanup
%{_bindir}/py.convert_unittest
%{_bindir}/py.countloc
%{_bindir}/py.lookup
%{_bindir}/py.svnwcrevert
%{_bindir}/py.which

%changelog
%autochangelog
