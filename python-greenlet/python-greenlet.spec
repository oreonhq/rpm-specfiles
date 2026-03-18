%global         modname greenlet

Name:           python-%{modname}
Version:        3.3.0
Release:        2%{?dist}
Summary:        Lightweight in-process concurrent programming
License:        MIT AND PSF-2.0
URL:            https://github.com/python-greenlet/greenlet
Source0:        %{url}/archive/%{version}/%{modname}-%{version}.tar.gz

# Skip leak checking to avoid a missing dependency, `objgraph`
Patch:          skip-leak-checks.patch
# Backport patch to fix python 3.15 builds
Patch:          https://patch-diff.githubusercontent.com/raw/python-greenlet/greenlet/pull/482.patch

BuildRequires:  gcc-c++

%global _description \
The greenlet package is a spin-off of Stackless, a version of CPython\
that supports micro-threads called "tasklets". Tasklets run\
pseudo-concurrently (typically in a single or a few OS-level threads)\
and are synchronized with data exchanges on "channels".

%description %{_description}

%package -n     python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-psutil

%description -n python3-%{modname} %{_description}

Python 3 version.

%package -n     python3-%{modname}-devel
Summary:        C development headers for python3-%{modname}
Requires:       python3-%{modname}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{modname}-devel
%{summary}.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
cd /
PYTHONPATH="%{buildroot}%{python3_sitearch}" \
  %{python3} -m unittest discover -v \
  -s "%{buildroot}%{python3_sitearch}/greenlet/tests" \
  -t "%{buildroot}%{python3_sitearch}"

%files -n python3-%{modname} -f %{pyproject_files}
%doc AUTHORS README.rst

%files -n python3-greenlet-devel
%{_includedir}/python%{python3_version}*/%{modname}/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.0-2
- Prepare for Oreon 11 (RP1)
