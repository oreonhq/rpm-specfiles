%global source0_hash 4bf085e5122ccc0f2a72c749aac8a94fb94211ae8b4f6fd525e58afb27ed8f18

%global shortname obs-sign
# http://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#PIE
%global _hardened_build 1
%global commit 5c320501dc048bbcf56480dfc5780fb43dd20de5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapdate 20210907
%global snapshotrel .%{snapdate}git%{shortcommit}
# To make rpmdev-bumpspec work properly
%global baserelease 10

Name:             obs-signd
Summary:          The OBS sign daemon
License:          GPL-2.0-only
URL:              https://github.com/openSUSE/obs-sign
Version:          2.8.4
Release:          %autorelease
#Release:          %%{baserelease}%%{?snapshotrel}%%{?dist}
Source0:          https://github.com/openSUSE/%{shortname}/archive/refs/tags/%{version}.tar.gz#/%{shortname}-%{version}.tar.gz
# We renamed the option in gnupg2 to 'file-is-digest'
Patch0:           0001-Rename-option-files-are-digests-to-file-is-digest.patch
# https://github.com/openSUSE/obs-sign/pull/6
Patch1:           0002-fixes-user-id-matching-to-provide-unique-results.patch
Requires:         gnupg2
BuildRequires:    perl-generators
BuildRequires:    systemd
BuildRequires:    gcc
BuildRequires:    make

%description
The OpenSUSE Build Service sign client and daemon.

This daemon can be used to sign anything via gpg by communicating
with a remote server to avoid the need to host the private key
on the same server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{shortname}-%{version}

# Create a sysusers.d config file
cat >obs-signd.sysusers.conf <<EOF
u obsrun - 'User for Open Build Service backend' %{_libdir}/obs /bin/false
EOF

%build
%make_build CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" sign

%install
mkdir -p %{buildroot}%{_sbindir} %{buildroot}%{_sysconfdir}
install -d -m 0755 %{buildroot}%{_bindir}

# binaries and configuration
mkdir -p %{buildroot}%{_sbindir} %{buildroot}%{_bindir} %{buildroot}%{_sysconfdir}
install -m 0755 signd %{buildroot}%{_sbindir}
install -m 0750 sign %{buildroot}%{_bindir}
install -m 0644 sign.conf %{buildroot}%{_sysconfdir}

# systemd service
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 dist/signd.service %{buildroot}%{_unitdir}

# man pages
install -d -m 0755 %{buildroot}%{_mandir}/man{5,8}

for f in 5 8; do
  install -m 0644 sig*.${f} %{buildroot}%{_mandir}/man${f}/
done

install -m0644 -D obs-signd.sysusers.conf %{buildroot}%{_sysusersdir}/obs-signd.conf

%post
%systemd_post signd.service

%preun
%systemd_preun signd.service

%postun
%systemd_postun_with_restart signd.service

%files
%config(noreplace) %{_sysconfdir}/sign.conf
%attr(4750,root,obsrun) %{_bindir}/sign
%{_sbindir}/signd
%{_unitdir}/signd.service
%doc %{_mandir}/man*/*
%{_sysusersdir}/obs-signd.conf

%changelog
%autochangelog
