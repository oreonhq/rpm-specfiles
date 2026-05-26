%global _generatorsdir %{_prefix}/lib/systemd/system-generators

Name:    vsftpd
Version: 3.0.5
Release: 15%{?dist}
Summary: Very Secure Ftp Daemon

# OpenSSL link exception
License:  GPL-2.0-only WITH vsftpd-openssl-exception
URL:      https://security.appspot.com/vsftpd.html
Source0:  https://security.appspot.com/downloads/%{name}-%{version}.tar.gz
Source1:  vsftpd.xinetd
Source2:  vsftpd.pam
Source3:  vsftpd.ftpusers
Source4:  vsftpd.user_list
Source6:  vsftpd_conf_migrate.sh
Source7:  vsftpd.service
Source8:  vsftpd@.service
Source9:  vsftpd.target
Source10: vsftpd-generator
Source11: vsftpd-tmpfiles.conf

BuildRequires: make
BuildRequires: pam-devel
BuildRequires: libcap-devel
BuildRequires: openssl-devel
BuildRequires: systemd
BuildRequires: git
BuildRequires: gcc

Requires: logrotate

Patch1:  0001-Don-t-use-the-provided-script-to-locate-libraries.patch
Patch2:  0002-Enable-build-with-SSL.patch
Patch3:  0003-Enable-build-with-TCP-Wrapper.patch
Patch4:  0004-Use-etc-vsftpd-dir-for-config-files-instead-of-etc.patch
Patch5:  0005-Use-hostname-when-calling-PAM-authentication-module.patch
Patch6:  0006-Close-stdin-out-err-before-listening-for-incoming-co.patch
Patch7:  0007-Make-filename-filters-smarter.patch
Patch8:  0008-Write-denied-logins-into-the-log.patch
Patch9:  0009-Trim-whitespaces-when-reading-configuration.patch
Patch10: 0010-Improve-daemonizing.patch
Patch11: 0011-Fix-listing-with-more-than-one-star.patch
Patch12: 0012-Replace-syscall-__NR_clone-.-with-clone.patch
Patch13: 0013-Extend-man-pages-with-systemd-info.patch
Patch14: 0014-Add-support-for-square-brackets-in-ls.patch
Patch15: 0015-Listen-on-IPv6-by-default.patch
Patch16: 0016-Increase-VSFTP_AS_LIMIT-from-200UL-to-400UL.patch
Patch17: 0017-Fix-an-issue-with-timestamps-during-DST.patch
Patch18: 0018-Change-the-default-log-file-in-configuration.patch
Patch19: 0019-Introduce-reverse_lookup_enable-option.patch
Patch20: 0020-Use-unsigned-int-for-uid-and-gid-representation.patch
Patch21: 0021-Introduce-support-for-DHE-based-cipher-suites.patch
Patch22: 0022-Introduce-support-for-EDDHE-based-cipher-suites.patch
Patch23: 0023-Add-documentation-for-isolate_-options.-Correct-defa.patch
Patch24: 0024-Introduce-new-return-value-450.patch
Patch25: 0025-Improve-local_max_rate-option.patch
Patch26: 0026-Prevent-hanging-in-SIGCHLD-handler.patch
Patch27: 0027-Delete-files-when-upload-fails.patch
Patch28: 0028-Fix-man-page-rendering.patch
Patch29: 0029-Fix-segfault-in-config-file-parser.patch
Patch30: 0030-Fix-logging-into-syslog-when-enabled-in-config.patch
Patch31: 0031-Fix-question-mark-wildcard-withing-a-file-name.patch
Patch32: 0032-Propagate-errors-from-nfs-with-quota-to-client.patch
Patch34: 0034-Turn-off-seccomp-sandbox-because-it-is-too-strict.patch
Patch36: 0036-Redefine-VSFTP_COMMAND_FD-to-1.patch
Patch37: 0037-Document-the-relationship-of-text_userdb_names-and-c.patch
Patch38: 0038-Document-allow_writeable_chroot-in-the-man-page.patch
Patch39: 0039-Improve-documentation-of-ASCII-mode-in-the-man-page.patch
Patch40: 0040-Use-system-wide-crypto-policy.patch
Patch41: 0041-Document-the-new-default-for-ssl_ciphers-in-the-man-.patch
Patch42: 0042-When-handling-FEAT-command-check-ssl_tlsv1_1-and-ssl.patch
Patch44: 0044-Disable-anonymous_enable-in-default-config-file.patch
Patch45: 0045-Expand-explanation-of-ascii_-options-behaviour-in-ma.patch
Patch46: 0046-vsftpd.conf-Refer-to-the-man-page-regarding-the-asci.patch
Patch47: 0047-Disable-tcp_wrappers-support.patch
Patch48: 0048-Fix-default-value-of-strict_ssl_read_eof-in-man-page.patch
Patch49: 0049-Add-new-filename-generation-algorithm-for-STOU-comma.patch
Patch50: 0050-Don-t-link-with-libnsl.patch
Patch51: 0051-Improve-documentation-of-better_stou-in-the-man-page.patch
Patch52: 0052-Fix-rDNS-with-IPv6.patch
Patch53: 0053-Always-do-chdir-after-chroot.patch
Patch54: 0054-vsf_sysutil_rcvtimeo-Check-return-value-of-setsockop.patch
Patch55: 0055-vsf_sysutil_get_tz-Check-the-return-value-of-syscall.patch
Patch56: 0056-Log-die-calls-to-syslog.patch
Patch57: 0057-Improve-error-message-when-max-number-of-bind-attemp.patch
Patch58: 0058-Make-the-max-number-of-bind-retries-tunable.patch
Patch59: 0059-Fix-SEGFAULT-when-running-in-a-container-as-PID-1.patch
Patch61: 0001-Move-closing-standard-FDs-after-listen.patch
Patch62: 0002-Prevent-recursion-in-bug.patch
Patch63: 0001-Set-s_uwtmp_inserted-only-after-record-insertion-rem.patch
Patch64: 0002-Repeat-pututxline-if-it-fails-with-EINTR.patch
Patch65: 0001-Repeat-pututxline-until-it-succeeds-if-it-fails-with.patch
Patch67: 0001-Fix-timestamp-handling-in-MDTM.patch
Patch68: 0002-Drop-an-unused-global-variable.patch
Patch69: 0001-Remove-a-hint-about-the-ftp_home_dir-SELinux-boolean.patch
Patch70: fix-str_open.patch
Patch71: vsftpd-3.0.5-enable_wc_logs-replace_unprintable_with_hex.patch
Patch72: vsftpd-3.0.5-replace-old-network-addr-functions.patch
Patch73: vsftpd-3.0.5-replace-deprecated-openssl-functions.patch
Patch74: vsftpd-3.0.5-add-option-for-tlsv1.3-ciphersuites.patch
Patch75: vsftpd-3.0.5-use-old-tlsv-options.patch
Patch76: 0076-Correct-the-definition-of-setup_bio_callbacks-in-ssl.patch
# oreon url source checksums begin
%global source0_sha256 26b602ae454b0ba6d99ef44a09b6b9e0dfa7f67228106736df1f278c70bc91d3
%global source0_file vsftpd-3.0.5.tar.gz
# oreon url source checksums end

