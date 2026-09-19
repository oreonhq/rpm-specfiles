%global source0_hash faecd3c499bb4acb92af7477a4990443b7050e997cc910570bc685385b69be90

Summary: Creates xguest user as a locked down user 
Name: xguest
Version: 1.0.10
Release: 54%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
BuildArch: noarch
Source: http://people.fedoraproject.org/~dwalsh/xguest/%{name}-%{version}.tar.bz2
URL: http://people.fedoraproject.org/~dwalsh/xguest/

Requires(pre): pam >= 0.99.8.1-17 selinux-policy-targeted > 3.6.3-12
Requires(pre): policycoreutils-sandbox

%description
Installing this package sets up the xguest user to be used as a temporary
account to switch to or as a kiosk user account. The account is disabled unless
SELinux is in enforcing mode. The user is only allowed to log in via graphical login program.
The home and temporary directories of the user will be polyinstantiated and
mounted on tmpfs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
%{__rm} -fR %{buildroot}
%{__mkdir} -p %{buildroot}/%{_sysconfdir}/security/namespace.d/
%{__mkdir} -p %{buildroot}/var/lib/xguest/home
install -m0644 xguest.conf %{buildroot}/%{_sysconfdir}/security/namespace.d/

%post
if [ $1 -eq 1 ]; then
semanage user -a  -S targeted -P xguest -R xguest_r xguest_u  2> /dev/null  || :
(useradd -c "Guest" -Z xguest_u -d /var/lib/xguest/home/xguest xguest || semanage login -a -S targeted -s xguest_u xguest || semanage login -m -S targeted -s xguest_u xguest) 2>/dev/null || exit 1
head -c 32  /dev/urandom | passwd xguest --stdin

echo "xguest:exclusive" >> /etc/security/sepermit.conf

semanage -S targeted -i - << _EOF
boolean -m --on allow_polyinstantiation 
boolean -m --on xguest_connect_network
boolean -m --on xguest_mount_media
boolean -m --on xguest_use_bluetooth
_EOF
fi

%files
%{_sysconfdir}/security/namespace.d/xguest.conf
%doc README LICENSE
%dir /var/lib/xguest/home
%dir /var/lib/xguest

%preun
if [ $1 -eq 0 ]; then
sed -i '/^xguest/d' /etc/security/sepermit.conf

fi

%changelog
%autochangelog
