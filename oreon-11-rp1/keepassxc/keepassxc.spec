%global source0_hash c9f5c4fe4b93d232795a9d8bfb58d129a492fcaa79c846eb637399164bcdb2d8

%undefine __cmake_in_source_build
# EPEL7 not possible because libgcrypt version is 1.5

Name:           keepassxc
Version:        2.7.12
Release:        1%{?dist}
Summary:        Cross-platform password manager
# Automatically converted from old format: Boost and BSD and CC0 and GPLv3 and LGPLv2 and LGPLv2+ and LGPLv3+ and Public Domain - review is highly recommended.
License:        BSL-1.0 AND LicenseRef-Callaway-BSD AND CC0-1.0 AND GPL-3.0-only AND LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-LGPLv2+ AND LGPL-3.0-or-later AND LicenseRef-Callaway-Public-Domain
URL:            https://keepassxc.org/
Source0:        https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/keepassxc-%{version}-src.tar.xz
Source1:        https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/keepassxc-%{version}-src.tar.xz.sig
Source2:        https://keepassxc.org/keepassxc_master_signing_key.asc
# Patch0: fixes GNOME quirks on Wayland sessions. Read
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/3BVLBS4B3XHJEXFVGD7RK2ZMXZG6JQZT/
# read also https://github.com/keepassxreboot/keepassxc/pull/3520/files
#
# Patch0 improved by pewpeww https://src.fedoraproject.org/rpms/keepassxc/pull-request/1
#
# 23 March 2022 Germano Massullo's update: Jan Grulich said that Qt patch https://code.qt.io/cgit/qt/qtbase.git/commit/?id=dda7dab8274991e4a61a97c352d4367f8f815bb9
# is included in qt5-qtbase in all Fedora versions since 32, even before it landed upstream, but it is not in RHEL qt5-qtbase package.
# So I think it is no longer needed in Fedora
# 
# Concerning upstream Qt6 version, the patch was reverted and kept for Qt 6.3, but concerning keepassxc it is not important since it uses Qt 5
#
# 29 April 2022 Germano Massullo's update: users in upstream bugreports
# https://github.com/keepassxreboot/keepassxc/issues/7959
# https://github.com/keepassxreboot/keepassxc/issues/5608
# are reporting regression. I am resuming xcb.patch to all branches
#
# 27 July 2022 Germano Massullo's update: new Qt release
# https://bodhi.fedoraproject.org/updates/FEDORA-2022-d1ac004bb1
# reintroduced xcb patch for GNOME Wayland mentioning in the description the
# problems keepassxc users experienced
#
# 15 April 2023 Germano Massullo's update: xcb.patch causes users no longer being
# able to move KeepassXC database entries between groups on Fedora 38 GNOME
# https://bugzilla.redhat.com/show_bug.cgi?id=2186217
# disabling the patch fixes the problem, therefore it has been disabled on
# Fedora >= 38
# Apply xcb.patch only for EPEL <= 9
%if (%{defined rhel} && 0%{?rhel} <= 9)
Patch0:         xcb.patch
%endif

%if (%{defined fedora} && 0%{?fedora} >= 44) || (%{defined rhel} && 0%{?rhel} >= 10)
BuildRequires:  botan3-devel
%else
BuildRequires:  botan2-devel
%endif
BuildRequires:  cmake >= 3.1
BuildRequires:  desktop-file-utils
%if %{defined rhel} && 0%{?rhel} < 9
BuildRequires:  gcc-toolset-12-gcc-c++
BuildRequires:  gcc-toolset-12-annobin-plugin-gcc
%else
BuildRequires:  gcc-c++
%endif
# required for check
BuildRequires:  glibc-langpack-en
BuildRequires:  libappstream-glib
BuildRequires:  libargon2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel >= 1.7
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libsodium-devel
BuildRequires:  libusb1-devel
BuildRequires:  libXi-devel
BuildRequires:  libXtst-devel
BuildRequires:  libyubikey-devel
# Concerning minizip dependency drama, this is the list of available minizip packages
# for all active branches
# == el8, el9 ==
# minizip
# minizip1.2
#
# == fedora >= 40 ==
# minizip-ng
# minizip-ng-compat
# Read https://fedoraproject.org/wiki/Changes/MinizipNGTransition 
%if 0%{?el8} || 0%{?el9}
BuildRequires: minizip1.2-devel
%else
BuildRequires: minizip-ng-compat-devel
%endif
BuildRequires:  pcsc-lite-devel
BuildRequires:  qrencode-devel
BuildRequires:  readline-devel
BuildRequires:  qt5-qtbase-devel >= 5.2
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel >= 5.2
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  zlib-devel
BuildRequires:  rubygem-asciidoctor
# for gpg verification
BuildRequires:  gnupg2

