%global source0_hash 6cd92e2597c35801e4ad9e2b62713db42d8884ef0d9c75d522bca3fbd78b1821
%global snapper_svcs snapper-boot.service snapper-boot.timer snapper-cleanup.service snapper-cleanup.timer snapper-timeline.service snapper-timeline.timer snapperd.service
Name:           snapper
Version:        0.13.2
Release:        1%{?dist}
Summary:        Tool for filesystem snapshot management
License:        GPL-2.0-only
URL:            https://snapper.io
Source0:        https://github.com/openSUSE/snapper/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-remove-ext4-info-xml.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       diffutils
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  btrfs-progs-devel
BuildRequires:  dbus-devel
BuildRequires:  docbook-style-xsl
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glibc-all-langpacks
BuildRequires:  json-c-devel
BuildRequires:  libacl-devel
BuildRequires:  libmount-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This package contains snapper, a tool for filesystem snapshot management.

%package libs
Summary:        Library for filesystem snapshot management
Requires:       util-linux%{?_isa}
Requires:       btrfs-progs%{?_isa}
%description libs
This package contains the snapper shared library
for filesystem snapshot management.

%package devel
Summary:        Header files and development libraries for %{name}-libs
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel%{?_isa}
Requires:       libacl-devel%{?_isa}
Requires:       boost-devel%{?_isa}
Requires:       btrfs-progs-devel
Requires:       libxml2-devel%{?_isa}
Requires:       libmount-devel%{?_isa}
%description devel
This package contains header files and documentation for developing with
snapper.

%package tests
Summary:        Integration tests for snapper
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description tests
%{summary}.

%package backup
Summary:        A backup program for snapper
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description backup
A backup program for snapshots created by snapper.

%package -n pam_snapper
Summary:        PAM module for calling snapper
BuildRequires:  pam-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n pam_snapper
A PAM module for calling snapper during user login and logout.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
find -type f -exec sed -i -e "s|/usr/lib/snapper|%{_libexecdir}/%{name}|g" {} ';'

%conf
autoreconf -vfi
%configure \
  --disable-bcachefs \
  --disable-ext4 \
  --disable-zypp \
  --enable-selinux \
  %{nil}

%build

%make_build
%install
%make_install
install -Dpm0644 data/sysconfig.snapper %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%find_lang %{name}
find %{buildroot} -name '*.la' -print -delete
rm -rf %{buildroot}%{_sysconfdir}/cron.hourly
rm -rf %{buildroot}%{_sysconfdir}/cron.daily
rm -rf %{buildroot}%{_docdir}/%{name}/COPYING
%oreon_autofiles pam_snapper usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make %{?_smp_mflags} check
%post

%systemd_post %{snapper_svcs}
%preun

%systemd_preun %{snapper_svcs}
%postun

%systemd_postun_with_restart %{snapper_svcs}
%pre libs

for i in config-templates/default filters/base.txt filters/lvm.txt filters/x11.txt ; do
    test -f /etc/snapper/${i}.rpmsave && mv -v /etc/snapper/${i}.rpmsave /etc/snapper/${i}.rpmsave.old ||:
done
%posttrans libs

for i in config-templates/default filters/base.txt filters/lvm.txt filters/x11.txt ; do
    test -f /etc/snapper/${i}.rpmsave && mv -v /etc/snapper/${i}.rpmsave /etc/snapper/${i} ||:
done
%files -f %{oreon_filedir}/main.list
%files -n snapper-libs -f %{oreon_filedir}/snapper-libs.list
%files -n snapper-devel -f %{oreon_filedir}/snapper-devel.list
%files -n snapper-tests -f %{oreon_filedir}/snapper-tests.list
%files -n snapper-backup -f %{oreon_filedir}/snapper-backup.list
%files -n pam_snapper -f %{oreon_filedir}/pam_snapper.list

%changelog

%autochangelog
