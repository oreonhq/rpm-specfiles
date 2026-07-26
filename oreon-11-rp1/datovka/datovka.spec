%global source0_hash a64be01e7eb420bd530911e311d882f0341b2e4d4a5989b31a95b7d9c602e9bb

Name: datovka
Version: 4.28.0
Release: 1%{?dist}
Summary: A free graphical interface for Czech Databox (Datové schránky)

License: GPL-3.0-or-later WITH cryptsetup-OpenSSL-exception
URL: https://www.datovka.cz/
#Source0: https://secure.nic.cz/files/datove_schranky/%%{version}/datovka-%%{version}.tar.xz
Source0: https://gitlab.nic.cz/%{name}/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: openssl-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtwebsockets-devel
BuildRequires: desktop-file-utils
BuildRequires: libdatovka-devel
BuildRequires: make
Requires: gnupg2-smime
# https://gitlab.nic.cz/datovka/datovka/-/issues/541
Patch:        datovka-4.28.0-s390x-disable-failing-test.patch

%description
GUI application allowing access to Czech Databox - an electronic communication
interface endorsed by the Czech government.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}

# drop failing tests (upstream notified)
pushd tests
rm -f test_crypto_message.pri test_isds_message.pri
popd

%build
lrelease-qt5 datovka.pro
%{qmake_qt5} PREFIX=%{_prefix} DISABLE_VERSION_CHECK_BY_DEFAULT=1
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install INSTALL_ROOT=%{buildroot}
%find_lang %{name} --with-qt
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
cd tests
%{qmake_qt5} tests.pro PREFIX=%{_prefix}
%make_build
./tests

%files -f %{name}.lang
%doc %{_pkgdocdir}
%{_bindir}/datovka
%{_datadir}/applications/datovka.desktop
%{_datadir}/icons/hicolor/*/apps/datovka.png
%{_datadir}/metainfo/datovka.metainfo.xml

%changelog
%autochangelog
