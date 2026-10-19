%global source0_hash a37bb0e78a419dcbeaa9c7027bcff52f5ec2367c25ec859da31dfde2928f279a
%{?mingw_package_header}
%global desc \
Graphene provides a small set of mathematical types needed to implement graphic \
libraries that deal with 2D and 3D transformations and projections. \
\
This package contains the MinGW Windows cross compiled graphene library.
Name:           mingw-graphene
Version:        1.10.8
Release:        1%{?dist}
Summary:        Thin layer of types for graphic libraries
License:        MIT
URL:            https://github.com/ebassi/graphene
Source0:        https://github.com/ebassi/graphene/releases/download/%{version}/graphene-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  meson
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-glib2
# /oreon:deps
%description %{desc}

%package -n mingw32-graphene
Summary:        MinGW Windows graphene library
%description -n mingw32-graphene
%{description}

%package -n mingw64-graphene
Summary:        MinGW Windows graphene library
%description -n mingw64-graphene %{desc}

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir graphene-%{version}
%oreon_prep
%build

%mingw_meson -Dintrospection=disabled
%mingw_ninja
%install
%mingw_ninja_install
rm -rf %{buildroot}%{mingw32_datadir}/installed-tests/
rm -rf %{buildroot}%{mingw64_datadir}/installed-tests/
rm -rf %{buildroot}%{mingw32_libexecdir}/installed-tests/
rm -rf %{buildroot}%{mingw64_libexecdir}/installed-tests/
%oreon_autofiles mingw32-graphene usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-graphene usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-graphene -f %{oreon_filedir}/mingw32-graphene.list
%files -n mingw64-graphene -f %{oreon_filedir}/mingw64-graphene.list

%changelog

%autochangelog
