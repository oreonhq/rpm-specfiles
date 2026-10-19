%global source2_hash 67c51aab37441f2827b52855366b2dd5912ce3722209be91de9dae736d7a47ba
%global source1_hash 0afe03d690db4b92c799c9522fdf52cba41f572a116e5cae16c5f58dddd59092
%global source0_hash 91df2ed7faca0716bbd726a17d6467ed92fcb2b6e45b57d9e619f9686ab99e1b
%global source2_key_fpr 11ACBA4F4778E3F6E4EDF38EB27B944E34884E85
Name: radvd
Version: 2.21
Release:        1%{?dist}
Summary:        A Router Advertisement daemon
License: radvd
URL: https://radvd.litech.org
Source0:        https://github.com/radvd-project/radvd/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/radvd-project/radvd/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://github.com/robbat2.gpg
Source3: radvd.sysusers
%{?systemd_requires}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  check-devel
BuildRequires:  flex
BuildRequires:  flex-static
BuildRequires:  gcc
BuildRequires:  gpgverify
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
radvd is the router advertisement daemon for IPv6.  It listens to router
solicitations and sends router advertisements as described in "Neighbor
Discovery for IP Version 6 (IPv6)" (RFC 2461).  With these advertisements
hosts can automatically configure their addresses and some other
parameters.  They also can choose a default router based on these
advertisements.

Install radvd if you are setting up IPv6 network and/or Mobile IPv6
services.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

for F in CHANGES; do
    iconv -f iso-8859-1 -t utf-8 < "$F" > "${F}.new"
    touch -r "$F" "${F}.new"
    mv "${F}.new" "$F"
done

%build

autoreconf -fiv
export CFLAGS="$RPM_OPT_FLAGS -fPIE " 
export LDFLAGS='-pie -Wl,-z,relro,-z,now,-z,noexecstack,-z,nodlopen'
%configure \
    --with-check \
    --disable-silent-rules \
    --with-pidfile=/run/radvd/radvd.pid
%make_build 
%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}/run/radvd
mkdir -p %{buildroot}%{_unitdir}
install -m 644 redhat/SysV/radvd.conf.empty %{buildroot}%{_sysconfdir}/radvd.conf
install -m 644 redhat/SysV/radvd.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/radvd
install -d -m 755 %{buildroot}%{_tmpfilesdir}
install -p -m 644 redhat/systemd/radvd-tmpfs.conf %{buildroot}%{_tmpfilesdir}/radvd.conf
install -m 644 redhat/systemd/radvd.service %{buildroot}%{_unitdir}
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/radvd.conf
%oreon_autofiles main

%check

make check
%postun

%systemd_postun_with_restart radvd.service
%post

%systemd_post radvd.service
%preun

%systemd_preun radvd.service
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.20-1
- Prepare for Oreon 11 (RP1)
