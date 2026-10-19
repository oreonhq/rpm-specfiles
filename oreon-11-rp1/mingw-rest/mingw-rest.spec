%global source0_hash 9266a5c10ece383e193dfb7ffb07b509cc1f51521ab8dad76af96ed14212c2e3
%{?mingw_package_header}
Name:           mingw-rest
Version:        0.10.2
Release:        1%{?dist}
Summary:        A library for access to RESTful web services
License:        LicenseRef-Callaway-LGPLv2
URL:            https://wiki.gnome.org/Projects/Librest
Source0:        http://download.gnome.org/sources/rest/0.8/rest-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-json-glib
BuildRequires:  mingw32-libsoup3
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-json-glib
BuildRequires:  mingw64-libsoup3
BuildRequires:  mingw64-libxml2
BuildRequires:  ninja-build
# /oreon:deps
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
%oreon_autofiles mingw32-rest usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-rest-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-rest usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-rest-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-rest -f %{oreon_filedir}/mingw32-rest.list
%files -n mingw32-rest-static -f %{oreon_filedir}/mingw32-rest-static.list
%files -n mingw64-rest -f %{oreon_filedir}/mingw64-rest.list
%files -n mingw64-rest-static -f %{oreon_filedir}/mingw64-rest-static.list

%changelog

%autochangelog
