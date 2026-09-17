%global source0_hash e8815251b370fae2379d5ec49f0d93052063768f35aae18b14c494054e9cabe4

Name:           klog
Version:        2.4.2
Release:        2%{?dist}
Summary:        A Ham radio logging program for KDE

License:        GPL-2.0-or-later
URL:            https://www.klog.xyz/

Source0:        https://github.com/ea4k/klog/releases/download/%{version}/%{name}-%{version}.tar.gz
Source100:      klog.desktop
Source101:      klog_48x48.png
Source102:      klog_64x64.png
Source103:      klog_128x128.png
Source104:      klog_256x256.png
Source105:      klog_512x512.png
Source106:      xyz.klog.klog.metainfo.xml

ExcludeArch:    i686

BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  gettext
BuildRequires:  hamlib-devel
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtcharts-devel
BuildRequires:  qt6-qtserialport-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtlocation-devel

%if ! 0%{?rhel} < 8
Recommends:     trustedqsl
%endif

%description
# Spelling intentional ignore rpmlint warnings.
KLog is a Ham radio logging program for KDE
Some features include:
    * DXCC award support.
    * Basic IOTA support.
    * Importing from Cabrillo files.
    * Importing from TLF.
    * Adding/Editing QSOs.
    * Save/read to/from disk file the log - ADIF format by default.
    * English/Spanish/Portuguese/Galician/Serbian/Swedish support.
    * QSL sent/received support.
    * Read/Write ADIF.
    * Delete QSOs.
    * DX-Cluster support. 

Some additional features of this application are still under development
and are not yet implemented.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Prep icon files
install -p %{SOURCE101} %{SOURCE102} %{SOURCE103} %{SOURCE104} %{SOURCE105} .

# Fix line endings
dos2unix TODO

%build
%qmake_qt6 PREFIX=%{buildroot}%{_prefix} src.pro
%make_build

%install
%make_install

# Manuall install translations because qmake is being stupid.
mkdir -p %{buildroot}%{_datadir}/%{name}/translations
install -pm 0644 build/target/translations/*.qm \
                 %{buildroot}%{_datadir}/%{name}/translations/

# Remove docs installed to wrong location
rm -f %{buildroot}%{_datadir}/%{name}/{COPYING,Changelog}

%find_lang %{name} --with-qt

# Install the provided desktop icon
for size in 48x48 64x64 128x128 256x256 512x512; do
    install -pDm 0644 %{name}_$size.png \
        %{buildroot}%{_datadir}/icons/hicolor/$size/apps/%{name}.png
done

# Install the provided desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
    %{SOURCE100}

# Install the provided AppStream metadata file
install -Dm 0644 %{SOURCE106} \
    %{buildroot}%{_metainfodir}/xyz.klog.klog.metainfo.xml

%files -f %{name}.lang
%doc AUTHORS README TODO NEWS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/mapqmlfile.qml
%{_datadir}/%{name}/marker.qml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/xyz.klog.klog.metainfo.xml

%changelog
%autochangelog
