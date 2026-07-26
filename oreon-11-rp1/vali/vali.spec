%global source0_hash 791785eca66392f91f28ca371ba9cfa2dc11915df0bff9f590a33453f67e5756

%global abi_ver 1

Name:           vali
Version:        0.1.1
Release:        %autorelease
Summary:        Varlink C implementation and code generator

License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/vali
Source0:        %{url}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz
Source1:        %{url}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

BuildRequires:  gcc
BuildRequires:  gpgverify
BuildRequires:  meson >= 1
BuildRequires:  pkgconfig(aml)
BuildRequires:  pkgconfig(json-c)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/libvali.so.%{abi_ver}
%{_libdir}/libvali.so.%{version}

%files devel
%{_bindir}/vali
%{_includedir}/vali.h
%{_libdir}/libvali.so
%{_libdir}/pkgconfig/vali.pc

%changelog
%autochangelog
