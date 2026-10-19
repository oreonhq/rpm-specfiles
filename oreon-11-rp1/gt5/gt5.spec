%global source0_hash 785a2a71f77e29d2cf4bbd2c6f49f690d6fdcb5f53abd51aee393572fd7fa03e
Name:		gt5
Summary:        A diff-capable 'du-browser'
Version:	1.4.0
Release:        1%{?dist}
License:	GPL-1.0-or-later
URL:		http://gt5.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		gt5-1.4.0-fix-max-depth.diff
BuildArch:	noarch
Requires:	gawk
Requires:	sed
Requires:	text-www-browser
# oreon:deps

# /oreon:deps
%description
Allows to check what takes the most of your hard disk space and track
its changes.
Note: It requires some console web browser installed in the system
(e.g. links, links2, elinks, lynx, w3m).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0

%build

%install
rm -fr %{buildroot}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -p gt5 %{buildroot}%{_bindir}/
install -p gt5.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
