%global source0_hash bd596550369f33ef9455566822f5a4d52852a63a33d3d70ac1fbb529b78abc7b
%bcond regenerate 0
%dnl %global max_types 16
%dnl %global max_types 5
%bcond tests 1
Name:           variant-lite
Version:        3.0.0
Release:        1%{?dist}
Summary:        Represent a type-safe union
License:        BSL-1.0
URL:            https://github.com/martinmoene/variant-lite
Source0:        https://github.com/martinmoene/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with regenerate}
%endif
%if %{with tests}
%endif
%global debug_package %{nil}
%global common_description %{expand:
A single-file header-only library to represent a type-safe union.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-variant-lite = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n variant-lite-%{version} -p1

# Unbundle lest
rm -rvf test/lest
ln -s /usr/include/lest test/lest

%if %{with regenerate}
%build

%if %{with regenerate}
%{python3} script/generate_header.py \
    %{?max_types:--max-types %{max_types}} \
    %{?max_args:--max-args %{max_args}} \
    --verbose
%endif
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if %{with tests}
%ctest
%endif
%files
%files -n variant-lite-devel -f %{oreon_filedir}/variant-lite-devel.list

%changelog

%autochangelog
%endif
