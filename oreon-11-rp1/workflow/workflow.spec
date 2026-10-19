%global source0_hash 321152d9c9c1d5d0182c098e631f5ccb23f4675760933930f18395a0bb69fac3
Summary:        C++ parallel computing and asynchronous networking engine
Name:           workflow
License:        Apache-2.0 AND BSD-2-Clause AND Zlib AND GPL-2.0-or-later
Version:        1.1.0
Release:        1%{?dist}
URL:            https://github.com/sogou/workflow
Source0:        https://github.com/sogou/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          workflow-0.11.10-test-c++17.patch
%ifnarch %{ix86}
%endif
%ifarch %{valgrind_arches}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  redis
BuildRequires:  sed
# /oreon:deps
%description
As Sogou`s C++ server engine, Sogou C++ Workflow supports almost all back-end
C++ online services of Sogou, including all search services, cloud input
method, online advertisements, etc., handling more than 10 billion requests
every day. This is an enterprise-level programming engine in light and elegant
design which can satisfy most C++ back-end development requirements.

%package devel
Summary:        C++ parallel computing and asynchronous networking engine
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
As Sogou`s C++ server engine, Sogou C++ Workflow supports almost all back-end
C++ online services of Sogou, including all search services, cloud input
method, online advertisements, etc., handling more than 10 billion requests
every day. This is an enterprise-level programming engine in light and elegant
design which can satisfy most C++ back-end development requirements.

%package docs
Summary:       C++ parallel computing and asynchronous networking engine
BuildArch:     noarch
%description docs
As Sogou`s C++ server engine, Sogou C++ Workflow supports almost all back-end
C++ online services of Sogou, including all search services, cloud input
method, online advertisements, etc., handling more than 10 billion requests
every day. This is an enterprise-level programming engine in light and elegant
design which can satisfy most C++ back-end development requirements.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Rename files to make installation of documentation easier
pushd docs
pushd en
rename .md .en.md *.md
mv *.* ..
popd
popd

%build

%cmake -GNinja
%cmake_build
rm -r _include
mkdir -p _include/workflow
ln -s src/algorithm/*.h   _include/workflow/
ln -s src/algorithm/*.inl _include/workflow/
ln -s src/client/*.h      _include/workflow/
ln -s src/kernel/*.h      _include/workflow/
ln -s src/factory/*.h     _include/workflow/
ln -s src/factory/*.inl   _include/workflow/
ln -s src/manager/*.h     _include/workflow/
ln -s src/manager/*.inl   _include/workflow/
ln -s src/nameservice/*.h _include/workflow/
ln -s src/protocol/*.h    _include/workflow/
ln -s src/protocol/*.inl  _include/workflow/
ln -s src/server/*.h      _include/workflow/
ln -s src/util/*.h        _include/workflow/
%install
%cmake_install
rm %{buildroot}/%{_docdir}/%{name}-%{version}/README.md
rm %{buildroot}/%{_libdir}/libworkflow.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n workflow-devel -f %{oreon_filedir}/workflow-devel.list
%files -n workflow-docs -f %{oreon_filedir}/workflow-docs.list

%changelog

%autochangelog
