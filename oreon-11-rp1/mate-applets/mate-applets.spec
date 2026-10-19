%global source0_hash a5967141527dc5b172d322a6003c23aeec253160f650bb36430a06ddaefa7e2e
%global branch 1.28
Name:          mate-applets
Version:       %{branch}.1
Release:        1%{?dist}
Summary:        MATE Desktop panel applets
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
%ifnarch s390 s390x sparc64
%endif
ExcludeArch: i386 i686
Provides:   mate-netspeed%{?_isa} = %{version}-%{release}
Provides:   mate-netspeed = %{version}-%{release}
Obsoletes:  mate-netspeed < %{version}-%{release}
# oreon:deps
BuildRequires:  dbus-glib-devel
BuildRequires:  gtksourceview4-devel
BuildRequires:  gucharmap-devel
BuildRequires:  kernel-tools-libs-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libgtop2-devel
BuildRequires:  libmateweather-devel
BuildRequires:  libnl3-devel
BuildRequires:  libnotify-devel
BuildRequires:  libwnck3-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-notification-daemon
BuildRequires:  mate-panel-devel
BuildRequires:  mate-settings-daemon-devel
BuildRequires:  polkit-devel
BuildRequires:  startup-notification-devel
BuildRequires:  upower-devel
# /oreon:deps
%description
MATE Desktop panel applets

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure   \
    --disable-schemas-compile                \
    --disable-static                         \
    --with-x                                 \
    --enable-polkit                          \
    --enable-ipv6                            \
    --enable-stickynotes                     \
    --libexecdir=%{_libexecdir}/mate-applets \
    --with-dbus-sys=%{_datadir}/dbus-1/system.d \
    --enable-in-process
sed -i /LDFLAGS/s/--as-needed/--no-as-needed/g stickynotes/Makefile
make %{?_smp_mflags} V=1
%install
%{make_install}
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
