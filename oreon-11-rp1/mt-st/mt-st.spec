Summary: Tool for controlling tape drives
Name: mt-st
Version: 1.8
Release: 3%{?dist}
License: GPL-1.0-or-later
URL: https://github.com/iustin/mt-st
Source0: https://github.com/iustin/mt-st/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: stinit.service
# oreon url source checksums begin
%global source0_sha256 e0549f55185bfdc82220e6dd530a2470189dd8017ee109fe91867dc0d6ac43dd
%global source0_file mt-st-1.8.tar.gz
# oreon url source checksums end
BuildRequires: gcc
BuildRequires: make
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
The mt-st package contains the mt and st tape drive management
programs. Mt (for magnetic tape drives) and st (for SCSI tape devices)
can control rewinding, ejecting, skipping files and blocks and more.

Install mt-st if you need a tool to  manage tape drives.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/mt-st-1.8.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e0549f55185bfdc82220e6dd530a2470189dd8017ee109fe91867dc0d6ac43dd" || { echo "oreon: Source0 SHA256 mismatch for mt-st-1.8.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup


%build
make CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"


%install
COMPLETIONDIR=%{buildroot}%{bash_completions_dir}
%make_install EXEC_PREFIX=/usr COMPLETIONINSTALLDIR=$COMPLETIONDIR SBINDIR=%{buildroot}%{_bindir}
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/stinit.service
cd $COMPLETIONDIR
mv mt-st mt


%post
%systemd_post stinit.service

%preun
%systemd_preun stinit.service

%postun
%systemd_postun_with_restart stinit.service


%files
%doc COPYING README.md stinit.def.examples
%{_bindir}/mt
%{_bindir}/stinit
%{_mandir}/man1/mt.1*
%{_mandir}/man8/stinit.8*
%{_unitdir}/stinit.service
%{_datadir}/bash-completion/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8-3
- Prepare for Oreon 11 (RP1)
