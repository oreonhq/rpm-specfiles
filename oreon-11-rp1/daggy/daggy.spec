%global source0_hash 66a81b3b4d560102d00d858d4ad31a051b9e28981e341fd05ae301c12099d1fd
%undefine __cmake_in_source_build
%global _vpath_srcdir src
Name:           daggy
Version:        2.2.4
Release:        1%{?dist}
Summary:        Data Aggregation Utility and C/C++ developer library
License:        MIT
URL:            https://github.com/synacker/daggy
Source0:        https://github.com/synacker/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
ExcludeArch: s390x
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libssh2-devel
BuildRequires:  mustache-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  yaml-cpp-devel
# /oreon:deps
%description
Daggy - Data Aggregation Utility and C/C++ developer library for data streams
catching

Daggy main goals are server-less, cross-platform, simplicity and ease-of-use.

Daggy can be helpful for developers, QA, DevOps and engineers for debug,
analyze and control any data streams, including requests and responses, in
distributed network systems, for example, based on micro-service architecture.

%package devel
Summary: Development files for %{name}
%description devel
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DVERSION=%{version}.0 src
%cmake_build
%install
%cmake_install
%oreon_autofiles daggy-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:${LD_LIBRARY_PATH}
%ctest
%files -f %{oreon_filedir}/main.list
%files -n daggy-devel -f %{oreon_filedir}/daggy-devel.list

%changelog

%autochangelog
