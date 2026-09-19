%global source0_hash 0d931dddb3744ed38aa2d319dd2d8a2f38a391011ff99db68ce7c83ab8f5b62f

Name:           pastebinit
Version:        1.5
Release:        20%{?dist}
Summary:        Send anything you want directly to a pastebin from the command line

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://launchpad.net/pastebinit
Source0:        http://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz

#
# supress useless dependancy to lsb_release, folow the comportement of
# upstream by using per default fpaste.org.
# this patch musn't be push to the upstream
#
Patch0:         %{name}-1.5-delete-dependancy-to-lsb_release.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  docbook-style-xsl libxslt gettext

%description
A software that lets you send anything you want directly to a
pastebin from the command line.  This software lets you send a file
or simply the result of a command directly to the pastebin you want
(if it's supported) and gives you the URL in return.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
# Change the location of pastebin config file from /etc/pastebin.d/
# to /usr/share/pastebinit/ (unappropriate dir. name "pastebinit.d"
# + FHS)
# See https://bugs.launchpad.net/pastebinit/+bug/621923
#
sed -i "s|pastebin.d|%{name}|g" %{name} README

%build
# Generate the man page from docbook xml
xsltproc -''-nonet %{_datadir}/sgml/docbook/xsl-stylesheets*/manpages/docbook.xsl pastebinit.xml

# Build translation
pushd po
make
popd

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/

cp -a pastebin.d %{buildroot}%{_datadir}
mv %{buildroot}%{_datadir}/pastebin.d/ %{buildroot}%{_datadir}/%{name}/

install -m 0755 -D -p %{name} %{buildroot}%{_bindir}/%{name}
install -m 0644 -D -p %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# Install translations
pushd po
cp -a mo %{buildroot}%{_datadir}/locale/
popd

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/%{name}/
%dir %{_sysconfdir}/%{name}/
%doc README COPYING

%changelog
%autochangelog
