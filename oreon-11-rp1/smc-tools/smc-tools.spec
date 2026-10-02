%global source0_hash 197da900aa08f60cb7c541241746771e90a1c1eb8e8e962241e3532d7fc334e5

Name:           smc-tools
Version:        1.8.8
Release:        1%{?dist}
Summary:        Shared Memory Communication Tools

License:        EPL-1.0
URL:            https://github.com/ibm-s390-linux/smc-tools
Source0:        https://github.com/ibm-s390-linux/smc-tools/archive/refs/tags/1.8.8.tar.gz#/smc-tools-1.8.7.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libnl3-devel
BuildRequires:  pkgconfig(bash-completion)

%ifarch s390 s390x
# for smc_chk
Requires:       python3
Requires:       man
%endif


%description
The Shared Memory Communication Tools (smc-tools) package enables usage of SMC
sockets in Linux.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup


%build
%ifarch ppc64le
# see arch/powerpc/include/uapi/asm/types.h
%global optflags %optflags -D__SANE_USERSPACE_TYPES__
%endif
%set_build_flags
%make_build


%install
%make_install V=1


%files
%license LICENSE
%doc README.md
%{_bindir}/smcd
%{_bindir}/smcr
%{_bindir}/smc_dbg
%{_bindir}/smc_pnet
%{_bindir}/smc_run
%{_bindir}/smcss
%{_libdir}/libsmc-preload.so*
%{_mandir}/man7/af_smc.7*
%{_mandir}/man8/smcd*.8*
%{_mandir}/man8/smcr*.8*
%{_mandir}/man8/smc_pnet.8*
%{_mandir}/man8/smc_run.8*
%{_mandir}/man8/smcss.8*
%ifarch s390 s390x
%{_bindir}/smc_chk
%{_bindir}/smc_rnics
%{_mandir}/man8/smc_chk.8*
%{_mandir}/man8/smc_rnics.8*
%endif
%{_datadir}/bash-completion/


%changelog
%autochangelog
