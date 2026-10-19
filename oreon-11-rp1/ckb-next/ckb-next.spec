%global source0_hash 1e4a15c2b3c5119164fe34560d0418e41679c4227d1a804113285e4d9109598b
Name:           ckb-next
Version:        0.6.2
Release:        5%{?dist}
Summary:        Unofficial driver for Corsair RGB keyboards
License:        GPL-2.0-only
URL:            https://github.com/ckb-next/ckb-next
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        ckb-next.appdata.xml
Source2:        ckb-next.1
Source3:        99-ckb-next.preset
Patch1: 0001-unbundle-kissfft.patch
%{?systemd_requires}
Requires:       qt6-qtbase
Obsoletes:      ckb < 0.2.8-0
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(QuaZip-Qt6)
BuildRequires:  cmake(kissfft)
BuildRequires:  cmake(zlib)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappindicator-devel
BuildRequires:  libappstream-glib
BuildRequires:  libgudev-devel
BuildRequires:  libxcb-devel
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  systemd-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-wm-devel
# /oreon:deps
%description
ckb-next is an open-source driver for Corsair keyboards and mice. It aims to
bring the features of their proprietary CUE software to the Linux operating
system. This project is currently a work in progress, but it already
supports much of the same functionality, including full RGB animations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove the bundled libraries
rm -rf src/libs/kissfft

# Fedora uses /usr/libexec for daemons
sed -e '/^ExecStart/cExecStart=%{_libexecdir}/ckb-next-daemon' -i linux/systemd/ckb-next-daemon.service.in

# Fedora has merged /lib into /usr/lib
sed -e 's|"/lib/udev/rules.d"|"%{_udevrulesdir}"|g' -i CMakeLists.txt

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DCMAKE_INSTALL_LIBEXECDIR=libexec \
  -DDISABLE_UPDATER=1 \
  -DFORCE_INIT_SYSTEM=systemd \
  -DSAFE_INSTALL=OFF \
  -DSAFE_UNINSTALL=OFF \
  -DPREFER_QT6=ON \
%cmake_build
%install
%cmake_install
mv %{buildroot}%{_bindir}/ckb-next-daemon %{buildroot}%{_libexecdir}/ckb-next-daemon
install -Dp -m 0644 %{SOURCE3}  %{buildroot}%{_presetdir}/99-ckb-next.preset
install -Dp -m 0644 %{SOURCE1}  %{buildroot}%{_datadir}/metainfo/ckb-next.appdata.xml
install -Dp -m 0644 %{SOURCE2}  %{buildroot}%{_mandir}/man1/ckb-next.1
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/ckb-next.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ckb-next.appdata.xml
%post

%systemd_post ckb-next-daemon.service
if [ $1 -eq 1 ]; then
    systemctl start ckb-next-daemon.service >/dev/null 2>&1 || :
fi
udevadm control --reload-rules 2>&1 > /dev/null || :
%preun

%systemd_preun ckb-next-daemon.service
%postun

%systemd_postun_with_restart ckb-next-daemon.service
udevadm control --reload-rules 2>&1 > /dev/null || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
