%global source0_hash 60d1ea8779471bb851b89b49ce44eecb78e46265be1a6e9320a28b100c8df44f
Name:           freealut
Version:        1.1.0
Release:        1%{?dist}
Summary:        Implementation of OpenAL's ALUT standard
License:        LicenseRef-Callaway-LGPLv2
URL:            http://openal.org/
Source0:        http://openal.org/openal_webstf/downloads/freealut-1.1.0.tar.gz
Patch0:         freealut-openal.patch
Patch1:         freealut-multiarch.patch
# oreon:deps
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openal-soft-devel
# /oreon:deps
%description
freealut is a free implementation of OpenAL's ALUT standard. See the file
AUTHORS for the people involved.

%package devel
Summary:        Development files for freealut
Requires:       %{name} = %{version}-%{release} 
Requires:       pkgconfig
Requires:       openal-soft-devel
%description devel
Development headers and libraries needed for freealut development

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0
%patch -P1
libtoolize
autoreconf

%build

%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/libalut.la
touch -r ChangeLog $RPM_BUILD_ROOT/%{_bindir}/freealut-config
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n freealut-devel -f %{oreon_filedir}/freealut-devel.list

%changelog

%autochangelog
