%global source0_hash b33b5dbcda10317ef67d628353d83246984ce6fcac102d4dc2aed121eba52e6f

%global optflags %(echo %{optflags} -fno-strict-aliasing)

%global _vpath_srcdir sdk/%{name}/projects/meson/

Name:           angelscript
Version:        2.38.0
Release:        4%{?dist}
Summary:        Flexible cross-platform scripting library

License:        zlib
URL:            http://www.angelcode.com/angelscript/
Source0:        %{url}/sdk/files/%{name}_%{version}.zip

BuildRequires:  meson
BuildRequires:  gcc-c++

%description
The AngelScript library is a software library for easy integration of
external scripting to applications, with built-in compiler and virtual
machine. The scripting language is easily extendable to incorporate
application specific data types and functions. It is designed with C++
in mind, as such it shares many features with C++, for example syntax
and data types.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%build
%meson
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%doc sdk/docs/articles/*.html
%{_libdir}/lib%{name}.so.23800

%files devel
%doc sdk/docs/manual/*
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h

%changelog
%autochangelog
