%global source0_hash 3f84f66e97b5f408b829060db2fedb3b6622740651a1cf646382554fc3fb1671
Name:           librhsm
Version:        0.0.5
Release:        1%{?dist}
Summary:        Red Hat Subscription Manager library
License:        LGPL-2.1-or-later
URL:            https://github.com/rpm-software-management/librhsm
Source0:        https://github.com/rpm-software-management/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-E3F42FCE156830A80358E6E94FD1AEC3365AF7BF.gpg
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(openssl)
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n librhsm-devel -f %{oreon_filedir}/librhsm-devel.list

%changelog

%autochangelog
