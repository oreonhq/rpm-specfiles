%global source0_hash none

%global source2_key_fpr 34FF9526CFEF0E97A340E2E40FDE7BE0E88F5E48

# See https://gitlab.freedesktop.org/emersion/libdisplay-info/-/merge_requests/149
# for library versioning explanation.
%global sover 3

Name:           libdisplay-info
Version:        0.3.0
Release:        1%{?dist}
Summary:        EDID and DisplayID library

# Main license: MIT
# test/data: CC-BY-4.0, MIT (see test/data/README.md).
License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/libdisplay-info
Source0:        https://gitlab.freedesktop.org/emersion/libdisplay-info/-/releases/0.3.0/downloads/libdisplay-info-0.3.0.tar.xz
Source1:        libdisplay-info-0.3.0.tar.xz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.57
BuildRequires:  pkgconfig(hwdata)

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
%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup


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
%{_libdir}/%{name}.so.%{sover}
%{_libdir}/%{name}.so.%{version}

%files tools
%{_bindir}/di-edid-decode

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.0-1
- Prepare for Oreon 11 (RP1)
