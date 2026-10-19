%global source0_hash 2dca25c0e0c837ddf00b52011b3f82cac1e4ddd3ad018227806b0c2288864acc
Name:           libass
Version:        0.17.5
Release:        1%{?dist}
Summary:        Portable library for SSA/ASS subtitles rendering
License:        ISC
URL:            https://github.com/libass
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
%ifnarch %{ix86}
%endif
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libunibreak)
# /oreon:deps
%description
Libass is a portable library for SSA/ASS subtitles rendering.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%ifarch %{ix86}
LDFLAGS="$LDFLAGS -Wl,-z,notext"
%endif
%configure --disable-static
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libass-devel -f %{oreon_filedir}/libass-devel.list

%changelog

%autochangelog
