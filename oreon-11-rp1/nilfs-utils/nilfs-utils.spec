%global source1_hash 232e08e95ca20a8169f4b941a31a98ea2c076429b406f8146bad60b00c828006
%global source0_hash 8602897ff0d2c49be9bc76311f0b102088e58b6de4f749009403de06ff2c34cd
Name:		nilfs-utils
Version:	2.2.11
Release:        1%{?dist}
Summary:        Utilities for managing NILFS v2 filesystems
License:	GPL-2.0-or-later
URL:		http://nilfs.sourceforge.net
Source0:        http://nilfs.sourceforge.net/download/%{name}-%{version}.tar.bz2
Source1:	http://nilfs.sourceforge.net/download/%{name}-%{version}.tar.bz2.asc
Source2:	8B055AE86DEFF458.asc
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libmount-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
# /oreon:deps
%description
Userspace utilities for creating and mounting NILFS v2 filesystems.

%package devel
Summary:	NILFS2 filesystem-specific headers
Requires:	nilfs-utils = %{version}-%{release}
%description devel
nilfs-utils-devel contains the header files needed to develop NILFS
filesystem-specific programs.

You should install nilfs-utils-devel if you want to develop NILFS
filesystem-specific programs. If you install nilfs-utils-devel, you'll
also want to install nilfs-utils.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build

%configure LDCONFIG=/bin/true --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT sbindir=%_sbindir root_sbindir=%_sbindir
rm -f $RPM_BUILD_ROOT/%{_libdir}/libnilfs*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n nilfs-utils-devel -f %{oreon_filedir}/nilfs-utils-devel.list

%changelog

%autochangelog
