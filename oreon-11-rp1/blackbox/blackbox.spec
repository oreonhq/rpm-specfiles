%global source0_hash e4f814fb02f6a977e9aab1c60192087597b79b0a56cc4a14e8a962b7d45d82d1
Name:           blackbox
Version:        0.77
Release:        1%{?dist}
Summary:        Very small and fast Window Manager
License:        MIT
URL:            https://github.com/bbidulock/blackboxwm
Source0:        https://github.com/bbidulock/blackboxwm/releases/download/%{version}/%{name}-%{version}.tar.lz
Source1:        blackbox.desktop
Source2:        blackbox.session
Patch0:         d3481ee7b7d104ef53ead4d35b9a9254c64bb87a.patch
Patch1:         d45570b2317ff8f20642fbda5aa07e8f43b254b0.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXt-devel
BuildRequires:  libtool
BuildRequires:  lzip
BuildRequires:  make
# /oreon:deps
%description
Blackbox is a window manager for the X Window environment, which is
almost completely compliant with ICCCM specified operation policies.
It features nice and fast interface with multiple workspaces and
simple menus. Fast built-in graphics code that can render solids,
gradients and bevels is used to draw window decorations. Remaining
small in size, blackbox preserves memory and CPU.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libXft-devel%{?_isa}
%description    devel
This package contains the Blackbox Toolbox files, headers and static library
of the utility class library for writing small applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# %%{__global_ldflags} wrongly passed to pkgconfig file
sed -i 's|@LDFLAGS@||g' lib/libbt.pc.in

%build

sh autogen.sh
autoreconf -fiv
%configure \
    --enable-shared \
    --disable-static
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -delete -print
install -pDm0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/xsessions/blackbox.desktop
install -pDm0755 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/X11/gdm/Sessions/Blackbox
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles blackbox-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n blackbox-devel -f %{oreon_filedir}/blackbox-devel.list

%changelog

%autochangelog
