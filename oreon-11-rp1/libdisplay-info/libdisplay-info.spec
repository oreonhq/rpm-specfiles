%global source1_hash a158d8d7d69e0d2e54f8351477f830f78cad8a83096adc75cf1d7aee3edaa734
%global source0_hash 6ae77cd937f9cf7d1321d35c116062c4911e8447010a6a713ac4286f7a9d5987
%global source2_key_fpr 34FF9526CFEF0E97A340E2E40FDE7BE0E88F5E48
%global sover 3
Name:           libdisplay-info
Version:        0.3.0
Release:        1%{?dist}
Summary:        EDID and DisplayID library
License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/libdisplay-info
Source0:        https://gitlab.freedesktop.org/emersion/libdisplay-info/-/releases/0.3.0/downloads/libdisplay-info-0.3.0.tar.xz
Source1:        https://gitlab.freedesktop.org/emersion/libdisplay-info/-/releases/0.3.0/downloads/libdisplay-info-0.3.0.tar.xz.sig
Source2:        gpgkey-0FDE7BE0E88F5E48.gpg
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(hwdata)
# /oreon:deps
%description
%{summary}.

%package        tools
Summary:        Command-line tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tools
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libdisplay-info-tools -f %{oreon_filedir}/libdisplay-info-tools.list
%files -n libdisplay-info-devel -f %{oreon_filedir}/libdisplay-info-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.0-1
- Prepare for Oreon 11 (RP1)
