%global source0_hash 917f7ef67bcf60553438d9e7c95f4ddcebc91d9693159539e2d5338733580d5f

Summary:	Mail filter for Sender Policy Framework verification
Name:		smf-spf
Version:	2.5.1^20220423g061e937
Release:	9%{?dist}
License:	GPL-2.0-or-later
URL:		https://github.com/jcbf/smf-spf/
Source0:	https://github.com/jcbf/smf-spf/archive/061e9371f761f70afd40af349f4037fe0460725c.zip
Source1:	smf-spf.service
Source2:	README.rpm
Source3:	smf-spf.sysusers
Source4:	smfs.conf

# Use the distribution optimization flags and don't strip the binary,
# so we get usable debuginfo
Patch0:		smf-spf-2.5.1-Makefile.patch

# Tag failing messages by default rather than rejecting them
Patch2:		smf-spf-2.5.1-conf.patch

# Use /run rather than /var/run with systemd
Patch5:		smf-spf-2.5.1-rundir.patch

BuildRequires:	libspf2-devel >= 1.2.5
BuildRequires:	sendmail-milter-devel >= 8.12
BuildRequires:	systemd-rpm-macros
BuildRequires:	make gcc coreutils
%{?sysusers_requires_compat}

Requires:	sendmail >= 8.12

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
# Install systemd unit file and tmpfiles.d configuration for /run/smfs
install -Dp -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/smf-spf.service
install -Dp -m 644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/smfs.conf
install -m0644 -D %{SOURCE3} %{buildroot}%{_sysusersdir}/smfs.conf

# Create dummy socket for %%ghost-ing
: > %{buildroot}/run/smfs/smf-spf.sock

%pre
%sysusers_create_compat %{SOURCE3}

%post
%systemd_post smf-spf.service

%preun
%systemd_preun smf-spf.service

%postun
%systemd_postun_with_restart smf-spf.service

%files
%doc ChangeLog readme README.rpm
%license COPYING
%{_sbindir}/smf-spf
%dir %{_sysconfdir}/mail/smfs/
%config(noreplace) %{_sysconfdir}/mail/smfs/smf-spf.conf
%attr(0700,smfs,smfs) %dir /run/smfs/
%ghost %attr(0600,smfs,smfs) /run/smfs/smf-spf.sock
%{_unitdir}/smf-spf.service
%{_tmpfilesdir}/smfs.conf
%{_sysusersdir}/smfs.conf

%changelog
%autochangelog
