%global source0_hash a026ef34c31b25975275cc29a5e4eba2b54524769672095a5228098a08acd82c
Name:		fprintd
Version:	1.94.5
Release:        1%{?dist}
Summary:        D-Bus service for Fingerprint reader access
License:	GPL-2.0-or-later AND GFDL-1.1-or-later
Source0:        https://gitlab.freedesktop.org/libfprint/fprintd/-/archive/v%{version}/fprintd-v%{version}.tar.gz
Url:		http://www.freedesktop.org/wiki/Software/fprint/fprintd
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  gtk-doc
BuildRequires:  libfprint-devel
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  perl-podlators
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  polkit-devel
BuildRequires:  python3-dbusmock
BuildRequires:  python3-libpamtest
# /oreon:deps
%description
D-Bus service to access fingerprint readers.

%package pam
Summary:	PAM module for fingerprint authentication
Requires:	%{name} = %{version}-%{release}
Provides:	pam_fprint = %{version}-%{release}
Obsoletes:	pam_fprint < 0.2-3
Requires(postun): authselect >= 0.3
License:	GPL-2.0-or-later
%description pam
PAM module that uses the fprintd D-Bus service for fingerprint
authentication.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
License:	GPL-2.0-or-later AND GFDL-1.1-or-later
BuildArch:	noarch
%description devel
Development documentation for fprintd, the D-Bus service for
fingerprint readers access.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%meson -Dgtk_doc=true -Dpam=true -Dpam_modules_dir=%{_libdir}/security
%meson_build
%install
%meson_install
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/lib/fprint
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%postun pam

if [ $1 -eq 0 ]; then
  /bin/authselect disable-feature with-fingerprint || :
fi
%files -f %{oreon_filedir}/main.list
%files -n fprintd-pam -f %{oreon_filedir}/fprintd-pam.list
%files -n fprintd-devel -f %{oreon_filedir}/fprintd-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.94.5-1
- Prepare for Oreon 11 (RP1)
