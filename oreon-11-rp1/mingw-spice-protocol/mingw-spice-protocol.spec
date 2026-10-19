%global source1_hash f03c8b49a6e9356b6ed1e9cfc7c0d7e79864348707812cbea79391a660ff4068
%global source0_hash baf58449f6e89d19f475899ad5fb9196fdc46c03cc53233f4e39cf2978f9cff7
Name:           mingw-spice-protocol
Version:        0.14.5
Release:        1%{?dist}
Summary:        Spice protocol header files
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.spice-space.org/
Source0:        http://www.spice-space.org/download/releases/spice-protocol-%{version}.tar.xz
Source1:        http://www.spice-space.org/download/releases/spice-protocol-%{version}.tar.xz.sig
Source2:        victortoso-E37A484F.keyring
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
# /oreon:deps
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
%oreon_autofiles mingw32-spice-protocol usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-spice-protocol usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-spice-protocol -f %{oreon_filedir}/mingw32-spice-protocol.list
%files -n mingw64-spice-protocol -f %{oreon_filedir}/mingw64-spice-protocol.list

%changelog

%autochangelog
