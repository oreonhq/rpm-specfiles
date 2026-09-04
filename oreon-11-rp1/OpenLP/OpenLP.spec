%global source0_hash 426f003af1af7ca9aa307baaccc5029c00ff8a886a249c3937753bd2709b4173

%global modname 3.1.6

Summary: Open source Church presentation and lyrics projection application
Name: OpenLP
Version: 3.1.7
Release: 1%{?dist}
Source0: https://get.openlp.org/%{version}/OpenLP-%{version}.tar.gz
# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
BuildArch: noarch

URL: http://openlp.org/

# Remove pytest-runner from setup_requires
# https://gitlab.com/openlp/openlp/-/merge_requests/848
# https://fedoraproject.org/wiki/Changes/DeprecatePythonPytestRunner
Patch:          https://gitlab.com/openlp/openlp/-/merge_requests/848.patch

BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-qt5
Requires:       python3-beautifulsoup4
Requires:       python3-chardet
Requires:       python3-lxml
Requires:       python3-sqlalchemy
Requires:       python3-enchant
Requires:       python3-mako
Requires:       python3-openoffice
Requires:       python3-alembic
Requires:       python3-appdirs
Requires:       python3-webob
Requires:       python3-QtAwesome
Requires:       python3-websockets
Requires:       python3-waitress
Requires:       python3-pymediainfo
Requires:       python3-pyopengl
Requires:       python3-qt5-webengine
Requires:       python3-zeroconf
Requires:       python3-flask
Requires:       python3-flask-cors
Requires:       python3-pyicu
Requires:       hicolor-icon-theme
Requires:       libreoffice-graphicfilter
Requires:       libreoffice-impress
Requires:       python3-PyMuPDF
Requires:       python3-qrcode 

%description
OpenLP is a church presentation software, for lyrics projection software,
used to display slides of Songs, Bible verses, videos, images, and
presentations via LibreOffice using a computer and projector.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l openlp

install -m644 -p -D resources/images/openlp-logo-16x16.png \
   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/openlp.png
install -m644 -p -D resources/images/openlp-logo-32x32.png \
   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/openlp.png
install -m644 -p -D resources/images/openlp-logo-48x48.png \
   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/openlp.png
install -m644 -p -D resources/images/openlp-logo.svg \
   %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/openlp.svg

desktop-file-install \
  --dir %{buildroot}/%{_datadir}/applications \
  resources/openlp.desktop

desktop-file-validate %{buildroot}/%{_datadir}/applications/openlp.desktop

mkdir -p %{buildroot}%{_datadir}/openlp/i18n/
mv resources/i18n/*.qm %{buildroot}%{_datadir}/openlp/i18n
mkdir -p %{buildroot}%{_datadir}/mime/packages
cp -p resources/openlp.xml %{buildroot}%{_datadir}/mime/packages
 
%files -f %{pyproject_files}
%doc copyright.txt LICENSE
%{_bindir}/openlp
%{_datadir}/mime/packages/openlp.xml
%{_datadir}/applications/openlp.desktop
%{_datadir}/icons/hicolor/*/apps/openlp.*
%{_datadir}/openlp

%changelog
%autochangelog
