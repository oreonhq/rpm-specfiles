%global source0_hash a2e840f82590690d27ea1ea1141af509ee34681fede897e58ae8d354701ce71b

Name:           zssh
Version:        1.5c
Release:        21%{?dist}
Summary:        SSH and Telnet client with ZMODEM file transfer capability
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://zssh.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/zssh/zssh/1.5/%{name}-%{version}.tgz
# patches from https://sources.debian.org/patches/zssh/1.5c.debian.1-7/
Patch0:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0001-Remove-build-instruction-about-lrzsz.patch
Patch1:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0002-Install-files-into-under-DESTDIR.patch
Patch2:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0003-Do-not-symlink-zssh-to-ztelnet.patch
Patch3:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0004-Use-GNU-openpty-library-for-pty.h.patch
Patch4:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0005-Do-not-call-strip-in-build-process.patch
Patch5:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0006-replace-CPPFunction-call-with-rl_completion_func_t.patch
Patch6:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0007-Fix-typo-in-man-page-zssh.1.patch
Patch7:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0008-Strip-build-date-from-version-string-to-enable-repro.patch
Patch8:         zssh-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  autoconf
Requires:       lrzsz

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# remove bundled lrzsz
rm -fr lrzsz-0.12.20

%build
autoconf
%configure
%make_build

%install
mkdir -p %{buildroot}%{_bindir}/ %{buildroot}%{_mandir}/man1/
%make_install
rm %{buildroot}%{_mandir}/man1/ztelnet.1*

%files
%doc README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
