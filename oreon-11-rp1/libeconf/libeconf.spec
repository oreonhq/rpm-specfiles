%global source0_hash 7c311d55237f1fc6ac437caca194d170c9cae314235d60a9fbf11e980114e25e
%undefine __cmake_in_source_build
%global somajor 0
Name:           libeconf
Version:        0.8.4
Release:        1%{?dist}
Summary:        Enhanced config file parser library
License:        MIT
URL:            https://github.com/openSUSE/libeconf
Source0:        https://github.com/openSUSE/libeconf/archive/refs/tags/v0.8.4.tar.gz#/libeconf-0.8.4.tar.gz
Patch0101:      0001-cmake-no-install-html.patch
Patch0102:      0002-disable-test.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
libeconf is a highly flexible and configurable library to parse and manage
key=value configuration files. It reads configuration file snippets from
different directories and builds the final configuration file from it.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        utils
Summary:        Utilities for manipulating config files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    utils
The %{name}-utils package contains utilities for manipulating
configuration files from applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libeconf-devel -f %{oreon_filedir}/libeconf-devel.list
%files -n libeconf-utils -f %{oreon_filedir}/libeconf-utils.list

%changelog

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.9-4
- Fix Source0 GitHub archive URL for spectool

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.9-3
- Prepare for Oreon 11 (RP1)
