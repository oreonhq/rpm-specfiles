%global source0_hash 4140ca17c39e7f3d8c9a426d12126a037a27dc148e50d3f98f0d334513fcbbb2

%global modname pycxx

%if 0%{?el6}%{?el7}%{?fc29}%{?fc30}%{?fc31}
%bcond_without python2
%else
%bcond_with    python2
%endif
%if 0%{?el6}%{?el7}%{?el8}%{?el9}%{?fedora}
%bcond_without python3
%else
%bcond_with    python3
%endif

Name:           python-%{modname}
Version:        7.2.0
Release:        1%{?dist}
Summary:        Write Python extensions in C++

License:        BSD-3-Clause
URL:            http://CXX.sourceforge.net/

BuildArch:      noarch

BuildRequires:  python3-setuptools

Source0:        https://downloads.sourceforge.net/cxx/%{modname}-%{version}.tar.gz
# Patch0:  remove unnecessary 'Src/' directory from include path in sources
Patch0:         %{name}-7-change-include-paths.patch

%global _description\
PyCXX is a set of classes to help create extensions of Python in the\
C++ language. The first part encapsulates the Python C API taking care\
of exceptions and ref counting. The second part supports the building\
of Python extension modules in C++.

%description %_description

%if %{with python2}
%package -n python2-%{modname}-devel
Summary:        PyCXX header and source files
%{?python_provide:%python_provide python2-%{modname}-devel}
BuildRequires:  python2-devel
Requires:       python2
# Obsoletes/Provides needed only for EL6
Provides:       python-pycxx-devel = %{version}-%{release}
Obsoletes:      python-pycxx-devel < 7.1.3-5

%description -n python2-%{modname}-devel %_description

The python2-%{modname}-devel package provides the header and source files
for Python 2.  There is no non-devel package needed.
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{modname}-devel
Summary:        PyCXX header and source files
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}-devel}
BuildRequires:  python%{python3_pkgversion}-devel
Requires:       python%{python3_pkgversion}

%description -n python%{python3_pkgversion}-%{modname}-devel %_description

The python%{python3_pkgversion}-%{modname}-devel package provides the header and source files
for Python 3.  There is no non-devel package needed.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{modname}-%{version}

%build
# Nothing to build.

%install
%global py_install_args --prefix=%{_prefix} --install-headers=%{_includedir}/CXX --install-data=%{_usrsrc}
%{?with_python2:%py2_install -- %{py_install_args}}
%{?with_python3:%py3_install -- %{py_install_args}}

# Write pkg-config PyCXX.pc file
mkdir -p %{buildroot}%{_datadir}/pkgconfig
cat > %{buildroot}%{_datadir}/pkgconfig/PyCXX.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
includedir=%{_includedir}
srcdir=%{_usrsrc}/CXX

Name: PyCXX
Description: Write Python extensions in C++
Version: %{version}
Cflags: -I\${includedir}
EOF

%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion PyCXX)" = "%{version}"

%if %{with python2}
%files -n python2-%{modname}-devel
%doc README.html COPYRIGHT Doc/Python2/
%dir %{_includedir}/CXX
%{_includedir}/CXX/*.hxx
%{_includedir}/CXX/*.h
%{_includedir}/CXX/Python2
%{python2_sitelib}/CXX*
%dir %{_usrsrc}/CXX
%{_usrsrc}/CXX/*.cxx
%{_usrsrc}/CXX/*.c
%{_usrsrc}/CXX/Python2
%{_datadir}/pkgconfig/PyCXX.pc
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{modname}-devel
%doc README.html COPYRIGHT Doc/Python3/
%dir %{_includedir}/CXX
%{_includedir}/CXX/*.hxx
%{_includedir}/CXX/*.h
%{_includedir}/CXX/Python3
%{python3_sitelib}/CXX*
%dir %{_usrsrc}/CXX
%{_usrsrc}/CXX/*.cxx
%{_usrsrc}/CXX/*.c
%{_usrsrc}/CXX/Python3
%{_datadir}/pkgconfig/PyCXX.pc
%endif

%changelog
%autochangelog
