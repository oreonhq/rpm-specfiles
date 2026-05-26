%global         modname greenlet

Name:           python-%{modname}
Version:        3.3.0
Release:        2%{?dist}
Summary:        Lightweight in-process concurrent programming
License:        MIT AND PSF-2.0
URL:            https://github.com/python-greenlet/greenlet
Source0:        https://github.com/python-greenlet/greenlet/archive/3.3.0/greenlet-3.3.0.tar.gz

# Skip leak checking to avoid a missing dependency, `objgraph`
Patch:        https://patch-diff.githubusercontent.com/raw/python-greenlet/greenlet/pull/482.patch
# Backport patch to fix python 3.15 builds
Patch:          https://patch-diff.githubusercontent.com/raw/python-greenlet/greenlet/pull/482.patch
# oreon url source checksums begin
%global source0_sha256 5d854395dc71b38a22e7e25467e7fc66e6a6fe538165318416cd2bb892692c6c
%global source0_file greenlet-3.3.0.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/greenlet-3.3.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5d854395dc71b38a22e7e25467e7fc66e6a6fe538165318416cd2bb892692c6c" || { echo "oreon: Source0 SHA256 mismatch for greenlet-3.3.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
