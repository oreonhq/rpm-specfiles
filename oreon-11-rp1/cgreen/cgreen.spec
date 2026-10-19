%global source0_hash 406e3eb77fe855152ae917651a52a2445be7ccde6affbc68aad90bbe985d3869
Name:           cgreen
Version:        1.7.0
Release:        1%{?dist}
Summary:        Modern unit test and mocking framework for C and C++
License:        ISC
URL:            https://github.com/cgreen-devs/%{name}
Source0:        https://github.com/cgreen-devs/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch: s390x
# oreon:deps
BuildRequires:  asciidoctor
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  perl-interpreter
# /oreon:deps
%description
A modern, portable, cross-language unit testing and mocking framework for C
and C++.

%package devel
Summary:        Libraries and headers for developing programs with Cgreen
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Libraries and headers for developing programs with Cgreen.

%package runner
Summary:        A runner for the Cgreen unit testing and mocking framework
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description runner
A runner for the Cgreen unit testing and mocking framework.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DCGREEN_WITH_HTML_DOCS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles cgreen-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cgreen-runner usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ifarch i686
/usr/bin/ctest --test-dir redhat-linux-build --output-on-failure \
    --force-new-ctest-process -j8 \
    --exclude-regex "assertion_messages"
%else
/usr/bin/ctest --test-dir redhat-linux-build --output-on-failure \
    --force-new-ctest-process -j8
%endif
%files -f %{oreon_filedir}/main.list
%files -n cgreen-devel -f %{oreon_filedir}/cgreen-devel.list
%files -n cgreen-runner -f %{oreon_filedir}/cgreen-runner.list

%changelog

%autochangelog
