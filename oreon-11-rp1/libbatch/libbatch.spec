%global source0_hash a2b5bdf7db95db31ba08b7d07d748141dfadfb537ccc742108e0ceb0a4947cc1

Name:           libbatch
Version:        2.4.5
Release:        21%{?dist}
Summary:        Generic batch management library

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://git.salome-platform.org/gitweb/?p=tools/libbatch.git
Source0:        http://files.salome-platform.org/Salome/other/libBatch-%{version}.tar.gz
# Use lib64 on x86_64
Patch0:         libbatch_libdir.patch
# Set a library soversion
Patch1:         libbatch_soversion.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  swig

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# %%{_datadir}/cmake ownership
Requires:       cmake
# %%{_datadir}/autoconf ownership
Requires:       filesystem

# Do not check .so files in the python_sitelib directory
# or any files in the application's directory for provides
%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so|%{_datadir}/myapp/.*)$

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n libBatch-%{version}

%build
%cmake -DLIBBATCH_PYTHONPATH=%{python3_sitearch}
%cmake_build

%install
%cmake_install

# Move autoconf macros to correct place
install -Dpm 0644 %{buildroot}%{_datadir}/%{name}/misc/check_libbatch.m4 %{buildroot}%{_datadir}/aclocal/check_libbatch.m4
rm -rf %{buildroot}%{_datadir}/%{name}

%files
%license COPYING
%{_libdir}/%{name}.so.*
%{python3_sitearch}/_%{name}.so
%{python3_sitearch}/%{name}.py*
%{python3_sitearch}/__pycache__/%{name}.*

%files devel
%{_includedir}/%{name}/
%{_datadir}/cmake/%{name}/
%{_datadir}/aclocal/check_libbatch.m4
%{_libdir}/%{name}.so

%changelog
%autochangelog
