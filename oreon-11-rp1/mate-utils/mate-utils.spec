%global source0_hash 58449d7a0d1d900ff03b78ca9f7e98c21e97f47fc26bee7ff1c61834f22f88d3
%global branch 1.28
Name:          mate-utils
Version:       %{branch}.0
Release:        1%{?dist}
Summary:        MATE utility programs
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Patch1:        mate-utils_0001-mate-screenshot-Toggle-shutter-sound.patch
Patch2:        mate-utils_0002-mate-screenshot-Replace-fork-save-with-sync-save.patch  
Requires: mate-dictionary = %{version}-%{release}
Requires: mate-screenshot = %{version}-%{release}
Requires: mate-search-tool = %{version}-%{release}
Requires: mate-system-log = %{version}-%{release}
Requires: mate-disk-usage-analyzer = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  e2fsprogs-devel
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  hardlink
BuildRequires:  libX11-devel
BuildRequires:  libXmu-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libgtop2-devel
BuildRequires:  libudisks2-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-panel-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  popt-devel
BuildRequires:  usermode
BuildRequires:  yelp-tools
# /oreon:deps
%description
The mate-utils package contains a set of small "desk accessory" utility
applications for MATE, such as a dictionary, a disk usage analyzer,
a screen-shot tool and others.

%package common
Summary: Common files for %{name}
BuildArch: noarch
%description common
%{summary}.

%package devel
Summary: Development files for mate-utils
Requires:  mate-dictionary%{?_isa} = %{version}-%{release}
%description devel
The mate-utils-devel package contains header files and other resources
needed to develop programs using the libraries contained in mate-utils.

%package -n mate-system-log
Summary: A log file viewer for the MATE desktop
Requires: %{name}-common = %{version}-%{release}
Requires: usermode
Requires: mate-desktop-libs
%description -n mate-system-log
An application that lets you view various system log files.

%package -n mate-screenshot
Summary: A utility to take a screen-shot of the desktop
Requires: %{name}-common = %{version}-%{release}
%description -n mate-screenshot
An application that let you take a screen-shot of your desktop.

%package -n mate-dictionary
Summary: A dictionary for MATE Desktop
Requires: %{name}-common = %{version}-%{release}
%description -n mate-dictionary
The mate-dictionary package contains a dictionary application for MATE Desktop.

%package -n mate-search-tool
Summary: A file searching tool for MATE Desktop
Requires: %{name}-common = %{version}-%{release}
Requires: mate-desktop-libs
%description -n mate-search-tool
An application to search for files on your computer.

%package -n mate-disk-image-mounter
Summary: A disk image mounter tool for MATE Desktop
Requires: %{name}-common = %{version}-%{release}
%description -n mate-disk-image-mounter
An application to mount disk images.

%package -n mate-disk-usage-analyzer
Summary: A disk usage analyzing tool for MATE Desktop
Requires: %{name}-common = %{version}-%{release}
%description -n mate-disk-usage-analyzer
An application to help analyze disk usage.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

# disable pt language for help in search tool
sed -i s/"IGNORE_HELP_LINGUAS ="/"IGNORE_HELP_LINGUAS = pt"/g gsearchtool/help/Makefile.am
# pt translation fix
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
    --disable-static            \
    --disable-schemas-compile   \
    --enable-gdict-applet       \
    --enable-in-process         \
    --enable-wayland            \
    --enable-gtk-doc-html       \
    --enable-ipv6=yes           \
    --enable-maintainer-flags=no  \
    --with-x
make %{?_smp_mflags} V=1
%install
%{make_install}
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
cat <<EOF >%{buildroot}%{_sysconfdir}/pam.d/mate-system-log
auth      include      config-util
account      include      config-util
session      include      config-util
EOF
mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps
cat <<EOF >%{buildroot}%{_sysconfdir}/security/console.apps/mate-system-log
USER=root
PROGRAM=%{_libexecdir}/mate-system-log
SESSION=true
FALLBACK=true
EOF
mkdir -p  %{buildroot}%{_libexecdir}
mv %{buildroot}%{_bindir}/mate-system-log %{buildroot}%{_libexecdir}
ln -s %{_bindir}/consolehelper %{buildroot}%{_bindir}/mate-system-log
rm -fv %{buildroot}%{_libdir}/*.la
rm -fv %{buildroot}%{_datadir}/MateConf/gsettings/*.convert
rm -rf %{buildroot}%{_datadir}/icons/shot.png
desktop-file-install                          \
  --delete-original                           \
  --dir %{buildroot}%{_datadir}/applications  \
%{buildroot}%{_datadir}/applications/*
%find_lang %{name} --with-gnome --all-name
%find_lang mate-disk-usage-analyzer --with-gnome --all-name
%find_lang mate-dictionary --with-gnome --all-name
%find_lang mate-search-tool --with-gnome --all-name
%find_lang mate-system-log --with-gnome --all-name
%oreon_autofiles mate-system-log usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mate-screenshot usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mate-dictionary usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mate-search-tool usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mate-disk-image-mounter usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mate-disk-usage-analyzer usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mate-utils-common -f %{oreon_filedir}/mate-utils-common.list
%files -n mate-utils-devel -f %{oreon_filedir}/mate-utils-devel.list
%files -n mate-system-log -f %{oreon_filedir}/mate-system-log.list
%files -n mate-screenshot -f %{oreon_filedir}/mate-screenshot.list
%files -n mate-dictionary -f %{oreon_filedir}/mate-dictionary.list
%files -n mate-search-tool -f %{oreon_filedir}/mate-search-tool.list
%files -n mate-disk-image-mounter -f %{oreon_filedir}/mate-disk-image-mounter.list
%files -n mate-disk-usage-analyzer -f %{oreon_filedir}/mate-disk-usage-analyzer.list

%changelog

%autochangelog
