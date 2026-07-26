%global source0_hash f887aa803724302151c698305704a0e3929d40553be82646d59c4d4cb0f4c697

Summary: Gamerzilla GObject Introspection Library
Name: gamerzillagobj
Version: 0.1.3
Release: %autorelease
License: zlib
URL: https://github.com/dulsi/gamerzillagobj
Source0: http://www.identicalsoftware.com/gamerzilla/%{name}-%{version}.tgz

BuildRequires: gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  make
BuildRequires: libgamerzilla-devel

%description
GamerzillaGObj is a gobject based introspection library to allow
shell-extensions to use Gamerzilla.

%package devel
Summary:        Development files for GamerzillaGObj

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and header files for GamerzillaGObj.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%make_build

%install
%make_install PREFIX=%{_prefix} LIB=%{_lib}

%files
%license LICENSE
%{_libdir}/libgamerzillagobj.so.0
%{_libdir}/libgamerzillagobj.so.0.0.0
%{_libdir}/girepository-1.0/Gamerzilla-0.1.typelib

%files devel
%{_libdir}/libgamerzillagobj.so
%{_datadir}/gir-1.0/Gamerzilla-0.1.gir

%changelog
%autochangelog
