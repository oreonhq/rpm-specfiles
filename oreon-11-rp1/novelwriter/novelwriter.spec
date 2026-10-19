%global source0_hash 3faab2ddfc69b43eec95527ee696d385bda9b6167b81424dbb5a1dc6c4863188
Name:           novelwriter
Version:        2.7.4
Release:        1%{?dist}
Summary:        Plain text editor designed for writing novels
License:        GPL-3.0-or-later AND CC-BY-SA-4.0 AND Apache-2.0 AND MIT
URL:            https://novelwriter.io/
Source0:        https://github.com/vkbo/novelwriter/archive/v%{version}/novelwriter-%{version}.tar.gz
BuildArch:      noarch
Requires:       hicolor-icon-theme
Provides:       bundled(material-design-icons)
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-novelwriter = %{version}-%{release}
# /oreon:deps
%description
novelWriter is a plain text editor designed for writing novels assembled from
many smaller text documents. It uses a minimal formatting syntax inspired by
Markdown, and adds a meta data syntax for comments, synopsis, and
cross-referencing. It's designed to be a simple text editor that allows for
easy organization of text and notes, using human readable text files as
storage for robustness.

The project storage is suitable for version control software, and also well
suited for file synchronization tools. All text is saved as plain text files
with a meta data header. The core project structure is stored in a single
project XML file. Other meta data is primarily saved as JSON files.

%package doc
Summary: Documentation for novelWriter
BuildArch:  noarch
%description doc
Documentation for novelWriter in docbook format. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n novelWriter-%{version} -p1
# https://github.com/vkbo/novelWriter/issues/2276
sed -i 's/self.spellLanguage = "en"/self.spellLanguage = "en_US"/g' novelwriter/config.py
sed -i 's/spellcheck = en/spellcheck = en_US/g' tests/reference/baseConfig_novelwriter.conf
# Use Fedora specific variant for qt6
sed -i 's/"lrelease"/"lrelease-qt6"/g' utils/assets.py

%build

%python3 pkgutils.py qtlrelease
%python3 pkgutils.py sample
pushd docs
sphinx-build source texinfo -b texinfo
pushd texinfo
makeinfo --docbook novelwriter.texi
popd
popd
%pyproject_wheel
%install
%pyproject_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications setup/data/novelwriter.desktop
mkdir -p %{buildroot}%{_metainfodir}/
install -m644 setup/novelwriter.appdata.xml %{buildroot}%{_metainfodir}/
mkdir -p %{buildroot}%{_datadir}/icons
cp -r -p setup/data/hicolor %{buildroot}%{_datadir}/icons/
install -pDm0644 docs/texinfo/novelwriter.xml \
  %{buildroot}%{_datadir}/help/en/novelwriter/novelwriter.xml
for file in docs/texinfo/novelwriter-figures/*.*
do
  install -pDm0644 $file \
  %{buildroot}%{_datadir}/help/en/novelwriter/novelwriter-figures/$(basename $file)
done
%find_lang nw --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

QT_QPA_PLATFORM=offscreen %pytest
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/novelwriter.appdata.xml
%files
%files -n novelwriter-doc -f %{oreon_filedir}/novelwriter-doc.list

%changelog

%autochangelog
