%global source0_hash 5f1f234bbbc6bb7aa1701031237a46788fe0a432c38c08b650ec49777e0b8080

Name:           x2godesktopsharing
Version:        3.2.0.0
Release:        19%{?dist}
Summary:        Share X11 desktops with other users via X2Go

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.x2go.org
Source0:        https://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-linguist
Requires:       hicolor-icon-theme
Requires:       x2goserver >= 4.0.0.0
%if 0%{?fedora}
Recommends:     x2goserver-desktopsharing >= 4.1.0.3
%else
Requires:       x2goserver-desktopsharing >= 4.1.0.3
%endif

%description
X2Go Desktop Sharing is an X2Go add-on tool that allows a user to 
grant other X2Go users access to the current session (shadow session
support). The current session may be an X2Go session itself or simply
a local X11 session.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Create a sysusers.d config file
cat >x2godesktopsharing.sysusers.conf <<EOF
g x2godesktopsharing -
EOF

%build
lrelease-qt5 x2godesktopsharing.pro
%{qmake_qt5}
%make_build

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_datadir}/{applications,x2go}
cp -p %{name} %{buildroot}%{_bindir}/
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop
mkdir -p %{buildroot}%{_datadir}/%{name}/icons
install -p -m 644 icons/%{name}.xpm %{buildroot}%{_datadir}/%{name}/icons/%{name}.xpm
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,64x64,128x128}/apps
install -p -m 644 icons/128x128/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -p -m 644 icons/16x16/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -p -m 644 icons/64x64/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -p -m 644 icons/32x32/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/x2go/versions
install -p -m 644 VERSION.x2godesktopsharing %{buildroot}%{_datadir}/x2go/versions/VERSION.x2godesktopsharing
cp -rp man %{buildroot}%{_datadir}/

install -m0644 -D x2godesktopsharing.sysusers.conf %{buildroot}%{_sysusersdir}/x2godesktopsharing.conf

%files
%license COPYING
%doc ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/x2go/versions/VERSION.x2godesktopsharing
%{_mandir}/man1/%{name}.1.gz
%{_sysusersdir}/x2godesktopsharing.conf

%changelog
%autochangelog
