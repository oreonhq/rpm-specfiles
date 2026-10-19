%global source0_hash b26c9016eb03bb4ee52cc00c642d56e00fc79ae7faac6bf4aa317d7451339ef7
    %bcond_without tests
Summary:        Tool for managing bootable, immutable filesystem trees
Name: ostree
Version: 2026.4
Release:        1%{?dist}
Source0:        https://github.com/ostreedev/%{name}/releases/download/v%{version}/libostree-%{version}.tar.xz
License: LGPL-2.0-or-later
URL: https://ostreedev.github.io/ostree/
%if %{with tests}
%endif
Requires: dracut
Requires: /usr/bin/gpgv2
Requires: systemd-units
Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: composefs
# oreon:deps
BuildRequires:  /usr/bin/g-ir-scanner
BuildRequires:  attr
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  dracut
BuildRequires:  git
BuildRequires:  gpgme-devel
BuildRequires:  gtk-doc
BuildRequires:  libattr-devel
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(composefs)
BuildRequires:  pkgconfig(e2p)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
libostree is a shared library designed primarily for
use by higher level tools to manage host systems (e.g. rpm-ostree),
as well as container tools like flatpak and the atomic CLI.

%package libs
Summary: C shared libraries %{name}
%description libs
The %{name}-libs provides shared libraries for %{name}.

%package devel
Summary: Development headers for %{name}
Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
The %{name}-devel package includes the header files for the %{name} library.

%ifnarch s390 s390x
%package grub2
Summary: GRUB2 integration for OSTree
%ifnarch aarch64 %{arm}
Requires: grub2
%else
Requires: grub2-efi
%endif
Requires: ostree
%description grub2
GRUB2 integration for OSTree
%endif

%if %{with tests}
%package tests
Summary: Tests for the %{name} package
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description tests
This package contains tests that can be used to verify
the functionality of the installed %{name} package.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libostree-%{version}
%oreon_prep
%build

env NOCONFIGURE=1 ./autogen.sh
%configure --disable-silent-rules \
           --enable-gtk-doc \
           --with-selinux \
           --with-curl \
           --with-openssl \
           --without-soup \
           --with-composefs \
           %{?with_tests:--with-soup3} \
           %{?!with_tests:--without-soup3} \
           %{?with_tests:--enable-installed-tests=exclusive} \
           --with-dracut=yesbutnoconf
%make_build
%install
%make_install INSTALL="install -p -c"
find %{buildroot} -name '*.la' -delete
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post ostree-remount.service
%preun

%systemd_preun ostree-remount.service
%files -f %{oreon_filedir}/main.list
%files -n ostree-libs -f %{oreon_filedir}/ostree-libs.list
%files -n ostree-devel -f %{oreon_filedir}/ostree-devel.list
%files -n ostree-grub2 -f %{oreon_filedir}/ostree-grub2.list
%files -n ostree-tests -f %{oreon_filedir}/ostree-tests.list

%changelog

%autochangelog
