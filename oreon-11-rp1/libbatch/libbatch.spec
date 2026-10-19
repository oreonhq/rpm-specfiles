%global source0_hash a2b5bdf7db95db31ba08b7d07d748141dfadfb537ccc742108e0ceb0a4947cc1
Name:           libbatch
Version:        2.4.5
Release:        1%{?dist}
Summary:        Generic batch management library
License:        LicenseRef-Callaway-LGPLv2
URL:            http://git.salome-platform.org/gitweb/?p=tools/libbatch.git
Source0:        http://files.salome-platform.org/Salome/other/libBatch-%{version}.tar.gz
Patch0:         libbatch_libdir.patch
Patch1:         libbatch_soversion.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  swig
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake
Requires:       filesystem
%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so|%{_datadir}/myapp/.*)$
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libBatch-%{version}
%oreon_prep
%build

%cmake -DLIBBATCH_PYTHONPATH=%{python3_sitearch}
%cmake_build
%install
%cmake_install
install -Dpm 0644 %{buildroot}%{_datadir}/%{name}/misc/check_libbatch.m4 %{buildroot}%{_datadir}/aclocal/check_libbatch.m4
rm -rf %{buildroot}%{_datadir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libbatch-devel -f %{oreon_filedir}/libbatch-devel.list

%changelog

%autochangelog
