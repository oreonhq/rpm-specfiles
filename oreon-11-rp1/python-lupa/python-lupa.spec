%global source0_hash eb37ec13ee29ce95b92a1d974a646766cddb1e65d93e992739bb4850b9a98675

%global _description\
Lupa integrates the run-times of Lua or LuaJIT2 into CPython. It is a\
partial rewrite of LunaticPython in Cython with some additional features\
such as proper co-routine support.

%ifarch x86_64 aarch64
%bcond_without luajit
%else
%bcond_with luajit
%endif

%if 0%{?fedora} == 43
%bcond old_cython 1
%else
%bcond old_cython 0
%endif

Name:           python-lupa
Version:        2.6
Release:        %autorelease
Summary:        Python wrapper around Lua and LuaJIT

License:        MIT
URL:            https://pypi.python.org/pypi/lupa
Source:         https://github.com/scoder/lupa/archive/lupa-%{version}/lupa-%{version}.tar.gz
# this could be passed via command line options or envvar if we're invoking setup.py directly
# but we're not
Patch:          lupa-default-to-no-bundle.diff

BuildRequires:  gcc
%if %{with luajit}
BuildRequires:  luajit-devel
%else
BuildRequires:  lua-devel
%endif
%if %{with old_cython}
BuildRequires:  sed
%endif

%description %_description

%package -n python3-lupa
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-setuptools

%description -n python3-lupa %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lupa-lupa-%{version} -p1
%if %{with old_cython}
for f in pyproject.toml requirements.txt; do
  sed -i 's|Cython>=3.1.6|Cython>=3.1.3|' $f
done
%endif

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l lupa

%check
# tox tries to do setup.py install and setup.py tes
# running tests directly failed because the local lupa folder
# is not functional prior to the build, which we do elsewhere
mkdir test_dir
cp -pr %{buildroot}%{python3_sitearch}/lupa test_dir
cp -pr lupa/tests test_dir/lupa/
cd test_dir
%{py3_test_envvars} %{python3} -m unittest -v

%files -n python3-lupa -f %{pyproject_files}
%doc README.rst CHANGES.rst INSTALL.rst
#{python3_sitearch}/lupa/
#{python3_sitearch}/lupa-*.egg-info

%changelog
%autochangelog
