%global source0_hash 8d7e97a056b1bfbfc730e69855857866729686b8c7e66a22aee81f1baeaab1ec

Name:           clazy
Summary:        Qt oriented code checker based on clang framework
Version:        1.17
Release:        2%{?dist}
License:        LGPL-2.0-or-later
URL:            https://invent.kde.org/sdk/%{name}

%if 0%{?commitdate}
Source0:        %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
Source0:        https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
%endif

Patch0:         clazy-no-rpath.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: clang-devel
BuildRequires: clang-tools-extra-devel
BuildRequires: llvm-devel
BuildRequires: perl-podlators

Requires: clang(major) = %{clang_major_version}
Requires: clang-tools-extra

%description
clazy is a compiler plugin which allows clang to understand Qt semantics.
You get more than 50 Qt related compiler warnings, ranging from unneeded
memory allocations to misusage of API, including fix-its for automatic
refactoring.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{?commitdate:%{commit}}%{!?commitdate:v%{version}}

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc HOWTO.md README.md
%license LICENSES/*
%{_bindir}/clazy
%{_bindir}/clazy-standalone
%dir %{_docdir}/clazy
%{_docdir}/clazy/*
%{_mandir}/man1/clazy.1.gz
%{_libdir}/ClazyPlugin.so
%{_libdir}/ClazyClangTidy.so
%{_datadir}/metainfo/org.kde.clazy.metainfo.xml

%changelog
%autochangelog
