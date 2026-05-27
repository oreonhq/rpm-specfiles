%global source0_hash 4bd8eece78bb5c1361fab95743e7100506e2408a25c4a592a0f8d349746dc5b4

# Force out of source build
%undefine __cmake_in_source_build

%global archivename ldacBT
%global sonamebase 2

Name:           libldac
Version:        %{sonamebase}.0.2.3
Release:        19%{?dist}
Summary:        A lossy audio codec for Bluetooth connections

License:        Apache-2.0
URL:            https://github.com/EHfive/ldacBT
Source0:        https://github.com/EHfive/ldacBT/releases/download/v2.0.2.3/ldacBT-2.0.2.3.tar.gz

# Upstream source throws error in a big-endian arch, see #1677491
ExcludeArch:    s390x

BuildRequires:  cmake3
BuildRequires:  gcc

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{archivename}

%build
%cmake3 \
    -DLDAC_SOFT_FLOAT=OFF \
    -DINSTALL_LIBDIR=%{_libdir}

%cmake3_build

%install
%cmake3_install

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/libldacBT_abr.so.%{sonamebase}
%{_libdir}/libldacBT_abr.so.%{sonamebase}.*
%{_libdir}/libldacBT_enc.so.%{sonamebase}
%{_libdir}/libldacBT_enc.so.%{sonamebase}.*
%{_libdir}/libldacBT_abr.so
%{_libdir}/libldacBT_enc.so

%files devel
%dir %{_includedir}/ldac
%{_includedir}/ldac/ldacBT_abr.h
%{_includedir}/ldac/ldacBT.h
%{_libdir}/pkgconfig/ldacBT-abr.pc
%{_libdir}/pkgconfig/ldacBT-enc.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.2.3-19
- Import
