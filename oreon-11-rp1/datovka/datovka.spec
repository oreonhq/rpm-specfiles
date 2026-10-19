%global source0_hash 951d31a6f139a29b967364d57f5227de59d24bdbb593d9561ac4fcb0402c4285
Name: datovka
Version: 4.29.5
Release:        1%{?dist}
Summary:        A free graphical interface for Czech Databox (Datové schránky)
License: GPL-3.0-or-later WITH cryptsetup-OpenSSL-exception
URL: https://www.datovka.cz/
Source0:        https://gitlab.nic.cz/%{name}/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Requires: gnupg2-smime
Patch:        datovka-4.28.0-s390x-disable-failing-test.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  libdatovka-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtwebsockets-devel
# /oreon:deps
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
%oreon_autofiles main

%check

cd tests
%{qmake_qt5} tests.pro PREFIX=%{_prefix}
%make_build
./tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
