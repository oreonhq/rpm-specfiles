%global source0_hash 683adb7d99d03f6ee7985173a206a2243f76632682334ced4cae2fcd20c83bc9

#https://fedoraproject.org/wiki/Changes/Harden_All_Packages#Troubleshooting_steps_for_package_maintainers
%undefine _hardened_build

Name:           libgdiplus
Version:        6.2
Release:        3%{?dist}
Summary:        An Open Source implementation of the GDI+ API
License:        MIT
URL:            https://gitlab.winehq.org/mono/libgdiplus
Source0:        https://dl.winehq.org/mono/sources/libgdiplus/%{name}-%{version}.tar.gz
BuildRequires:  gcc gcc-c++
BuildRequires:  freetype-devel glib2-devel libjpeg-devel libtiff-devel
BuildRequires:  libpng-devel fontconfig-devel
BuildRequires:  cairo-devel giflib-devel libexif-devel
BuildRequires:  zlib-devel
BuildRequires:  pango-devel
BuildRequires: make

%description
An Open Source implementation of the GDI+ API, it is part of the Mono 
Project

%package devel
Summary: Development files for libgdiplus
Requires: %{name} = %{version}-%{release}

%description devel
Development files for libgdiplus

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

CFLAGS="$RPM_OPT_FLAGS -Wl,-z,lazy"
CXXFLAGS="$RPM_OPT_FLAGS -Wl,-z,lazy"

export CFLAGS
export CXXFLAGS

%build
%configure --disable-static --with-pango
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc NEWS README.md TODO AUTHORS ChangeLog
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so

%changelog
%autochangelog