# enforces on the user system, Qt version to be the same one used to build KeepassXC
# This avoids "not a bug" bugreports like this one
# https://bugzilla.redhat.com/show_bug.cgi?id=2068981
# Moreover it is very important in case of mass rebuild of Qt+applications that
# are dependent from Qt, because it happened (see following bugreport) that users experienced
# that their system was not able to install a new Qt update due packaging bugs, but the system
# was able to update keepassxc (which was built upon new Qt release), resulting in a
# Qt - KeepassXC mismatch
# https://bugzilla.redhat.com/show_bug.cgi?id=2111413
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

# KeePassXC bundles the ykcore code due to lack of support from Yubico and
# stratification of version across various operating system distros. Additionally,
# KeePassXC has modified the API of ykcore to make it more functional when using
# non-YubiKey keys (ie, OnlyKey).
Provides: bundled(ykcore)

# GNOME-Shell does not allow clearing the clipboard when KeePassXC does not have focus.
# KeePassXC already works around this by calling wl-copy, which is part of wl-clipboard.
# See: https://github.com/keepassxreboot/keepassxc/issues/4498
Recommends: (wl-clipboard if gnome-shell)

# Unsupported CPU architectures on EPEL8
# filled https://bugzilla.redhat.com/show_bug.cgi?id=2144863
# to be compliant to "Architecture Build Failures" paragraph of Fedora Packaging Guidelines 
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_architecture_build_failures
%if %{defined rhel} && 0%{?rhel} == 8
ExcludeArch: s390x
%endif

%description
KeePassXC is a community fork of KeePassX
KeePassXC is an application for people with extremely high demands on secure
personal data management.
KeePassXC saves many different information e.g. user names, passwords, urls,
attachemts and comments in one single database. For a better management
user-defined titles and icons can be specified for each single entry.
Furthermore the entries are sorted in groups, which are customizable as well.
The integrated search function allows to search in a single group or the
complete database.
KeePassXC offers a little utility for secure password generation. The password
generator is very customizable, fast and easy to use. Especially someone who
generates passwords frequently will appreciate this feature.
The complete database is always encrypted either with AES (alias Rijndael) or
Twofish encryption algorithm using a 256 bit key. Therefore the saved
information can be considered as quite safe.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%setup -q
%autopatch -p1

# Older version of appstream-util can't parse some url types
%if (%{defined rhel} && 0%{?rhel} <= 9)
sed -i '/type="vcs-browser"/d' ./share/linux/org.keepassxc.KeePassXC.appdata.xml
sed -i '/type="contribute"/d' ./share/linux/org.keepassxc.KeePassXC.appdata.xml
%endif

# Older version of desktop-file-utils before 0.26 don't know about some fields
# Remove when desktop-file-utils 0.26 is available in EPEL8
%if (%{defined rhel} && 0%{?rhel} <= 9)
sed -i 's/Version=1.5/Version=1.0/' ./share/linux/org.keepassxc.KeePassXC.desktop.in
sed -i '/^SingleMainWindow=true/d' ./share/linux/org.keepassxc.KeePassXC.desktop.in
%endif

%build
%if %{defined rhel} && 0%{?rhel} == 8
%enable_devtoolset12
# disable -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1, as gcc-toolset-{10,11,12}-annobin
# do not provide gcc-annobin.so anymore, despite that they provide annobin.so. but
# redhat-rpm-config still passes -fplugin=gcc-annobin to the compiler.
%undefine _annotated_build
%endif
%cmake \
    %{?flatpak:-DKEEPASSXC_DIST_TYPE=Flatpak} \
    -DCMAKE_BUILD_TYPE=Release \
    -DKEEPASSXC_BUILD_TYPE=Release \
    -DWITH_XC_ALL=ON \
    -DWITH_XC_DOCS=ON \
    -DWITH_XC_UPDATECHECK=OFF
%cmake_build
 
%install
%cmake_install
%if %{defined flatpak}
install -m0755 utils/keepassxc-flatpak-wrapper.sh %{buildroot}%{_bindir}/keepassxc-wrapper
%endif
 
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    --delete-original \
    --add-mime-type application/x-keepassxc \
    %{buildroot}%{_datadir}/applications/org.%{name}.KeePassXC.desktop
 
%find_lang %{name} --with-qt

%check
# C language fails https://github.com/keepassxreboot/keepassxc/issues/11813
export LC_ALL=en_US.UTF-8
# 'testcli' fails with "Subprocess aborted" in Koji and local mock
%ctest --exclude-regex testcli
desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.KeePassXC.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.%{name}.KeePassXC.appdata.xml

%files -f %{name}.lang
%doc README.md
%license COPYING LICENSE*
%{_bindir}/keepassxc
%{_bindir}/keepassxc-cli
%{_bindir}/keepassxc-proxy
%if %{defined flatpak}
%{_bindir}/keepassxc-wrapper
%endif
%{_datadir}/keepassxc
%{_datadir}/keepassxc/wordlists
%{_datadir}/applications/org.%{name}.KeePassXC.desktop
%{_datadir}/metainfo/org.%{name}.KeePassXC.appdata.xml
%{_datadir}/mime/packages/*.xml
%{_datadir}/icons/hicolor/*/*/*keepassxc*
%{_libdir}/%{name}
%{_mandir}/man1/%{name}-cli.1*
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
