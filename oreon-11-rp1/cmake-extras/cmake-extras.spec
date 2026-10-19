%global source0_hash fa15760e81d5ff93571b55773fa4323c430d783c27a0b60107b3a0c225dd58b6
%global debug_package %{nil}
%bcond check 1
Name:           cmake-extras
Version:        1.10
Release:        1%{?dist}
Summary:        A collection of add-ons for the CMake build tool
License:        LGPL-3.0-or-later AND BSD-2-Clause
URL:            https://gitlab.com/ubports/development/core/cmake-extras
Source0:        https://gitlab.com/ubports/development/core/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Patch0:         cmake-extras-fix-find-qmlplugindump.patch
Patch1:         https://salsa.debian.org/debian-ayatana-team/cmake-extras/-/raw/master/debian/patches/1004_switch-to-python3.patch
%if %{with check}
%endif
Requires:       licensecheck
Requires:       lcov
Requires:       doxygen
Requires:       astyle
Requires:       gettext
Requires:       intltool
Requires:       vala
Requires:       pkgconfig(gio-2.0)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gobject-introspection-1.0)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  licensecheck
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  python3-clang
# /oreon:deps
%description
A collection of add-ons for the CMake build tool.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main
%if %{with check}
%check

pushd examples/copyrighttest-demo
%cmake -DCMAKE_PREFIX_PATH=%{_builddir}/%{name}-%{version}/src/CopyrightTest
%cmake_build
%ctest -E 'must_fail_1|must_fail_4'
popd
pushd examples/gsettings-demo
%cmake -DCMAKE_PREFIX_PATH=%{_builddir}/%{name}-%{version}/src/GSettings
%cmake_build
%ctest
popd
pushd examples/includechecker-demo
%cmake -DCMAKE_PREFIX_PATH=%{_builddir}/%{name}-%{version}/src/IncludeChecker
%cmake_build
%ctest
popd
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
