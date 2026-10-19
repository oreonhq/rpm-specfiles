%global source0_hash 792e0ea3c96ffe3ad65617a104b7dc50684932bc96d2adab501c952fd65c3e4a
Name:		libgtextutils
Version:	0.7
Release:        39%{?dist}
Summary:        Assaf Gordon text utilities
License:	AGPL-3.0-or-later
URL:		http://hannonlab.cshl.edu/fastx_toolkit/
Source0:        https://github.com/agordon/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:		libgtextutils-GCC6-iostream.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
Text utilities library used by the fastx_toolkit, from the Hannon Lab

%package       devel
Summary:       Development files for %{name}
Requires:      %{name} = %{version}-%{release}
Requires:      pkgconfig
%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p1

%build

%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libgtextutils-devel -f %{oreon_filedir}/libgtextutils-devel.list

%changelog

%autochangelog
