%global source0_hash ee019ef7003df5f7f117aae381770172664c6f98df4396b079efe279eb17decc

Name:           xwxapt
Version:        3.4.1
Release:        18%{?dist}
Summary:        GTK+ graphical application for decoding and saving weather images

# Most files are GPLv2+ but some are GPLv3+ so combined work is GPLv3+
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later

URL:            http://www.5b4az.org/
Source0:        http://www.5b4az.org/pkg/apt/%{name}/%{name}-%{version}.tar.bz2
#add .desktop file
Source1:        %{name}.desktop
#temporary Icon
Source2:        %{name}.png
#Wrapper script for user config
Source3:        %{name}.sh.in

Patch1: xwxapt-3.4.1-fedora-c99.patch

BuildRequires: make
BuildRequires:  gcc gcc-c++
BuildRequires:  automake autoconf libtool gettext
BuildRequires:	alsa-lib-devel
BuildRequires:  gtk3-devel
BuildRequires:  rtl-sdr-devel
BuildRequires:  desktop-file-utils

Requires:	alsa-lib

%description
xwxapt is a GTK+ graphical version of wxapt. It uses the same decoding
engine as wxapt but it displays APT images at half-size as they are
received, storing the full-sized files when reception is completed. 

It also displays some status information (audio level, sync level,
sync status etc) and text messages as it runs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
./autogen.sh
%configure LDFLAGS="-lm"
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" PACKAGE_LIBS="$PACKAGE_LIBS -lm"

%install
# Install tries to install stuff to $HOME so do it manually...
install -pDm 0755 src/%{name} %{buildroot}%{_bindir}/%{name}.bin

#install default user configuration file
install -pDm 0644 %{name}/xwxaptrc %{buildroot}%{_datadir}/%{name}/xwxaptrc

#install wrapper script 
install -pDm 0755 %{SOURCE3} %{buildroot}%{_bindir}/xwxapt

# no upstream .desktop or icon yet so we'll use a temporary one
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -p %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png

desktop-file-install  \
        --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%doc AUTHORS README NEWS
%doc doc/xwxapt.html
%license COPYING
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*%{name}.desktop

%changelog
%autochangelog
