%global source0_hash 55a7517cd3572bd2565df0cf450944a04d5273b279ebb369a895391957f0f960
Name:           libspectre
Version:        0.2.12
Release:        1%{?dist}
Summary:        A library for rendering PostScript(TM) documents
License:        GPL-2.0-or-later
URL:            http://libspectre.freedesktop.org
Source0:        https://libspectre.freedesktop.org/releases/%{name}-%{version}.tar.gz
%if 0%{?fedora} > 27 || (0%{?oreon} >= 11)
%else
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libgs-devel
BuildRequires:  make
# /oreon:deps
%description
%{name} is a small library for rendering PostScript(TM) documents.
It provides a convenient easy to use API for handling and rendering
PostScript documents.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
  --disable-silent-rules \
  --disable-static
%make_build
%install
%make_install
rm -fv %{buildroot}%{_libdir}/libspectre.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libspectre-devel -f %{oreon_filedir}/libspectre-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.12-11
- Import
