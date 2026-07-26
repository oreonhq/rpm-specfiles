%global source0_hash 1086f82fbf30b0618b1953b05d33db62c68fc7ce49391ce1374192f776fde72d

%global commit 97d2850af13c339369093b78abe5265845d78220
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           linenoise
Version:        1.0
Release:        14.20200312git%{shortcommit}%{?dist}
Summary:        Minimal replacement for readline
License:        BSD-2-Clause
URL:            https://github.com/antirez/linenoise
Source0:        https://github.com/antirez/linenoise/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         %{name}-build-shared-lib.patch
Patch1:         %{name}-symbol-visibility.patch
Patch2:         %{name}-add-linenoiseWasInterrupted-symbol.patch
Patch3:         %{name}-CVE-2025-9810.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: make

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description
Linenoise is a replacement for the readline line-editing library with the goal 
of being smaller.

%description devel
This package contains files needed for developing software that uses
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
LIBDIR="%{_libdir}" INCLUDEDIR="%{_includedir}" CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
LIBDIR="%{_libdir}" INCLUDEDIR="%{_includedir}" CFLAGS="%{optflags}" make %{?_smp_mflags} DESTDIR="%{buildroot}" install

%files
%license LICENSE
%doc README.markdown
%{_libdir}/liblinenoise.so.*

%files devel
%doc example.c
%{_includedir}/linenoise.h
%{_libdir}/liblinenoise.so

%ldconfig_scriptlets

%changelog
%autochangelog
