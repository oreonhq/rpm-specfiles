%global source0_hash c0f28cb0ec215ce2244e2a2008dac76bb6426adf0804f53c6784e6baeec13a47

# $Id: rblcheck.spec,v 1.16 2005/07/01 10:41:31 oliver Exp $

Name:		rblcheck
Summary:	Command-line interface to RBL-style listings

Version:	1.5
Release:	51%{?dist}

Source0:	https://github.com/logic/rblcheck/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:	rblcheckrc

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/logic/rblcheck

# Change the text "RBL filtered by" to "listed by"
# (RBL is a trademark of MAPS LLC.)
# 'listed by' is more accurate
Patch0:		rblcheck-texttweak.patch

# Fix broken code for looking up TXT records, code borrowed
# from Ian Gulliver's "firedns" library (GPL), which can be found at:
# http://firestuff.org/
Patch1:		rblcheck-txt.patch

# Comes from a post to the rblcheck users mailing list. See:
# http://sourceforge.net/mailarchive/forum.php?thread_id=1371771&forum_id=4256
Patch2:		rblcheck-names.patch

# Compile fix for x86_64 systems
Patch3:		rblcheck-1.5-res_query.patch

Patch4:		rblcheck-configure-c99.patch

BuildRequires: make
BuildRequires:	docbook-utils, gcc

%description
rblcheck is a very basic interface to RBL-style DNS listings such as those
operated by the MAPS (http://www.mail-abuse.org/) and ORBL
(http://www.orbl.org/) projects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p1 -b .texttweak
%patch -P1 -p0 -b .txt
%patch -P2 -p0 -b .names
%patch -P3 -p1 -b .res_query
%patch -P4 -p1 -b .c99

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%{__install} -D -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rblcheckrc

%files
%doc AUTHORS ChangeLog NEWS README COPYING
%doc docs/rblcheck.ps docs/rblcheck.rtf docs/html/
%{_bindir}/rbl
%{_bindir}/rblcheck
%config(noreplace) %{_sysconfdir}/rblcheckrc

%changelog
%autochangelog
