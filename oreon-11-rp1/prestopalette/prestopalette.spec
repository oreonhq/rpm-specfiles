%global source0_hash bdad1bec87a1a8c53f95c841d66f298f8a0ada858f7baa3e69ae168796d8b313

Name:		prestopalette
Version:	0.1.31
Release:	22%{?dist}
Summary:	An artist's tool for creating harmonious color palettes

License:	MIT
URL:		https://github.com/PrestoPalette/PrestoPalette
Source0:	https://github.com/PrestoPalette/PrestoPalette/archive/%{version}/%{version}.tar.gz#/prestopalette-%{version}.tar.gz
Source1:	https://raw.githubusercontent.com/PrestoPalette/PrestoPalette-Packaging/master/Fedora/PrestoPalette.appdata.xml#/PrestoPalette.appdata.xml
Source2:	https://raw.githubusercontent.com/PrestoPalette/PrestoPalette-Packaging/master/Fedora/Icon.png#/PrestoPalette.png

BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtmultimedia-devel

ExcludeArch: i686

%{?el7:BuildRequires: tar}

%description
%{name} is an artist's tool for creating harmonious color palettes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n PrestoPalette-%{version}

%build
%qmake_qt5 -config release PrestoPalette.pro && \
%make_build all
cat > PrestoPalette.desktop <<EOF
[Desktop Entry]
Name=PrestoPalette
Comment=An artist's tool for creating harmonious color palettes
Exec=PrestoPalette
Icon=%{_datadir}/pixmaps/PrestoPalette.png
Terminal=false
Type=Application
Categories=Graphics
EOF

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/{applications,pixmaps,metainfo}
install -Dp -m 755 build/release/PrestoPalette %{buildroot}/%{_bindir}
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications PrestoPalette.desktop
appstream-util validate-relax --nonet %{SOURCE1}
install -Dp -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/metainfo/
install -Dp -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/pixmaps/

%files
%{_bindir}/PrestoPalette
%{_datadir}/applications/PrestoPalette.desktop
%{_datadir}/metainfo/PrestoPalette.appdata.xml
%{_datadir}/pixmaps/PrestoPalette.png
%license LICENSE

%changelog
%autochangelog
