%global source0_hash 9641511a6b14a77f68817f1a6e72fa9e55bc3ef2628a10011dcab07c6ba10539
%ifarch %{arm} %{ix86}
%bcond check 1
%else
%bcond check 0
%endif
%bcond_with all_tests
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%global optflags %(echo %{optflags} -Wno-error=template-id-cdtor)
%endif
Name:           dispenso
Version:        1.6.2
Release:        1%{?dist}
Summary:        A library for working with sets of tasks in parallel
%global major_ver %(c=%{version}; echo $c | cut -d. -f1)
License:        MIT
URL:            https://github.com/facebookincubator/dispenso
Source0:        https://github.com/facebookincubator/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-use-system-gtest.diff
Patch1:         %{name}-use-system-moodycamel.diff
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  moodycamel-concurrentqueue-devel
# /oreon:deps
%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       moodycamel-concurrentqueue-devel
%description    devel

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# make sure we use the system library
rm -rf dispenso/third-party

%build

%cmake \
%if %{with check}
  -DDISPENSO_BUILD_TESTS=ON \
%else
  %{nil}
%endif
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%if %{with all_tests}
%ctest
%else
EXCLUDED_TESTS='-E Priorty\.PriorityGetsCycles'
EXCLUDED_TESTS+='|TimedTaskTest'
%if 0%{?el10}
EXCLUDED_TESTS+='|TwoSubgraphs\.ReplaceSourceGraph'
EXCLUDED_TESTS+='|TwoSubgraphs\.ReplaceMiddleGraph'
EXCLUDED_TESTS+='|TwoSubgraphs\.ReplaceBothGraph'
EXCLUDED_TESTS+='|TwoSubgraphs\.PartialEvaluation'
EXCLUDED_TESTS+='|BiPropGraphTest\.SimpleEvaluation'
%endif
%ctest $EXCLUDED_TESTS
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n dispenso-devel -f %{oreon_filedir}/dispenso-devel.list

%changelog

%autochangelog
