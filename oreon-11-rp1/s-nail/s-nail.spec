%global source1_hash a90c84f46469234f7bb508c644a69cdb9429d6831be2a4c74c7fc1794f35961b
%global source0_hash 20ff055be9829b69d46ebc400dfe516a40d287d7ce810c74355d6bdc1a28d8a9
Name:           s-nail
Version:        14.9.25
Release:        1%{?dist}
Summary:        Environment for sending and receiving mail, providing functionality of POSIX mailx
License:        ISC AND BSD-4-Clause-UC AND BSD-3-Clause AND HPND-sell-variant
URL:            https://www.sdaoden.eu/code.html#s-nail
Source0:        https://www.sdaoden.eu/downloads/%{name}-%{version}.tar.xz
Source1:        https://www.sdaoden.eu/downloads/%{name}-%{version}.tar.xz.asc
Source2:        steffen.asc
Patch0:		s-nail-makeflags.patch
Patch1:		s-nail-14.9.25-test-sha256.patch
Requires(pre):  %{_sbindir}/update-alternatives
Provides:       mailx = %{version}-%{release}
Obsoletes:      mailx < 12.6
Provides: /bin/mail
Provides: /bin/mailx
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  krb5-devel
BuildRequires:  libidn2-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
# /oreon:deps
%description
S-nail provides a simple and friendly environment for sending
and receiving mail. It is intended to provide the functionality
of the POSIX mailx(1) command, but is MIME capable and optionally offers
extensions for line editing, S/MIME, SMTP and POP3, among others.
S-nail divides incoming mail into its constituent messages and allows
the user to deal with them in any order. It offers many commands
and internal variables for manipulating messages and sending mail.
It provides the user simple editing capabilities to ease the composition
of outgoing messages, and increasingly powerful and reliable
non-interactive scripting capabilities.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -p1

cat <<EOF >>nail.rc

# Fedora-specific defaults
set bsdcompat
set noemptystart
set prompt='& '
EOF

%build

%make_build \
    CFLAGS="%{build_cflags}" \
    LDFLAGS="%{build_ldflags}" \
    OPT_AUTOCC=no \
    OPT_DEBUG=yes \
    OPT_NOMEMDBG=yes \
    OPT_DOTLOCK=no \
    VAL_PREFIX=%{_prefix} \
    VAL_SYSCONFDIR=%{_sysconfdir} \
    VAL_MAIL=%{_localstatedir}/mail \
    config
%make_build build
%install
%make_install
chmod 0755 %{buildroot}%{_bindir}/%{name}
for f in Mail mail mailx nail; do
    ln -s %{_bindir}/%{name} %{buildroot}%{_bindir}/$f
    ln -s %{_mandir}/man1/%{name}.1 %{buildroot}%{_mandir}/man1/$f.1
done
%oreon_autofiles main

%check

make test
%pre

%{_sbindir}/update-alternatives --remove-all mailx >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 14.9.25-4
- Prepare for Oreon 11 (RP1)
