%global source0_hash af2b89bc974060bfb2c5683bd9d905312075d4227456ddafbcb0b280b5451a7f
%global upstreamversion 2024-07
Name:           picocom
Version:        2024.07
Release:        1%{?dist}
Summary:        Minimal serial communications program
License:        GPL-2.0-or-later
URL:            https://gitlab.com/wsakernel/picocom/
Source0:        https://gitlab.com/wsakernel/%{name}/-/archive/%{upstreamversion}/%{name}-%{upstreamversion}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  golang-github-cpuguy83-md2man
BuildRequires:  make
# /oreon:deps
%description
As its name suggests, [picocom] is a minimal dumb-terminal emulation
program. It is, in principle, very much like minicom, only it's "pico"
instead of "mini"! It was designed to serve as a simple, manual, modem
configuration, testing, and debugging tool. It has also served (quite
well) as a low-tech "terminal-window" to allow operator intervention
in PPP connection scripts (something like the ms-windows "open
terminal window before / after dialing" feature).  It could also prove
useful in many other similar tasks. It is ideal for embedded systems
since its memory footprint is minimal (less than 20K, when
stripped).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{upstreamversion}

# Create a sysusers.d config file
cat >picocom.sysusers.conf <<EOF
g dialout 18
EOF

%build

make CC="%{__cc}" CFLAGS="$RPM_OPT_FLAGS -DUSE_CUSTOM_BAUD" %{_smp_mflags} UUCP_LOCK_DIR=/run/lock/picocom
make doc
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 picocom $RPM_BUILD_ROOT%{_bindir}/
install -m 644 picocom.1 $RPM_BUILD_ROOT%{_mandir}/man1/
mkdir -p $RPM_BUILD_ROOT/run/lock/picocom
install -m0644 -D picocom.sysusers.conf %{buildroot}%{_sysusersdir}/picocom.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
