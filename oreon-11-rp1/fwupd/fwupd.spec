%global source0_hash 8724305a52621ab6586de3290f6a78edb8393a4aa4bcb6c63f9228ae5e00acf8
%global glib2_version 2.68.0
%global libxmlb_version 0.3.24
%global libusb_version 1.0.9
%global libcurl_version 7.62.0
%global libjcat_version 0.1.0
%global systemd_version 249
%global __requires_exclude ^%{python3}$
%ifnarch ppc64le
%global enable_tests 1
%endif
%global enable_dummy 1
%ifarch x86_64 aarch64 riscv64
%global have_uefi 1
%endif
%ifarch i686 x86_64 armv7hl aarch64 ppc64le riscv64
%global have_flashrom 1
%endif
%ifarch i686 x86_64
%global have_msr 1
%endif
%if 0%{?fedora} >= 30 || (0%{?oreon} >= 11)
%global have_modem_manager 1
%endif
%if 0%{?fedora} || (0%{?oreon} >= 11)
%global have_passim 1
%endif
Summary:        Firmware update daemon
Name:      fwupd
Version:   2.1.8
Release:        1%{?dist}
License:   LGPL-2.1-or-later
URL:       https://github.com/fwupd/fwupd
Source0:        https://github.com/fwupd/fwupd/releases/download/%{version}/%{name}-%{version}.tar.xz
%if 0%{?have_passim}
%endif
%ifarch %{valgrind_arches}
%endif
%if 0%{?have_flashrom}
%endif
%if 0%{?have_modem_manager}
%endif
%if 0%{?have_uefi}
%endif
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: libxmlb%{?_isa} >= %{libxmlb_version}
Requires: libusb1%{?_isa} >= %{libusb_version}
Requires: shared-mime-info
Obsoletes: dbxtool < 9
Provides: dbxtool
Recommends: udisks2
Recommends: bluez
Recommends: jq
%if 0%{?have_passim}
Recommends: passim
%endif
%if 0%{?have_modem_manager}
Recommends: %{name}-plugin-modem-manager
%endif
%if 0%{?have_flashrom}
Recommends: %{name}-plugin-flashrom
%endif
%if 0%{?have_uefi}
Recommends: %{name}-efi
Recommends: %{name}-plugin-uefi-capsule-data
%endif
# oreon:deps
BuildRequires:  ModemManager-glib-devel
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  gnutls-devel
BuildRequires:  gnutls-utils
BuildRequires:  gobject-introspection-devel
BuildRequires:  hwdata
BuildRequires:  libblkid-devel
BuildRequires:  libcurl-devel
BuildRequires:  libdrm-devel
BuildRequires:  libjcat-devel
BuildRequires:  libmbim-devel
BuildRequires:  libmnl-devel
BuildRequires:  libqmi-devel
BuildRequires:  libusb1-devel
BuildRequires:  libxmlb-devel
BuildRequires:  meson
BuildRequires:  passim-devel
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  polkit
BuildRequires:  polkit-devel
BuildRequires:  python3-jinja2
BuildRequires:  python3-packaging
BuildRequires:  readline-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  vala
# /oreon:deps
%description
fwupd is a daemon to allow session software to update device firmware.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: libebitdo-devel < 0.7.5-3
Obsoletes: libdfu-devel < 1.0.0
%description devel
Files for development with %{name}.

%package tests
Summary: Data files for installed tests
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tests
Data files for installed tests.

%if 0%{?have_modem_manager}
%package plugin-modem-manager
Summary: fwupd plugin using ModemManger
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugin-modem-manager
This provides the optional package which is only required on hardware that
might have mobile broadband hardware. It is probably not required on servers.
%endif

%if 0%{?have_flashrom}
%package plugin-flashrom
Summary: fwupd plugin using flashrom
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugin-flashrom
This provides the optional package which is only required on hardware that
can be flashed using flashrom. It is probably not required on servers.
%endif

%if 0%{?have_uefi}
%package plugin-uefi-capsule-data
Summary: Localized data for the UEFI UX capsule
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugin-uefi-capsule-data
This provides the pregenerated BMP artwork for the UX capsule, which allows the
"Installing firmware update…" localized text to be shown during a UEFI firmware
update operation. This subpackage is probably not required on embedded hardware
or server machines.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
    -Dumockdev_tests=disabled \
    -Ddocs=enabled \
%if 0%{?enable_tests}
    -Dtests=true \
%else
    -Dtests=false \
%endif
%if 0%{?have_flashrom}
    -Dplugin_flashrom=enabled \
%else
    -Dplugin_flashrom=disabled \
%endif
%if 0%{?have_modem_manager}
    -Dplugin_modem_manager=enabled \
%else
    -Dplugin_modem_manager=disabled \
%endif
%if 0%{?have_passim}
    -Dpassim=enabled \
%else
    -Dpassim=disabled \
%endif
%ifarch i686 x86_64
    -Dhsi=enabled \
%else
    -Dhsi=disabled \
%endif
    -Dman=true \
    -Dsystemd_unit_user="" \
    -Dbluez=enabled \
    -Dsupported_build=enabled
%meson_build
%if 0%{?enable_tests}
%check

%meson_test
%endif
%install
%meson_install
mkdir -p --mode=0700 $RPM_BUILD_ROOT%{_localstatedir}/lib/fwupd
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/fwupd
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post fwupd.service fwupd-refresh.timer
%preun

%systemd_preun fwupd.service fwupd-refresh.timer
%postun

%systemd_postun_with_restart fwupd.service fwupd-refresh.timer
%triggerun -- fedora-release-common < 39-0.28

systemctl --no-reload preset fwupd-refresh.timer &>/dev/null || :
%files -f %{oreon_filedir}/main.list
%files -n fwupd-devel -f %{oreon_filedir}/fwupd-devel.list
%files -n fwupd-tests -f %{oreon_filedir}/fwupd-tests.list
%files -n fwupd-plugin-modem-manager -f %{oreon_filedir}/fwupd-plugin-modem-manager.list

%changelog

%autochangelog
