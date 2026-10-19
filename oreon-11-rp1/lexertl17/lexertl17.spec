%global source0_hash 3cb24e62ac98319d578c1fa193baa4412e42ac1864d05a25bd31db6394cc8b40
Name:           lexertl17
Summary:        The Modular Lexical Analyser Generator
Epoch:          1
Version:        1.3.1
Release:        1%{?dist}
License:        BSL-1.0 AND Unicode-3.0
URL:            https://github.com/BenHanson/lexertl17
Source0:        https://github.com/BenHanson/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%if %{undefined fc43} && %{undefined fc42}
ExcludeArch:    %{ix86}
%endif
%global debug_package %{nil}
%global common_description %{expand:
lexertl is a header-only library for writing lexical analyzers. With lexertl
you can:
- Build lexical analyzers at runtime
- Scan Unicode and ASCII input
- Scan from files or memory
- Generate C++ code or even write your own code generator}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
# /oreon:deps
%description %{common_description}

%package devel
Summary:        %{summary}
Provides:       lexertl17-static = %{epoch}:%{version}-%{release}
Conflicts:      lexertl14-devel
%description devel %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lexertl17-%{version} -p1

# Fix line terminations (particularly for files that may be installed)
find . -type f -exec file '{}' '+' |
  grep -E '\bCRLF\b' |
  cut -d ':' -f 1 |
  xargs -r dos2unix --keepdate

%conf
%cmake -DBUILD_TESTING:BOOL=ON -DBUILD_EXAMPLES:BOOL=ON

%build

%cmake_build
mkdir _cleaned
cp -rvp examples _cleaned
find _cleaned/examples -type f -name CMakeLists.txt -print -delete
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n lexertl17-devel -f %{oreon_filedir}/lexertl17-devel.list

%changelog

%autochangelog
