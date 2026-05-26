Name:		fprintd
Version:	1.94.5
Release:	%autorelease
Summary:	D-Bus service for Fingerprint reader access

# man page is GFDL-1.1-or-later
License:	GPL-2.0-or-later AND GFDL-1.1-or-later
Source0:	https://gitlab.freedesktop.org/libfprint/fprintd/-/archive/v%{version}/fprintd-v%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 a026ef34c31b25975275cc29a5e4eba2b54524769672095a5228098a08acd82c
%global source0_file fprintd-v1.94.5.tar.gz
# oreon url source checksums end
Url:		http://www.freedesktop.org/wiki/Software/fprint/fprintd

BuildRequires:	meson
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	git
BuildRequires:	pam-devel
BuildRequires:	libfprint-devel >= 1.94.0
BuildRequires:	polkit-devel
BuildRequires:	gtk-doc
BuildRequires:	gettext
BuildRequires:	perl-podlators
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	python3-dbusmock
BuildRequires:	python3-libpamtest


%description
D-Bus service to access fingerprint readers.

%package pam
Summary:	PAM module for fingerprint authentication
Requires:	%{name} = %{version}-%{release}
# Note that we obsolete pam_fprint, but as the configuration
# is different, it will be mentioned in the release notes
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
# dbus interfaces are GPL-2.0-or-later
# documentation is GFDL-1.1-or-later
License:	GPL-2.0-or-later AND GFDL-1.1-or-later
BuildArch:	noarch

%description devel
Development documentation for fprintd, the D-Bus service for
fingerprint readers access.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/fprintd-v1.94.5.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a026ef34c31b25975275cc29a5e4eba2b54524769672095a5228098a08acd82c" || { echo "oreon: Source0 SHA256 mismatch for fprintd-v1.94.5.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -S git -n %{name}-v%{version}

%build
%meson -Dgtk_doc=true -Dpam=true -Dpam_modules_dir=%{_libdir}/security
%meson_build

%install
%meson_install
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/lib/fprint

%find_lang %{name}

%postun pam
if [ $1 -eq 0 ]; then
  /bin/authselect disable-feature with-fingerprint || :
fi

%files -f %{name}.lang
%doc README COPYING AUTHORS TODO
%{_bindir}/fprintd-*
%{_libexecdir}/fprintd
# FIXME This file should be marked as config when it does something useful
%{_sysconfdir}/fprintd.conf
%{_datadir}/dbus-1/system.d/net.reactivated.Fprint.conf
%{_datadir}/dbus-1/system-services/net.reactivated.Fprint.service
%{_unitdir}/fprintd.service
%{_datadir}/polkit-1/actions/net.reactivated.fprint.device.policy
%attr(0700, -, -) %{_localstatedir}/lib/fprint
%{_mandir}/man1/fprintd.1.gz

%files pam
%doc pam/README
%{_libdir}/security/pam_fprintd.so
%{_mandir}/man8/pam_fprintd.8.gz

%files devel
%{_datadir}/gtk-doc/
%{_datadir}/dbus-1/interfaces/net.reactivated.Fprint.Device.xml
%{_datadir}/dbus-1/interfaces/net.reactivated.Fprint.Manager.xml

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.94.5-1
- Prepare for Oreon 11 (RP1)
