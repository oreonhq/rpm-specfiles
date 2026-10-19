%global source0_hash fee05740e86ee66f4540486d92683ee8e8071119907b57ca762c7e5d943ecef0
%undefine __cmake_in_source_build
%global archivename ldacBT
%global sonamebase 2
Name:           libldac
Version:        %{sonamebase}.0.2.6
Release:        1%{?dist}
Summary:        A lossy audio codec for Bluetooth connections
License:        Apache-2.0
URL:            https://github.com/EHfive/ldacBT
Source0:        https://github.com/EHfive/ldacBT/releases/download/v%{version}/ldacBT-%{version}.tar.gz
ExcludeArch:    s390x
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
# /oreon:deps
%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description
LDAC is an audio coding technology developed by Sony.
It enables the transmission of High-Resolution Audio content,
even over a Bluetooth connection.

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c -n %{archivename}

%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -DLDAC_SOFT_FLOAT=OFF \
    -DINSTALL_LIBDIR=%{_libdir}
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libldac-devel -f %{oreon_filedir}/libldac-devel.list

%changelog

%autochangelog
