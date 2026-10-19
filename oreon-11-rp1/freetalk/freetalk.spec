%global source1_hash 97d2cf2cc55a3dc40f09c4f089ca9fba7cd4670ddca35afef2e36649b0c9f616
%global source0_hash bb5b4f29a706af2f891987802200e26b737bcece44338172419755f1eee1b580
Name:           freetalk
Version:        4.2
Release:        1%{?dist}
Summary:        Terminal XMPP client
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/freetalk/
Source0:        http://ftp.gnu.org/gnu/freetalk/freetalk-4.2.tar.gz
Source1:        http://ftp.gnu.org/gnu/freetalk/freetalk-4.2.tar.gz.sig
Source2:        freetalk-keyring.gpg
Requires:  words
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  guile30-devel
BuildRequires:  loudmouth-devel
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  texinfo
# /oreon:deps
%description
GNU Freetalk is a console based chat client for Jabber and other XMPP servers.
It has context sensitive auto-completion for buddy names, commands, and even
ordinary English words. Similar to GNU Emacs, You can customize and extend GNU
Freetalk with Scheme language.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

./bootstrap
%configure
%make_build
%install
%make_install
rm -rf %{buildroot}%{_infodir}/dir
chmod 755 %{buildroot}%{_datadir}/%{name}/extensions/first-time-run.sh
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
