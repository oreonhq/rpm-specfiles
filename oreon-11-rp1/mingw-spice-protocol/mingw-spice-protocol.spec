%global source0_hash 04ffba610d9fd441cfc47dfaa135d70096e60b1046d2119d8db2f8ea0d17d912

Name:           mingw-spice-protocol
Version:        0.14.4
Release:        12%{?dist}
Summary:        Spice protocol header files
# Main headers are BSD, controller / foreign menu are LGPL
# Automatically converted from old format: BSD and LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.spice-space.org/
Source0:        http://www.spice-space.org/download/releases/spice-protocol-%{version}.tar.xz
Source1:        http://www.spice-space.org/download/releases/spice-protocol-%{version}.tar.xz.sig
Source2:        victortoso-E37A484F.keyring

BuildArch:      noarch
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  meson gcc git gnupg2

%description
Header files describing the spice protocol
and the para-virtual graphics card QXL.

%package -n mingw32-spice-protocol
Summary:        Spice protocol header files
Requires:       pkgconfig

%description -n mingw32-spice-protocol
Header files describing the spice protocol
and the para-virtual graphics card QXL.

%package -n mingw64-spice-protocol
Summary:        Spice protocol header files
Requires:       pkgconfig

%description -n mingw64-spice-protocol
Header files describing the spice protocol
and the para-virtual graphics card QXL.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -S git_am -n spice-protocol-%{version}

%build
%mingw_meson
%mingw_ninja

%install
export DESTDIR=%{buildroot}
%mingw_ninja install

%files -n mingw32-spice-protocol
%doc COPYING CHANGELOG.md
%{mingw32_includedir}/spice-1
%{mingw32_datadir}/pkgconfig/spice-protocol.pc

%files -n mingw64-spice-protocol
%doc COPYING CHANGELOG.md
%{mingw64_includedir}/spice-1
%{mingw64_datadir}/pkgconfig/spice-protocol.pc

%changelog
%autochangelog
