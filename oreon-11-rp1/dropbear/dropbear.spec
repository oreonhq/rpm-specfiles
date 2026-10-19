%global source2_hash 143397f47ae71f4ec87c3594a18ff42c7b767113f4c566e08876a29db6dddb9a
%global source1_hash e5971e62ee25f3cce66a09bf5ab2411e76c258b960be832159473f3395116695
%global source0_hash e098034a843699200c8c977a991fff73159735bf795d5f72ef672c41a6b1ae81
Name:              dropbear
Version:           2026.94
Release:        1%{?dist}
Summary:        Lightweight SSH server and client
License:           MIT
URL:               https://matt.ucc.asn.au/dropbear/dropbear.html
Source0:        https://matt.ucc.asn.au/%{name}/releases/%{name}-%{version}.tar.bz2
Source1:           https://matt.ucc.asn.au/%{name}/releases/%{name}-%{version}.tar.bz2.asc
Source2:           https://matt.ucc.asn.au/dropbear/releases/dropbear-key-2015.asc
Source4:           dropbear.service
Source5:           dropbear-keygen.service
Requires(post):    systemd-sysv
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libtomcrypt-devel
BuildRequires:  libtommath-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
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
EOT
%make_build
%install
%make_install
install -d %{buildroot}%{_sysconfdir}/%{name}
install -d %{buildroot}%{_unitdir}
install -pm644 %{S:4} %{buildroot}%{_unitdir}/%{name}.service
install -pm644 %{S:5} %{buildroot}%{_unitdir}/dropbear-keygen.service
%oreon_autofiles main

%check

%post

%systemd_post %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%preun

%systemd_preun %{name}.service
%triggerun -- dropbear < 0.55-2

systemd-sysv-convert --save dropbear >/dev/null 2>&1 ||:
chkconfig --del dropbear >/dev/null 2>&1 || :
systemctl try-restart dropbear.service >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
