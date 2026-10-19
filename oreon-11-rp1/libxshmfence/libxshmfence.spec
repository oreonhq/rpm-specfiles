%global source0_hash d4a4df096aba96fea02c029ee3a44e11a47eb7f7213c1a729be83e85ec3fde10
Name:           libxshmfence
Version:        1.3.3
Release:        1%{?dist}
Summary:        X11 shared memory fences
License:        HPND-sell-variant
URL:            https://www.x.org/
Source0:        https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xproto)
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
Shared memory fences for X11, as used in DRI3.

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

autoreconf -v -i -f
%configure --disable-static
make %{?_smp_mflags}
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libxshmfence-devel -f %{oreon_filedir}/libxshmfence-devel.list

%changelog

%autochangelog
