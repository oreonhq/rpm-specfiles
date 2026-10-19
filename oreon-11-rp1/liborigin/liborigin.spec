%global source0_hash b1bf35f72e39892ad351bed4a3e724aee6cfa673281dea2c78cceb9042a74e57
%undefine __cmake_in_source_build
Name:           liborigin
Version:        3.0.4
Release:        1%{?dist}
Epoch:          1
Summary:        Library for reading OriginLab OPJ project files
License:        GPL-3.0-only
URL:            https://sourceforge.net/projects/liborigin/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Provides:       liborigin2 = 2.0.0-21
Obsoletes:      liborigin2 < 2.0.0-21
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
# /oreon:deps
%description
A library for reading OriginLab OPJ project files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       liborigin2-devel = 2.0.0-21
Obsoletes:      liborigin2-devel < 2.0.0-21
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%cmake -DBUILD_STATIC_LIBS=off
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n liborigin-devel -f %{oreon_filedir}/liborigin-devel.list
%files -n liborigin-doc -f %{oreon_filedir}/liborigin-doc.list

%changelog

%autochangelog