%description
vsftpd is a Very Secure FTP daemon. It was written completely from
scratch.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/vsftpd-3.0.5.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "26b602ae454b0ba6d99ef44a09b6b9e0dfa7f67228106736df1f278c70bc91d3" || { echo "oreon: Source0 SHA256 mismatch for vsftpd-3.0.5.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -S git
cp %{SOURCE1} .

%build

%ifarch s390x sparcv9 sparc64
%make_build CFLAGS="$RPM_OPT_FLAGS -fPIE -pipe -Wextra -Werror" \
%else
%make_build CFLAGS="$RPM_OPT_FLAGS -fpie -pipe -Wextra -Werror" \
%endif
        LINK="-pie -lssl $RPM_LD_FLAGS" %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/{vsftpd,pam.d,logrotate.d}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{5,8}
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_generatorsdir}
install -m 755 vsftpd  $RPM_BUILD_ROOT%{_bindir}/vsftpd
install -m 600 vsftpd.conf $RPM_BUILD_ROOT%{_sysconfdir}/vsftpd/vsftpd.conf
install -m 644 vsftpd.conf.5 $RPM_BUILD_ROOT/%{_mandir}/man5/
install -m 644 vsftpd.8 $RPM_BUILD_ROOT/%{_mandir}/man8/
install -m 644 RedHat/vsftpd.log $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/vsftpd
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/vsftpd
install -m 600 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/vsftpd/ftpusers
install -m 600 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/vsftpd/user_list
install -m 744 %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/vsftpd/vsftpd_conf_migrate.sh
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_unitdir}
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_unitdir}
install -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_unitdir}
install -m 755 %{SOURCE10} $RPM_BUILD_ROOT%{_generatorsdir}
install -Dpm 644 %{SOURCE11} $RPM_BUILD_ROOT%{_tmpfilesdir}/vsftpd.conf
                            
mkdir -p $RPM_BUILD_ROOT/%{_var}/ftp/pub

%post
%systemd_post vsftpd.service

%preun
%systemd_preun vsftpd.service
%systemd_preun vsftpd.target

%postun
%systemd_postun_with_restart vsftpd.service 

%files
%{_unitdir}/*
%{_generatorsdir}/*
%{_bindir}/vsftpd
%dir %{_sysconfdir}/vsftpd
%{_sysconfdir}/vsftpd/vsftpd_conf_migrate.sh
%config(noreplace) %{_sysconfdir}/vsftpd/ftpusers
%config(noreplace) %{_sysconfdir}/vsftpd/user_list
%config(noreplace) %{_sysconfdir}/vsftpd/vsftpd.conf
%config(noreplace) %{_sysconfdir}/pam.d/vsftpd
%config(noreplace) %{_sysconfdir}/logrotate.d/vsftpd
%doc FAQ INSTALL BUGS AUDIT Changelog LICENSE README README.security REWARD
%doc SPEED TODO BENCHMARKS COPYING SECURITY/ EXAMPLE/ TUNING SIZE vsftpd.xinetd
%{_mandir}/man5/vsftpd.conf.*
%{_mandir}/man8/vsftpd.*
%{_var}/ftp
%{_tmpfilesdir}/vsftpd.conf

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.5-15
- Prepare for Oreon 11 (RP1)
