%global source0_hash 90f8d2fa8b5567c6899830ddef2c03f3c27960b11aca222fa17aa7ac613c2890

Name:           duktape
Version:        2.7.0
Release:        %autorelease
Summary:        Embeddable Javascript engine

License:        MIT
Url:            http://duktape.org/
Source0:        http://duktape.org/duktape-2.7.0.tar.xz
Patch0:         duktape-2.7.0-link-against-libm.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  make

%description
Duktape is an embeddable Javascript engine, with a focus on portability and
compact footprint.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
Embeddable Javascript engine.

This package contains header files and libraries needed to develop
application that use %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%make_build -f Makefile.sharedlibrary INSTALL_PREFIX=%{_prefix} LIBDIR=/%{_lib}

%install
%make_install -f Makefile.sharedlibrary INSTALL_PREFIX=%{_prefix} LIBDIR=/%{_lib}

%files
%license LICENSE.txt
%doc AUTHORS.rst
%{_libdir}/libduktape.so.*
%{_libdir}/libduktaped.so.*

%files devel
%doc examples/ README.rst
%{_includedir}/duk_config.h
%{_includedir}/duktape.h
%{_libdir}/libduktape.so
%{_libdir}/libduktaped.so
%{_libdir}/pkgconfig/duktape.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.7.0-1
- Import
