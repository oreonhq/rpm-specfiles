%global source0_hash cf1e1e972cba0c56a365dcf496737f8f49959c5c80f0ca954f228a9ed43b8d3c
Name: evolution-rspam
Summary:        Evolution Plugin for reporting spam
Version: 0.6.0
Release:        1%{?dist}
License: GPL-2.0-or-later
Source0:        http://gnome.eu.org/%{name}-%{version}.tar.xz
URL: http://gnome.eu.org/evo/index.php/Report_as_Spam
Patch0: evolution-rspam-0.6.0-evo38.patch
Patch1: evolution-rspam-0.6.0-convert-fix.patch
Patch2: evolution-rspam-0.6.0-globals-clash.patch
Patch3: evolution-rspam-0.6.0-evo312.patch
Patch4: evolution-rspam-0.6.0-evo313.patch
Patch5: evolution-rspam-0.6.0-evo3136.patch
Patch6: evolution-rspam-0.6.0-source-double-unref.patch
Patch7: evolution-rspam-0.6.0-activity-leak.patch
Patch8: evolution-rspam-0.6.0-evo3_23_2.patch
Patch9: evolution-rspam-0.6.0-fix-po-charset.patch
Patch10: evolution-rspam-0.6.0-no-gtkuimanager.patch
Patch11: evolution-rspam-0.6.0-spamcop-flush-outbox-on-send.patch
Patch12: evolution-rspam-0.6.0-gcc-changes.patch
Patch13: evolution-rspam-0.6.0-drop-gconf-requirement.patch
Patch14: evolution-rspam-0.6.0-evo3_57_1.patch
Patch15: evolution-rspam-0.6.0-am_nls.patch
Requires: perl-Razor-Agent
Requires: pyzor
Requires: evolution >= 3.55.1
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  evolution-devel
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl(XML::Parser)
# /oreon:deps
%description
Rspam Evolution Plugin enables Evolution Mail client to report email messages
as spam to checksum-based and statistical filtering networks.
It supports Razor network, DCC, SpamCop and Pyzor.
This plugins requires a pretty new version of evolution to build.
See README for more information about required programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -name \*\.la -print | xargs rm -f
%find_lang rspam
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
