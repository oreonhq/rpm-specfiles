%global source0_hash db63293d38f72795a0a92b0002cbef7d0b0b611f765c4c7bcc1ed6e0144d474b

Name:          sailcut
Version:       1.5.1
Release:       3%{?dist}
Summary:       A sail design and plotting software

License:       GPL-2.0-only
URL:           http://www.sailcut.com/
Source0:       https://github.com/sailcut/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:       sailcut.desktop
Source2:       sailcut.xml

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtsvg-devel
BuildRequires: qt6-qttools-devel
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: transfig
BuildRequires: desktop-file-utils
BuildRequires: shared-mime-info

%description
Sailcut CAD is a sail design and plotting software.
It allows you to design and visualize your own sail and compute the accurate
development of all panels in flat sheets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%qmake_qt6 PREFIX=%{_prefix} %{name}.pro
%make_build
pushd doc
mkdir build
./makedocs $PWD/build
popd

%install
make INSTALL_ROOT=%{buildroot} install
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/mime/packages/%{name}.xml
install -p -D -m 644 icons/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -p -D -m 644 icons/%{name}-file.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-%{name}.svg
%{_bindir}/desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md doc/build/en/*
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/%{name}.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-%{name}.svg
%{_datadir}/metainfo/org.sailcut.cad.metainfo.xml

%changelog
%autochangelog
