%global source0_hash e1424e7f8cfdcb2b9daa83e5565a3789cb04b5a0910be212e3ac30feca6523ac
%bcond regenerate_cpp 1
%bcond regenerate_python 1
%bcond network_tests 0
Name:           cucumber-messages
Version:        34.2.1
%global cpp_soversion 32
Release:        1%{?dist}
Summary:        A message protocol for representing results and other information from Cucumber
License:        MIT
URL:            https://github.com/cucumber/messages
Source0:        https://github.com/cucumber/messages/archive/v%{version}/messages-%{version}.tar.gz
ExcludeArch:    %{ix86}
%if %{with regenerate_cpp} || %{with regenerate_python}
%endif
%if %{with network_tests}
%endif
%global common_description %{expand:
Cucumber Messages is a message protocol for representing results and other
information from Cucumber. The protocol aims to decouple various components of
the Cucumber platform, with the following advantages:
  • Each component only needs to know about a subset of messages
  • Gherkin is decoupled from the Cucumber execution component
  • Enables the future support other formats such as Markdown and Excel}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv_build) < 0.13.0
BuildRequires:  python3dist(uv_build) >= 0.12.0
Requires:       python3-cucumber-messages = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package cpp-libs
Summary:        Cucumber Messages for C++ (JSON schema)
%description cpp-libs %{common_description}

This package contains libraries implementing Cucumber Messages for C++.

%package cpp-devel
Summary:        Development files for using the C++ implementation of Gherkin
Requires:       %{name}-cpp-libs%{?_isa} = %{version}-%{release}
%description cpp-devel %{common_description}

This package contains header files and libraries for developing and building
programs that use Cucumber Messages for C++.

%package -n python3-cucumber-messages
Summary:        Message protocol for representing results and other information from Cucumber
BuildArch:      noarch
%description -n python3-cucumber-messages
Cucumber Messages is a message protocol for representing results and other
information from Cucumber.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n messages-%{version} -p1
# Do not upper-bound (SemVer-bound) the version of uv_build; we must work with
# what we have, and compatibility is quite good in practice.
sed -r -i 's/"(uv_build *>= *[^:]+), *<[^"]+"/"\1"/' python/pyproject.toml

%build

pushd cpp
%if %{with regenerate_cpp}
%make_build clean
%make_build generate
%endif
%cmake_build
popd
pushd python
%if %{with regenerate_python}
%make_build clean
%make_build generate
%endif
%pyproject_wheel
popd
%install
pushd cpp
%cmake_install
popd
pushd python
%pyproject_install
popd
%oreon_autofiles cucumber-messages-cpp-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cucumber-messages-cpp-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles python3-cucumber-messages usr/lib/python3*/site-packages/cucumber_messages* usr/lib64/python3*/site-packages/cucumber_messages* usr/bin/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/lib/python3*/site-packages/cucumber_messages* usr/lib64/python3*/site-packages/cucumber_messages* usr/bin/*

%check

pushd cpp
%ctest
popd
pushd python
%if %{without network_tests}
ignore="${ignore-} --ignore=tests/test_model_load.py"
%endif
%pytest ${ignore-} -v
popd
%files
%files -n cucumber-messages-cpp-libs -f %{oreon_filedir}/cucumber-messages-cpp-libs.list
%files -n cucumber-messages-cpp-devel -f %{oreon_filedir}/cucumber-messages-cpp-devel.list
%files -n python3-cucumber-messages -f %{oreon_filedir}/python3-cucumber-messages.list

%changelog

%autochangelog
