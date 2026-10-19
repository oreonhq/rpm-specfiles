%global source0_hash b18f733e7f52bbbf10170b09e2cd41ea324376bf4af9b103514602f2647046cd
%global         basever 0.8.18
Name:           libcompizconfig
Version:        0.8.18
Release:        1%{?dist}
Epoch:          1
Summary:        Configuration back end for compiz
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:            https://gitlab.com/compiz/%{name}
Source0:        https://gitlab.com/compiz/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Requires:       compiz >= %{basever}
Patch0:         libcompizconfig-0.8.18-version-fix.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  compiz-bcop
BuildRequires:  compiz-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libX11-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:  protobuf-devel
# /oreon:deps
%description
The Compiz Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity
through plugins and themes contributed by the community giving a
rich desktop experience.

This package contains the library for plugins to configure compiz 
settings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       compiz-devel >= %{version}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-v%{version}
%patch -P0 -p1 -b .version-fix

%build

./autogen.sh
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags} V=1
%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libcompizconfig-devel -f %{oreon_filedir}/libcompizconfig-devel.list

%changelog

%autochangelog
