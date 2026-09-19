%global source0_hash 8497a8b1028001df684c7fce2820898a30fb39938a467216477c5401dcb9476e

Name:           lumail
Version:        3.1
Release:        21%{?dist}
Summary:        Modern console-based e-mail client

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://lumail.org/
Source0:        https://lumail.org/download/%{name}-%{version}.tar.gz
# Upstream https://github.com/lumail/lumail/commit/16c437fd6
Patch0:         0001-Makefile-fix-Makefile-installation-re-introduce-DEST.patch
# Upstream https://github.com/lumail/lumail/commit/929c21b96
Patch1:         0002-Makefile-allow-changing-CPPFLAGS.patch

Patch2:         https://github.com/lumail/lumail/commit/fe9337e.patch#/0001-imap_proxy-terminate-the-proxy-child-on-failure-to-e.patch
Patch3:         https://github.com/lumail/lumail/commit/ddd4078.patch#/0002-global_state-include-the-response-from-the-IMAP-prox.patch
Patch4:         https://github.com/lumail/lumail/commit/1edffc9.patch#/0003-imap_proxy-spin-for-10-seconds-for-the-IMAP-proxy-so.patch
Patch5:         https://github.com/lumail/lumail/commit/05079ed.patch#/0004-perl-imap-proxy-avoid-calling-a-noop-on-an-empty-han.patch
Patch6:         https://github.com/lumail/lumail/commit/9650e8b.patch#/0005-perl-imap-proxy-croak-early-on-bad-params.patch
Patch7:         lumail-3.1-lua54.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(gmime-2.6)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pcre-devel
BuildRequires:  file-devel

%description
Lumail is a modern console-based email-client, with fully integrated
scripting, implemented in the Lua programming language.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1

%build
make %{?_smp_mflags} CPPFLAGS="%{optflags}" LVER=lua

%install
%make_install

%files
%{_sysconfdir}/lumail
%config(noreplace) %{_sysconfdir}/lumail/lumail.lua
%{_prefix}/lib/lumail
%{_bindir}/lumail2
%{_datadir}/lumail
%doc *.md
%license LICENSE

%changelog
%autochangelog
