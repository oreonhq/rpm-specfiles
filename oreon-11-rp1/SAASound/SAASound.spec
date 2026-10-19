%global source0_hash a8363bbf91357b1ffb5d840b067316cc2ecc491edb18a7c76aa049a93827753e
Name:           SAASound
Version:        3.2
Release:        42%{?dist}
Summary:        Phillips SAA 1099 sound chip emulator library
License:        LicenseRef-Callaway-BSD
URL:            http://simonowen.com/sam/saasound
Source0:        http://simonowen.com/sam/saasound/%{name}-%{version}.tar.gz
Patch0:         SAASound-3.2-fixweaksymbol.patch
Patch1:         SAASound-3.2-configure-c99.patch
Provides:       saasound = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
Phillips SAA 1099 sound chip emulator library

%package devel
Summary:        Development files for SAASound
Requires:       SAASound = %{version}-%{release}
Provides:       saasound-devel = %{version}-%{release}
%description devel
Development files for SAASound

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n SAASound-devel -f %{oreon_filedir}/SAASound-devel.list

%changelog

%autochangelog
