%global source0_hash 350a1dd0a8ed6a2c9c183cff2a21f394299e968fcc6ae2e8c93c565dae604ae8

%global branch 1.28

Name:          mate-polkit
Version:       %{branch}.1
Release:       %autorelease
Summary:       Integrates polkit authentication for MATE desktop
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: gtk3-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: polkit-devel
BuildRequires: libappindicator-gtk3-devel

Provides:   PolicyKit-authentication-agent
# dropping -devel subpackage 
Provides:   mate-polkit-devel%{?_isa} = %{version}-%{release}
Provides:   mate-polkit = %{version}-%{release}
Obsoletes:  mate-polkit-devel < %{version}-%{release}

%description
Integrates polkit with the MATE Desktop environment

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

# fix https://github.com/mate-desktop/mate-polkit/issues/56
sed -i '/^Categories=/d' src/polkit-mate-authentication-agent-1.desktop.in
sed -i '/^Categories=/d' src/polkit-mate-authentication-agent-1.desktop.in.in

%build
%configure  \
        --disable-static       \
        --enable-accountsservice \
        --enable-appindicator=yes

make %{?_smp_mflags} V=1

%install
%{make_install}

%find_lang %{name}

find %{buildroot} -name '*.la' -exec rm -fv {} ';'

%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/polkit-mate-authentication-agent-1.desktop

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_sysconfdir}/xdg/autostart/polkit-mate-authentication-agent-1.desktop
%{_libexecdir}/polkit-mate-authentication-agent-1

%changelog
%autochangelog
