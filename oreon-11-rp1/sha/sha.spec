%global source0_hash 786159140fbb6647a8fbb5d909c721ff58e27c705333457566985777e3d6d730
Name:		sha
Version:	1.1
Release:        1%{?dist}
Summary:        File hashing utility
License:	LicenseRef-Callaway-BSD
URL:		http://hg.saddi.com/sha-asaddi
Source0:        http://www.saddi.com/software/%{name}/dist/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
file hashing utility that uses the
SHA-1, SHA-256, SHA-384, & SHA-512 hash algorithms.
It can be used for file integrity checking, 
remote file comparisons, etc. 
The portable algorithm implementations 
can be useful in other projects too

%package devel
Summary:	Development files for sha
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the libraries needed to develop applications
that use sha

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure \
	--disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install
rm -f %{buildroot}/%{_libdir}/*.la
mkdir -p %{buildroot}/%{_includedir}/sha
install -pm 644 *.h %{buildroot}/%{_includedir}/sha
%ldconfig_scriptlets
%ldconfig_scriptlets -n sha-devel
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n sha-devel -f %{oreon_filedir}/sha-devel.list

%changelog

%autochangelog
