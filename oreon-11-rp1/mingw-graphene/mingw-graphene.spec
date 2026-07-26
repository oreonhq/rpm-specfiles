%global source0_hash a37bb0e78a419dcbeaa9c7027bcff52f5ec2367c25ec859da31dfde2928f279a

%{?mingw_package_header}

%global desc \
Graphene provides a small set of mathematical types needed to implement graphic \
libraries that deal with 2D and 3D transformations and projections. \
\
This package contains the MinGW Windows cross compiled graphene library.

Name:           mingw-graphene
Version:        1.10.8
Release:        9%{?dist}
Summary:        Thin layer of types for graphic libraries

License:        MIT
URL:            https://github.com/ebassi/graphene
Source0:        %{url}/releases/download/%{version}/graphene-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  meson >= 0.50.1

BuildRequires:  mingw32-filesystem >= 107
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem >= 107
BuildRequires:  mingw64-gcc-c++

BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2

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

%autosetup -p1 -n graphene-%{version}

%build
%mingw_meson -Dintrospection=disabled
%mingw_ninja

%install
%mingw_ninja_install
rm -rf %{buildroot}%{mingw32_datadir}/installed-tests/
rm -rf %{buildroot}%{mingw64_datadir}/installed-tests/
rm -rf %{buildroot}%{mingw32_libexecdir}/installed-tests/
rm -rf %{buildroot}%{mingw64_libexecdir}/installed-tests/

%files -n mingw32-graphene
%license LICENSE.txt
%doc README.md
%{mingw32_libdir}/libgraphene-1.0.dll.a
%{mingw32_includedir}/graphene-1.0/
%dir %{mingw32_libdir}/graphene-1.0
%{mingw32_libdir}/graphene-1.0/include/
%{mingw32_bindir}/libgraphene-1.0-0.dll
%{mingw32_libdir}/pkgconfig/graphene-1.0.pc
%{mingw32_libdir}/pkgconfig/graphene-gobject-1.0.pc

%files -n mingw64-graphene
%license LICENSE.txt
%doc README.md
%{mingw64_libdir}/libgraphene-1.0.dll.a
%{mingw64_includedir}/graphene-1.0/
%dir %{mingw64_libdir}/graphene-1.0
%{mingw64_libdir}/graphene-1.0/include/
%{mingw64_bindir}/libgraphene-1.0-0.dll
%{mingw64_libdir}/pkgconfig/graphene-1.0.pc
%{mingw64_libdir}/pkgconfig/graphene-gobject-1.0.pc

%changelog
%autochangelog
