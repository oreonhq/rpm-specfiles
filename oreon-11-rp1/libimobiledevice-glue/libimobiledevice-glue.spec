%global source0_hash 6489a3411b874ecd81c87815d863603f518b264a976319725e0ed59935546774
Name:           libimobiledevice-glue
Version:        1.3.2
Release:        1%{?dist}
Summary:        Library with common code among libimobiledevice projects
License:        LGPL-2.1-or-later
URL:            https://github.com/libimobiledevice/libimobiledevice-glue
Source0:        https://github.com/libimobiledevice/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libplist-devel
BuildRequires:  make
# /oreon:deps
%description
The libimobiledevice-glue library is library with common code used by libraries
and tools around the libimobiledevice project.

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

%configure --disable-static
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libimobiledevice-glue-devel -f %{oreon_filedir}/libimobiledevice-glue-devel.list

%changelog

* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-1
- Prepare for Oreon 11 (RP1)
