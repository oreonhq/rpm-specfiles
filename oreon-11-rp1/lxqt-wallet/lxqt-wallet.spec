%global source0_hash d19d61e7c1263416b082b9899cc486833dc109d36fc1ce786751c4f4dd887951

%global srcname lxqt_wallet

Name:           %(echo %{srcname} |tr _ - )
Version:        4.0.2
Release:        4%{?dist}
Summary:        Create a kwallet like functionality for LXQt

License:        BSD-2-Clause
URL:            https://github.com/lxqt/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(lxqt)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  libgcrypt-devel
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  qt6-linguist

%description
This project seeks to give a functionality for secure storage
of information that can be presented in key-values pair like
user names-passwords pairs.

Currently the project can store the information in KDE's kwallet,
GNOME's secret service or in an internal system that use libgcrypt
as its cryptographic backend.

The internal secure storage system allows the functionality to
be provided without dependencies on KDE or GNOME libraries.

This project is designed to be used by other projects simply by
adding the source folder in the build system and start using it.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       liblxqt-devel%{?_isa}

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n%{srcname}-%{version}
cp -p backend/README README-backend
cp -p frontend/README README-frontend

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%files -f %{name}.lang
%license LICENSE
%doc README.md changelog
%{_bindir}/lxqt_wallet-cli
%{_libdir}/liblxqt-wallet.so.6.0.0

%files devel
%doc README-*
%{_includedir}/lxqt/lxqt-wallet.h
%{_includedir}/lxqt/lxqt_wallet.h
%{_libdir}/liblxqt-wallet.so
%{_libdir}/pkgconfig/lxqt-wallet.pc

%changelog
%autochangelog
