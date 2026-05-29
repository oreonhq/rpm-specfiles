%global source0_hash 10bd584d8f00d8091e814902b9f0a3e209f16e938f510fc23ba05f3fa469db5a

%global pkgname libisofs

Summary:        Library to create ISO 9660 disk images
Name:           libisofs
Version:        1.5.8
Release:        3%{?dist}
# libisofs/make_isohybrid_mbr.c is LGPL-2.0-or-later, rest is GPL-2.0-or-later
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://libburnia-project.org/
Source0:        https://files.libburnia-project.org/releases/libisofs-1.5.8.pl02.tar.gz
Source1:        https://files.libburnia-project.org/releases/libisofs-1.5.8.pl02.tar.gz.sig
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/44BC9FD0D688EB007C4DD029E9CBDFC0ABC0A854
Patch0:         libisofs-0.6.16-multilib.patch
Patch1:         libisofs-1.5.4-rpath.patch
BuildRequires:  gnupg2
BuildRequires:  gcc, make, libacl-devel, zlib-devel
%if 0%{?rhel} && "%{name}" != "%{pkgname}" || 0%{?oreon}
BuildRequires:  autoconf, automake, libtool
%endif

%description
Libisofs is a library to create an ISO-9660 filesystem and supports
extensions like RockRidge or Joliet. It is also a full featured
ISO-9660 editor, allowing you to modify an ISO image or multisession
disc, including file addition or removal, change of file names and
attributes etc. It supports the extension AAIP which allows to store
ACLs and xattr in ISO-9660 filesystems as well. As it is linked with
zlib, it supports zisofs compression, too.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if 0%{!?_without_doc:1}
%package doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
BuildRequires:  doxygen, graphviz

%description doc
Libisofs is a library to create an ISO-9660 filesystem and supports
extensions like RockRidge or Joliet. This package contains the API
documentation for developing applications that use %{name}.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{pkgname}-%{version} -p1

# Rename from libisofs to libisofs1 for EPEL
%if 0%{?rhel} && "%{name}" != "%{pkgname}" || 0%{?oreon}
sed -e 's@libisofs_libisofs@libisofs_libisofs1@g' \
    -e 's@libisofs/libisofs.la@libisofs/libisofs1.la@g' \
    -e 's@(includedir)/libisofs@(includedir)/libisofs1@g' \
    -e 's@libisofs-1.pc@libisofs1-1.pc@g' -i Makefile.am
sed -e 's@libisofs-1.pc@libisofs1-1.pc@g' -i configure.ac
sed -e 's@isofs@isofs1@g' libisofs-1.pc.in > libisofs1-1.pc.in

libtoolize --force
autoreconf --force --install
%endif

%build
%configure --disable-static
%make_build
%{!?_without_doc:doxygen doc/doxygen.conf}

%install
%make_install

# Don't install any libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la

# Clean up for later usage in documentation
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS COPYRIGHT README
%{_libdir}/%{name}*.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}*.pc

%if 0%{!?_without_doc:1}
%files doc
%doc doc/html/
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.8-3
- Import
