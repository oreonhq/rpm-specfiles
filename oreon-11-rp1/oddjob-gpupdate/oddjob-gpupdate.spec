%global source0_hash f348b37d7b744f5764feeae129c87bd1ccc35d782ea718dbfa0257d828c9d1b2
Name:           oddjob-gpupdate
Version:        0.2.3
Release:        1%{?dist}
Summary:        An oddjob helper which applies group policy objects
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/altlinux/oddjob-gpupdate.git
Source0:        https://github.com/altlinux/%{name}/archive/refs/tags/v%{version}/%{name}.%{version}.tar.gz
Patch0:         0001-Use-samba-gpupdate-to-apply-policy.patch
Patch1:         0002-Hardening-to-protect-against-malicous-usernames.patch
Patch2:         0003-execl-requires-the-exe-as-the-first-arg.patch
Patch3:         0004-Let-autoupdate-to-fix-obsolete-AC_PROG_LIBTOOL.patch
Requires: oddjob
Requires(post): /usr/bin/dbus-send
Requires(post): psmisc
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dbus-devel
BuildRequires:  gcc
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  oddjob
BuildRequires:  pam-devel
BuildRequires:  xmlto
# /oreon:deps
%description
This package contains the oddjob helper which can be used by the
pam_oddjob_gpupdate module to apply group policy objects at login-time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -if
%configure \
    --disable-static \
    --enable-pie \
    --enable-now \
    --with-selinux-acls \
    --with-selinux-labels
%make_build
%install
%make_install
rm -f %{buildroot}%{_pam_moduledir}/pam_oddjob_gpupdate.la
%oreon_autofiles main

%post

if test $1 -eq 1 ; then
    killall -HUP dbus-daemon 2>&1 > /dev/null
fi
if [ -f /var/lock/subsys/oddjobd ] ; then
    /usr/bin/dbus-send --system --dest=com.redhat.oddjob /com/redhat/oddjob com.redhat.oddjob.reload
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
