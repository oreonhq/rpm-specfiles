%global gitdate 20231216
%global commit0 fab698862466994a8fdc9aa335c87b4f05430ce6
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           signon-plugin-oauth2
Version:        0.25^%{gitdate}.%{shortcommit0}
Release:        7%{?dist}
Summary:        OAuth2 plugin for the Accounts framework

License:        LGPL-2.1-or-later
URL:            https://gitlab.com/accounts-sso/signon-plugin-oauth2

Source0:        https://gitlab.com/accounts-sso/signon-plugin-oauth2/-/archive/%{commit0}/%{name}-%{commit0}.tar.gz

BuildRequires: make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  pkgconfig(signon-plugins)
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libproxy-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup -n %{name}-%{commit0} -p1


%build
%qmake_qt6 \
    QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release \
    LIBDIR=%{?_libdir} \
    signon-oauth2.pro

%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}

# Delete tests
rm -fv %{buildroot}/%{_bindir}/signon-oauth2plugin-tests
rm -rfv %{buildroot}/%{_datadir}/signon-oauth2plugin-tests

# Delete examples
rm -fv %{buildroot}/%{_bindir}/oauthclient
rm -rvf %{buildroot}/%{_sysconfdir}


%check
%make_build check


%ldconfig_scriptlets

%files
%{_libdir}/signon/liboauth2plugin.so

%files devel
%{_includedir}/signon-plugins/*.h
%{_libdir}/pkgconfig/signon-oauth2plugin.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.25^%{gitdate}.%{shortcommit0}-7
- Prepare for Oreon 11 (RP1)
