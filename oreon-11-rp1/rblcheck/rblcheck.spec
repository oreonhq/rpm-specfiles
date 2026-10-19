%global source0_hash c0f28cb0ec215ce2244e2a2008dac76bb6426adf0804f53c6784e6baeec13a47
Name:		rblcheck
Summary:        Command-line interface to RBL-style listings
Version:	1.5
Release:        1%{?dist}
Source0:        https://github.com/logic/rblcheck/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:	rblcheckrc
License:	GPL-2.0-or-later
URL:		https://github.com/logic/rblcheck
Patch0:		rblcheck-texttweak.patch
Patch1:		rblcheck-txt.patch
Patch2:		rblcheck-names.patch
Patch3:		rblcheck-1.5-res_query.patch
Patch4:		rblcheck-configure-c99.patch
# oreon:deps
BuildRequires:  docbook-utils
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
