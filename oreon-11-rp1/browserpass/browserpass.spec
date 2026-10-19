%global source0_hash aaeab732115f9c44eccd9201b03e56090286c28f5483a57851fe4e21d0361f84
%bcond check 0
%global goipath         github.com/browserpass/browserpass-native
%global tag             %{version}
Version:                3.1.2
%global native_mozpath %{_libdir}/mozilla/native-messaging-hosts
%global native_chromepath %{_sysconfdir}/chromium/native-messaging-hosts
%global native_id com.github.browserpass.native
%gometa -f
%global common_description %{expand:
This is a host application for browserpass browser extension providing it
access to your password store. The communication is handled through
Native Messaging API.}
Name:           browserpass
Release:        1%{?dist}
Summary:        Native messaging host
License:        ISC
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version}/%{name}-native-%{version}.tar.gz
# oreon:deps
BuildRequires:  gnupg2
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  jq
# /oreon:deps
%package -n       browserpass-firefox
Summary:        Native component for the Firefox extension
BuildArch:      noarch

%description -n browserpass-firefox
Native component for the Firefox extension

%package -n       browserpass-chromium
Summary:        Native component for the Chromium extension
BuildArch:      noarch

%description -n browserpass-chromium
Native component for the Chromium extension

%description %{common_description}

%package firefox
Summary: Native component for the Firefox extension
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: mozilla-filesystem
Recommends: firefox
%description firefox
Browserpass native component for the Firefox extension

%package chromium
Summary: Native component for the Chromium extension
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: chromium
%description chromium
Browserpass native component for the Chromium extension

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%goprep

%build

%gobuild -o %{gobuilddir}/bin/browserpass-native %{goipath}
%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                     %{buildroot}%{native_mozpath}
jq '.path = "%{_bindir}/browserpass-native"' browser-files/firefox-host.json > %{buildroot}%{native_mozpath}/%{native_id}.json
install -m 0755 -vd                     %{buildroot}%{native_chromepath}
jq '.path = "%{_bindir}/browserpass-native"' browser-files/chromium-host.json > %{buildroot}%{native_chromepath}/%{native_id}.json
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n browserpass-firefox -f %{oreon_filedir}/browserpass-firefox.list
%files -n browserpass-chromium -f %{oreon_filedir}/browserpass-chromium.list

%changelog

%autochangelog
