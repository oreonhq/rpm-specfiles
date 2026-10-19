%global source0_hash 4888ef54f9b404853712945218b3168696569db9167d7e01ec76e44b6c05c71c
%global _lto_cflags %nil
Name:           sleuthkit
Version:        4.15.0
Release:        1%{?dist}
Summary:        The Sleuth Kit (TSK)
License:        CPL-1.0 AND IPL-1.0 AND GPL-2.0-or-later
URL:            https://www.sleuthkit.org
Source0:        https://github.com/sleuthkit/sleuthkit/archive/sleuthkit-%{version}/sleuthkit-%{version}.tar.gz
%{?_with_java:
Requires:       java >= 1:1.6.0
Requires:       jpackage-utils
}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: file
Requires: mac-robber
# oreon:deps
BuildRequires:  afflib-devel
BuildRequires:  gcc-c++
BuildRequires:  libewf-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  sqlite-devel
# /oreon:deps
%description
The Sleuth Kit (TSK) is a collection of UNIX-based command line tools that
allow you to investigate a computer. The current focus of the tools is the
file and volume systems and TSK supports FAT, Ext2/3, NTFS, UFS,
and ISO 9660 file systems

%package        libs
Summary:        Library for %{name}
%description    libs
The %{name}-libs package contains library for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       sqlite-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{name}-%{version}
autoreconf -vif

%build

%configure --disable-static \
 %{!?_with_java:--disable-java}
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install INSTALL="install -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n sleuthkit-libs -f %{oreon_filedir}/sleuthkit-libs.list
%files -n sleuthkit-devel -f %{oreon_filedir}/sleuthkit-devel.list

%changelog

%autochangelog
