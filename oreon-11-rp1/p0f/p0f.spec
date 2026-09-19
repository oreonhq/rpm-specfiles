%global source0_hash 543b68638e739be5c3e818c3958c3b124ac0ccb8be62ba274b4241dbdec00e7f

Name: p0f
Version: 3.09b
Release: 24%{?dist}

Summary: Versatile passive OS fingerprinting tool
License: LGPL-2.0-or-later
URL: http://lcamtuf.coredump.cx/p0f.shtml
Source: http://lcamtuf.coredump.cx/p0f3/releases/p0f-%{version}.tgz
# Fix up build script to use proper flags
Patch1: p0f-3.06b-compiler.patch
Patch2: p0f-configure-c99.patch
BuildRequires: make
BuildRequires: libpcap-devel
BuildRequires: gcc

%description
P0f is a versatile passive OS fingerprinting tool. P0f can identify the
system on machines that talk thru or near your box. p0f will also check
masquerading and firewall presence, the distance to the remote system and its
uptime, other guy's network hookup (DSL, OC3, avian carriers) and his ISP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -DFP_FILE=\"%{_sysconfdir}/p0f/p0f.fp\""

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_sbindir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/p0f
%{__cp} p0f $RPM_BUILD_ROOT%{_sbindir}
%{__cp} p0f.fp $RPM_BUILD_ROOT%{_sysconfdir}/p0f

# Build the tools
cd tools
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%{__cp} p0f-client p0f-sendsyn p0f-sendsyn6 $RPM_BUILD_ROOT%{_sbindir}

%files
%doc docs/*
%doc tools/README-TOOLS
%{_sbindir}/*
%dir %{_sysconfdir}/p0f
%config %{_sysconfdir}/p0f/p0f.fp

%changelog
%autochangelog
