%global gitdate 20240205
%global commit0 eef943f0edf3beee8ecb85d4a9dae3656002fc24
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           signon-ui
Version:        0.15^%{gitdate}.%{shortcommit0}
Release:        6%{?dist}
Summary:        Online Accounts Sign-on Ui

License:        GPL-3.0-only
URL:            https://launchpad.net/signon-ui

# Source0:      https://launchpad.net/signon-ui/trunk/%{version}/+download/signon-ui-%{version}.tar.bz2
Source0:        https://gitlab.com/accounts-sso/%{name}/-/archive/%{commit0}/%{name}-%{commit0}.tar.bz2

%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  libaccounts-qt6-devel
BuildRequires:  signon-qt6-devel
BuildRequires:  signon-devel
BuildRequires:  libproxy-devel
BuildRequires:  libnotify-devel

Requires:       dbus

%description
Sign-on UI is the component responsible for handling the user interactions which
can happen during the login process of an online account.
It can show password dialogs and dialogs with embedded web pages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{commit0}


%build
export PATH=%{_qt6_bindir}:$PATH
%{qmake_qt6} QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release signon-ui.pro

make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot}

# Own directory where others can install provider-specific configuration
mkdir -p %{buildroot}/%{_sysconfdir}/signon-ui/webkit-options.d

%files
%doc README TODO NOTES
%license COPYING
%{_bindir}/signon-ui
%{_datadir}/dbus-1/services/*.service
%{_datadir}/applications/signon-ui.desktop
%{_sysconfdir}/signon-ui

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.15^%{gitdate}.%{shortcommit0}-6
- Prepare for Oreon 11 (RP1)
