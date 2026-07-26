%global source0_hash 9266a5c10ece383e193dfb7ffb07b509cc1f51521ab8dad76af96ed14212c2e3

%{?mingw_package_header}

Name:           mingw-rest
Version:        0.9.1
Release:        1%{?dist}
Summary:        A library for access to RESTful web services

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://wiki.gnome.org/Projects/Librest
Source0:        http://download.gnome.org/sources/rest/0.8/rest-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  mingw32-filesystem >= 98
BuildRequires:  mingw64-filesystem >= 98
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libsoup3
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libsoup3
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw32-json-glib
BuildRequires:  mingw64-json-glib

%description
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent
remote objects, which methods can then be called on. The majority of services
don't actually adhere to this strict definition. Instead, their RESTful end
point usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of API that
this library is attempting to support.

%package -n     mingw32-rest
Requires:       pkgconfig
Summary:        A library for access to RESTful web services

%description -n mingw32-rest
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent
remote objects, which methods can then be called on. The majority of services
don't actually adhere to this strict definition. Instead, their RESTful end
point usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of API that
this library is attempting to support.

%package -n     mingw32-rest-static
Requires:       pkgconfig
Requires:       mingw32-rest = %{version}-%{release}
Summary:        A library for access to RESTful web services

%description -n mingw32-rest-static
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent
remote objects, which methods can then be called on. The majority of services
don't actually adhere to this strict definition. Instead, their RESTful end
point usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of API that
this library is attempting to support.

%package -n     mingw64-rest
Requires:       pkgconfig
Summary:        A library for access to RESTful web services

%description -n mingw64-rest
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent
remote objects, which methods can then be called on. The majority of services
don't actually adhere to this strict definition. Instead, their RESTful end
point usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of API that
this library is attempting to support.

%package -n     mingw64-rest-static
Requires:       pkgconfig
Requires:       mingw64-rest = %{version}-%{release}
Summary:        A library for access to RESTful web services

%description -n mingw64-rest-static
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent
remote objects, which methods can then be called on. The majority of services
don't actually adhere to this strict definition. Instead, their RESTful end
point usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of API that
this library is attempting to support.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n rest-%{version}

%global meson_flags %{shrink: \
    -Dgtk_doc=false \
    -Dintrospection=false \
    -Dexamples=false \
}

%build
export MINGW_BUILDDIR_SUFFIX=static
%mingw_meson %{meson_flags} --default-library=static
%mingw_ninja
export MINGW_BUILDDIR_SUFFIX=shared
%mingw_meson %{meson_flags} --default-library=shared
%mingw_ninja

%install
export MINGW_BUILDDIR_SUFFIX=static
%mingw_ninja_install
export MINGW_BUILDDIR_SUFFIX=shared
%mingw_ninja_install

%files -n mingw32-rest
%license COPYING
%doc AUTHORS README.md
%{mingw32_bindir}/librest-1.0-0.dll
%{mingw32_libdir}/librest-1.0.dll.a
%{mingw32_bindir}/librest-extras-1.0-0.dll
%{mingw32_libdir}/librest-extras-1.0.dll.a
%{mingw32_libdir}/pkgconfig/rest*
%{mingw32_includedir}/rest-1.0

%files -n mingw32-rest-static
%{mingw32_libdir}/librest-1.0.a
%{mingw32_libdir}/librest-extras-1.0.a

%files -n mingw64-rest
%license COPYING
%doc AUTHORS README.md
%{mingw64_bindir}/librest-1.0-0.dll
%{mingw64_libdir}/librest-1.0.dll.a
%{mingw64_bindir}/librest-extras-1.0-0.dll
%{mingw64_libdir}/librest-extras-1.0.dll.a
%{mingw64_libdir}/pkgconfig/rest*
%{mingw64_includedir}/rest-1.0

%files -n mingw64-rest-static
%{mingw64_libdir}/librest-1.0.a
%{mingw64_libdir}/librest-extras-1.0.a

%changelog
%autochangelog
