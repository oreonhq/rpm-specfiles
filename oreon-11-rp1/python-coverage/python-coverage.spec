%global source0_hash none

#global prever b1

Name:           python-coverage
Summary:        Code coverage testing module for Python
Version:        7.13.5
Release:        1%{?dist}
# There is a jquery file in tests/ that is MIT OR GPL-2.0-only
# but it does not end up in the binary package
License:        Apache-2.0
URL:            http://nedbatchelder.com/code/modules/coverage.html
Source0:        https://pypi.python.org/packages/source/c/coverage/coverage-7.13.5%{?prever}.tar.gz
BuildRequires:  gcc

%description
Coverage.py is a Python module that measures code coverage during Python
execution. It uses the code analysis tools and tracing hooks provided in the
Python standard library to determine which lines are executable, and which
have been executed.

%{?pyproject_extras_subpkg:%pyproject_extras_subpkg -n python%%{python3_pkgversion}-coverage toml}

%package -n python%{python3_pkgversion}-coverage
Summary:        Code coverage testing module for Python 3
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  pyproject-rpm-macros
# As the "coverage" executable requires the setuptools at runtime (#556290),
# so the "python3-coverage" executable requires python3-setuptools:
Requires:       python%{python3_pkgversion}-setuptools
Provides:       bundled(js-jquery) = 1.11.1
Provides:       bundled(js-jquery-debounce) = 1.1
Provides:       bundled(js-jquery-hotkeys) = 0.8
Provides:       bundled(js-jquery-isonscreen) = 1.2.0
Provides:       bundled(js-jquery-tablesorter)

%description -n python%{python3_pkgversion}-coverage
Coverage.py is a Python 3 module that measures code coverage during Python
execution. It uses the code analysis tools and tracing hooks provided in the
Python standard library to determine which lines are executable, and which
have been executed.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n coverage-%{version}%{?prever}

find . -type f -exec chmod 0644 \{\} \;
sed -i 's/\r//g' README.rst

%generate_buildrequires
%pyproject_buildrequires -x toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l coverage
rm %{buildroot}/%{_bindir}/coverage

# make compat symlinks
pushd %{buildroot}%{_bindir}
ln -s coverage-%{python3_version} coverage-3
ln -s coverage-%{python3_version} coverage
popd

%files -n python%{python3_pkgversion}-coverage -f %{pyproject_files}
%license NOTICE.txt
%doc README.rst
%{python3_sitearch}/a1_coverage.pth
%{_bindir}/coverage
%{_bindir}/coverage3
%{_bindir}/coverage-3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.13.5-1
- Prepare for Oreon 11 (RP1)
