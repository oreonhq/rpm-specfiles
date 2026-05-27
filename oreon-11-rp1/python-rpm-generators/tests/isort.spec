%global source0_hash none

Name:           isort
Version:        5.7.0
Release:        0
Summary:        A Python package with a console_scripts entrypoint
License:        MIT
Source0:        https://files.pythonhosted.org/packages/source/i/isort/isort-5.7.0.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# Turn off Python bytecode compilation because the build would fail without Python %%{python3_test_version}
%define __brp_python_bytecompile %{nil}

%description
...

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup

%build
%py3_build

%install
%py3_install

# A fake installation by a different Python version:
%if "%{python3_version}" != "%{python3_test_version}"
mv %{buildroot}%{_prefix}/lib/python%{python3_version} \
   %{buildroot}%{_prefix}/lib/python%{python3_test_version}
mv %{buildroot}%{_prefix}/lib/python%{python3_test_version}/site-packages/%{name}-%{version}-py%{python3_version}.egg-info \
   %{buildroot}%{_prefix}/lib/python%{python3_test_version}/site-packages/%{name}-%{version}-py%{python3_test_version}.egg-info
%endif

%files
%{_bindir}/%{name}*
%{_prefix}/lib/python%{python3_test_version}/site-packages/%{name}*
