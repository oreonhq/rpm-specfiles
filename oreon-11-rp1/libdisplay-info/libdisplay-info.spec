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
Source1:        https://gitlab.freedesktop.org/emersion/libdisplay-info/-/releases/0.3.0/downloads/libdisplay-info-0.3.0.tar.xz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg
# oreon url source checksums begin
%global source0_sha256 6ae77cd937f9cf7d1321d35c116062c4911e8447010a6a713ac4286f7a9d5987
%global source0_file libdisplay-info-0.3.0.tar.xz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libdisplay-info-0.3.0.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6ae77cd937f9cf7d1321d35c116062c4911e8447010a6a713ac4286f7a9d5987" || { echo "oreon: Source0 SHA256 mismatch for libdisplay-info-0.3.0.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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
