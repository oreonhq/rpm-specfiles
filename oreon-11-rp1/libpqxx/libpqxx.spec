%global source0_hash aa214df8b98672a43a39b68a37da87af1415a44965f6e484f85ca0eb4f151367
%bcond check 1
%bcond doc   1
Name:           libpqxx
Summary:        C++ client API for PostgreSQL
Epoch:          1
Version:        7.10.5
Release:        1%{?dist}
%global         forgeurl https://github.com/jtv/%{name}/
%global         tag %{version}
%forgemeta
License:        LicenseRef-Callaway-BSD
URL:            http://pqxx.org/
Source0:        %{forgeurl}archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         libpqxx-7.10.5-cxx20.patch
%if %{with check}
%endif
%if %{with doc}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libpq-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  postgresql-test-rpm-macros
BuildRequires:  xmlto
# /oreon:deps
%description
C++ client API for PostgreSQL. The standard front-end (in the sense of
"language binding") for writing C++ programs that use PostgreSQL.
Supersedes older libpq++ interface.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig
%description devel
%{summary}.

%if %{with doc}
%package doc
Summary: Developer documentation for %{name}
BuildArch: noarch
%description doc
%{summary}.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%cmake -G Ninja \
%if %{with doc}
  -DBUILD_DOC=ON
%endif
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%if %{with check}
%postgresql_tests_run
cd "%{_vpath_builddir}/test"
%__ctest -V --force-new-ctest-process %{?_smp_mflags}
cd -
%endif
%files -f %{oreon_filedir}/main.list
%files -n libpqxx-devel -f %{oreon_filedir}/libpqxx-devel.list
%files -n libpqxx-doc -f %{oreon_filedir}/libpqxx-doc.list

%changelog

%autochangelog
