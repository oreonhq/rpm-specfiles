%global source0_hash 785a2a71f77e29d2cf4bbd2c6f49f690d6fdcb5f53abd51aee393572fd7fa03e

Name:		gt5
Summary:	A diff-capable 'du-browser'
Version:	1.4.0
Release:	37%{?dist}
License:	GPL-1.0-or-later
URL:		http://gt5.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		gt5-1.4.0-fix-max-depth.diff
BuildArch:	noarch
#something else is required in runtime?
Requires:	gawk
#sed is not needed to mention only in BuildRequires
Requires:	sed
#Some console web browser is required (e.g. links links2 elinks lynx w3m)
Requires:	text-www-browser

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
#it's a shell-script, nothing to do

%install
rm -fr %{buildroot}
#make install requires a patch to drop out chown root:root,
#it was suggested to use install -p instead of
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -p gt5 %{buildroot}%{_bindir}/
install -p gt5.1 %{buildroot}%{_mandir}/man1/

%files
%attr(0755,root,root) %{_bindir}/gt5
#INSTALL is not needed
%doc README LICENSE Changelog
%{_mandir}/man1/gt5.1*

%changelog
%autochangelog
