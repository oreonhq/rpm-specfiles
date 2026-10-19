%global source0_hash 0f466fce1acf2f63a99f784abfa68ac03b3ee8d12aa16a8cc481e4e2e03ec44c
%global commit d81c4b8aaa148e721b0bb5eb02ad87d26a3eca6c
%global snapdate 20251127
Name:           lexertl14
Summary:        The Modular Lexical Analyser Generator
Version:        0.1.0^%{snapdate}.%{sub %{commit} 1 7}
Epoch:          1
Release:        1%{?dist}
License:        BSL-1.0
URL:            https://github.com/BenHanson/lexertl14
Source0:        https://github.com/BenHanson/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
%global debug_package %{nil}
%global common_description %{expand:
This is the C++14 version of lexertl. Please prefer lexertl17 wherever
possible.}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
# /oreon:deps
%description %{common_description}

%package devel
Summary:        %{summary}
Provides:       lexertl14-static = %{epoch}:%{version}-%{release}
Conflicts:      lexertl17-devel
Obsoletes:      lexertl14-examples < 0.1.0^20240216git7a365a2-5
%description devel %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lexertl14-%{commit} -p1

# Fix line terminations (particularly for files that may be installed)
find . -type f -exec file '{}' '+' |
  grep -E '\bCRLF\b' |
  cut -d ':' -f 1 |
  xargs -r dos2unix --keepdate

%conf
%cmake -DBUILD_TESTING:BOOL=ON -DBUILD_EXAMPLES:BOOL=ON

%build

%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n lexertl14-devel -f %{oreon_filedir}/lexertl14-devel.list

%changelog

%autochangelog
