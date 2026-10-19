%global source0_hash ddacd2a8120aeb2351e4486ee04a17782b5004aee99f2041d829bc4dcf2a5b3b
Name:           monit
Version:        6.0.0
Release:        1%{?dist}
Summary:        Manages and monitors processes, files, directories and devices
License:        AGPL-3.0-only
URL:            https://mmonit.com/monit/
Source0:        https://mmonit.com/monit/dist/%{name}-%{version}.tar.gz
%{?systemd_requires}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
monit is a utility for managing and monitoring, processes, files, directories
and devices on a UNIX system. Monit conducts automatic maintenance and repair
and can execute meaningful causal actions in error situations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Prevent-rerunning autoconf.
touch -r aclocal.m4 configure*
touch -r libmonit/aclocal.m4 libmonit/configure*

%build

%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -p -D -m0600 monitrc $RPM_BUILD_ROOT%{_sysconfdir}/monitrc
install -p -D -m0755 monit $RPM_BUILD_ROOT%{_bindir}/monit
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
install -m0644 system/startup/monit.service ${RPM_BUILD_ROOT}%{_unitdir}/monit.service
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/monit.d
%{__sed} -i 's/# set daemon  120.*/set daemon 60  # check services at 1-minute intervals/' \
    $RPM_BUILD_ROOT%{_sysconfdir}/monitrc
%{__sed} -i 's/#  include \/etc\/monit.d\/\*/include \/etc\/monit.d\/\*/' \
    $RPM_BUILD_ROOT%{_sysconfdir}/monitrc
%oreon_autofiles main

%post

%systemd_post monit.service
[ -f %{_sysconfdir}/monit.conf ] &&
    touch -r %{_sysconfdir}/monitrc %{_sysconfdir}/monit.conf &&
    mv -f %{_sysconfdir}/monit.conf %{_sysconfdir}/monitrc 2> /dev/null || :
%preun

%systemd_preun monit.service
%postun

%systemd_postun_with_restart monit.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
