%global source0_hash 1bbdc24aed0b43855332dccc2419165bd91952fe4b9eb4c8664a7d9ec10aac41

%global commit  44ff753f51d1a767b8d71b04e882847664d9f0c8

Summary:        Generic IMAP server compliancy tester
Name:           imaptest
# Upstream is not really planning on adding version numbers
Version:        20250509
Release:        2%{?dist}
License:        MIT
URL:            https://dovecot.github.io/imaptest/
Source0:        https://github.com/dovecot/imaptest/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:         https://github.com/dovecot/imaptest/commit/39d3dcc8f8ae4e7e751cb0ba633301630e32f54e.patch#/imaptest-20250520-so-file.patch
BuildRequires:  dovecot-devel >= 2.4.1
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
# dovecot-devel.i686 was removed with dovecot-2.3.21-7.fc41
%if 0%{?fedora} || 0%{?rhel} > 9
ExcludeArch:    %{ix86}
%endif

%description
ImapTest is a generic IMAP server compliancy tester that works with all IMAP
servers. It supports stress testing with state tracking, scripted testing and
benchmarking. When stress testing with state tracking ImapTest sends random
commands to the server and verifies that server's output looks correct. Using
the scripted testing ImapTest runs a list of predefined scripted tests and
verifies that server returns expected output.

Examples and details are provided online at: https://www.imapwiki.org/ImapTest

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{commit} -p1
autoreconf -i

# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1103927#c4 (and later)
sed -e 's@\(^LIBDOVECOT .*\)@\1 -Wl,-rpath -Wl,%{_libdir}/dovecot@' -i src/Makefile.in

%build
%configure --with-dovecot=%{_libdir}/dovecot
%make_build

%install
%make_install

# Copy test files for later shipping
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/
cp -pr src/tests/ $RPM_BUILD_ROOT%{_datadir}/%{name}/

%check
$RPM_BUILD_ROOT%{_bindir}/%{name} --help

%files
%license COPYING COPYING.MIT
%doc AUTHORS profile.conf pop3-profile.conf
%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20250509-2
- Prepare for Oreon 11 (RP1)
