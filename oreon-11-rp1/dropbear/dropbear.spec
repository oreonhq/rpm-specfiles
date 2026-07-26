%global source0_hash 0d1f7ca711cfc336dc8a85e672cab9cfd8223a02fe2da0a4a7aeb58c9e113634

Name:              dropbear
Version:           2025.89
Release:           3%{?dist}
Summary:           Lightweight SSH server and client
License:           MIT
URL:               https://matt.ucc.asn.au/dropbear/dropbear.html
Source0:           https://matt.ucc.asn.au/%{name}/releases/%{name}-%{version}.tar.bz2
Source1:           https://matt.ucc.asn.au/%{name}/releases/%{name}-%{version}.tar.bz2.asc
Source2:           https://matt.ucc.asn.au/dropbear/releases/dropbear-key-2015.asc
Source4:           dropbear.service
Source5:           dropbear-keygen.service
BuildRequires:     gcc
# for gpg verification
BuildRequires:     gnupg2
BuildRequires:     libtomcrypt-devel
BuildRequires:     libtommath-devel
BuildRequires:     libxcrypt-devel
BuildRequires:     pam-devel
BuildRequires:     systemd
# For triggerun
Requires(post):    systemd-sysv
BuildRequires:     zlib-devel
BuildRequires:     make

%description
Dropbear is a relatively small SSH server and client. It's particularly useful
for "embedded"-type Linux (or other Unix) systems, such as wireless routers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build
%configure --enable-pam --disable-bundled-libtom

cat > localoptions.h <<EOT
#define SFTPSERVER_PATH "/usr/libexec/openssh/sftp-server"
EOT

%make_build

%install
%make_install
install -d %{buildroot}%{_sysconfdir}/%{name}
install -d %{buildroot}%{_unitdir}
install -pm644 %{S:4} %{buildroot}%{_unitdir}/%{name}.service
install -pm644 %{S:5} %{buildroot}%{_unitdir}/dropbear-keygen.service

%check
# Tests require local network and the running user to be able to login,
# not feasible with mock restrictions

%post
%systemd_post %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%preun
%systemd_preun %{name}.service

%triggerun -- dropbear < 0.55-2
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply dropbear
# to migrate them to systemd targets
systemd-sysv-convert --save dropbear >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
chkconfig --del dropbear >/dev/null 2>&1 || :
systemctl try-restart dropbear.service >/dev/null 2>&1 || :

%files
%doc CHANGES README.md
%license LICENSE
%dir %{_sysconfdir}/dropbear
%{_unitdir}/dropbear*
%{_bindir}/dropbearkey
%{_bindir}/dropbearconvert
%{_bindir}/dbclient
%{_sbindir}/dropbear
%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*

%changelog
%autochangelog
