%global source0_hash 7f76fe6e8a8588297179b3aed9cd2a3caa2cb709f8deaa81b8e23cccad06bf99
Summary:        Mail filter for Sender Policy Framework verification
Name:		smf-spf
Version:	2.5.1^20220423g061e937
Release:        9%{?dist}
License:	GPL-2.0-or-later
URL:		https://github.com/jcbf/smf-spf/
Source0:        https://github.com/jcbf/smf-spf/archive/061e9371f761f70afd40af349f4037fe0460725c.zip
Source1:	smf-spf.service
Source2:	README.rpm
Source3:	smf-spf.sysusers
Source4:	smfs.conf
Patch0:		smf-spf-2.5.1-Makefile.patch
Patch2:		smf-spf-2.5.1-conf.patch
Patch5:		smf-spf-2.5.1-rundir.patch
%{?sysusers_requires_compat}
Requires:	sendmail >= 8.12
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libspf2-devel
BuildRequires:  make
BuildRequires:  sendmail-milter-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
smf-spf is a lightweight, fast and reliable Sendmail milter that implements the
Sender Policy Framework technology with the help of the libspf2 library. It
checks SPF records to make sure that e-mail messages are authorized by the
domain that it is coming from. It's an alternative for the spfmilter,
spf-milter, and milter-spiff milters.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-061e9371f761f70afd40af349f4037fe0460725c/

# Copy in additional sources
install -m 0644 %{SOURCE1} .
install -m 0644 %{SOURCE2} .
install -m 0644 %{SOURCE3} .
install -m 0644 %{SOURCE4} .

%build

%make_build OPTFLAGS="-DSM_CONF_STDBOOL_H %{optflags}" LDFLAGS="%{build_ldflags} -lmilter -lpthread -lspf2"
%install
install -d -m 700 %{buildroot}/run/smfs
install -Dp -m 755 smf-spf %{buildroot}%{_sbindir}/smf-spf
install -Dp -m 644 smf-spf.conf %{buildroot}%{_sysconfdir}/mail/smfs/smf-spf.conf
install -Dp -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/smf-spf.service
install -Dp -m 644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/smfs.conf
install -m0644 -D %{SOURCE3} %{buildroot}%{_sysusersdir}/smfs.conf
: > %{buildroot}/run/smfs/smf-spf.sock
%oreon_autofiles main

%pre

%sysusers_create_compat %{SOURCE3}
%post

%systemd_post smf-spf.service
%preun

%systemd_preun smf-spf.service
%postun

%systemd_postun_with_restart smf-spf.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
