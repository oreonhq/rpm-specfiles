%global source0_hash 6638fce302d384f5f97e701d218b1c3f1e8e43159ea202e7336815094bc570d4
%global commit 669d31c24a1c173581f7abc45e73516a6434b026
%global gittag v5.0.6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           rudeconfig
Version:        5.0.6
Release:        1%{?dist}
Summary:        Library (C++ API) for reading and writing configuration/.ini files
License:        GPL-2.0-or-later
URL:            http://www.rudeserver.com/config
Source0:        https://github.com/mflood/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         %{name}-%{commit}-configure-c99.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
%{name} is a library that allows applications to read, modify
and create configuration/.ini files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{name} is a library that allows applications to read, modify
and create configuration/.ini files. The %{name}-devel package
contains libraries, header files, and documentation needed
to develop C++ applications using %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build

%configure --disable-static
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rudeconfig-devel -f %{oreon_filedir}/rudeconfig-devel.list

%changelog

%autochangelog
