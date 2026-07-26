%global source0_hash c8a956f6f0660356b725cb06ef5835dfb36526043a4f8c1cfe7674bb7bdd6c5c

%global gitproject0	xca
%global gitowner0	chris2511

Summary:	Graphical X.509 certificate management tool
Name:		xca
Version:	2.9.0
Release:	2%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://hohnstaedt.de/xca/
Source0:	https://github.com/%{gitowner0}/%{gitproject0}/releases/download/RELEASE.%{version}/%{name}-%{version}.tar.gz
Source1:	xca-2.5.0-README.IMPORTANT

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Help)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	openssl-devel
%if 0%{?fedora} >= 41
BuildRequires:	openssl-devel-engine
%endif
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	libtool-ltdl-devel
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinxcontrib-qthelp

Requires:	hicolor-icon-theme

Suggests:	qt6-qtbase-mysql
Suggests:	qt6-qtbase-postgresql
Suggests:	qt6-qtbase-odbc

%description
  X Certificate and Key management is a graphic interface for managing
asymmetric keys like RSA or DSA, certificates and revocation lists. It is
intended as a small CA for creation and signing certificates. It uses the
OpenSSL library for the cryptographic operations.
  Certificate signing requests (PKCS#10), certificates (X509v3), the signing
of requests, the creation of self-signed certificates, certificate revocation
lists and SmartCards are supported. For an easy company-wide use, customizable
templates can be used for certificate and request generation. The PKI structures
can be imported and exported in several formats like PKCS#7, PKCS#12, PEM,
DER, PKCS#8. All cryptographic data are stored in a byte order agnostic file
format, portable across operating systems.

#-------------------------------------------------------------------------------
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#-------------------------------------------------------------------------------

%autosetup -p 1
cp '%{SOURCE1}' README.IMPORTANT

#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

export CXXFLAGS='%{optflags} -DDOCDIR=\"%{_docdir}/xca\"'
%cmake	-DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed"
%cmake_build

#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------

%cmake_install

#	Do not include db statistics program and man.
find '%{buildroot}' -name 'xca_db_stat*' -delete

#	Do not use pixmaps directory.
rm -rf '%{buildroot}%{_datadir}/pixmaps'

#	Reinstall documentation.
rm -rf '%{buildroot}%{_docdir}/xca'/*
mv '%{buildroot}%{_datadir}/xca/html' '%{buildroot}%{_docdir}/xca/'

#	Install mime file types.
install -d -m 755 '%{buildroot}%{_datadir}/mime/packages'
install -p -m 644 misc/xca.xml '%{buildroot}%{_datadir}/mime/packages/'

#	Validate desktop files.
desktop-file-validate %{buildroot}%{_datadir}/applications/de.hohnstaedt.xca.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/de.hohnstaedt.xca.metainfo.xml

#	Tag translation files.
%find_lang '%{name}' --with-qt

#-------------------------------------------------------------------------------
%files -f %{name}.lang
#-------------------------------------------------------------------------------

%doc AUTHORS COPYRIGHT README.IMPORTANT
%doc %{_docdir}/xca/*
%{_bindir}/xca
%dir %{_datadir}/xca
%{_datadir}/xca/*.txt
%{_datadir}/xca/*.xca
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/mime/packages/%{name}.*
%{_datadir}/applications/de.hohnstaedt.xca.desktop
%{_datadir}/bash-completion/
%{_metainfodir}/de.hohnstaedt.xca.metainfo.xml
%attr(0644, root, root) %{_mandir}/*/*
# template, contains no translations or language code
%exclude %{_datadir}/xca/i18n/xca.qm

#-------------------------------------------------------------------------------
%changelog
%autochangelog
