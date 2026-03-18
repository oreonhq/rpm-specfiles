Name:           librhsm
Version:        0.0.4
Release:        2%{?dist}
Summary:        Red Hat Subscription Manager library
License:        LGPL-2.1-or-later
URL:            https://github.com/rpm-software-management/librhsm
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
# Key exported from Petr Pisar's keyring
Source2:        gpgkey-E3F42FCE156830A80358E6E94FD1AEC3365AF7BF.gpg

BuildRequires:  gnupg2
BuildRequires:  meson >= 0.37.0
BuildRequires:  gcc
BuildRequires:  pkgconfig(gio-2.0) >= 2.44
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2
BuildRequires:  pkgconfig(openssl)

%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.0

%files devel
%{_libdir}/%{name}.so
%{_includedir}/rhsm/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.4-2
- Prepare for Oreon 11 (RP1)
