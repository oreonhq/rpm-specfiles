%global source0_hash bb5b4f29a706af2f891987802200e26b737bcece44338172419755f1eee1b580

Name:           freetalk
Version:        4.2
Release:        %autorelease
Summary:        Terminal XMPP client

License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/freetalk/
Source0:        http://ftp.gnu.org/gnu/freetalk/freetalk-4.2.tar.gz
Source1:        http://ftp.gnu.org/gnu/freetalk/freetalk-4.2.tar.gz.sig
# https://savannah.gnu.org/project/release-gpgkeys.php?group=freetalk
Source2:        freetalk-keyring.gpg

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
Requires:  words

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

# Files containing shebangs need to have the executable bits.
chmod 755 %{buildroot}%{_datadir}/%{name}/extensions/first-time-run.sh

%check
# Find a way to run a smoke test without generating a configuration file
#./freetalk -help  2>&1 | grep 'version %{version}'

%files
%license COPYING
%doc AUTHORS
%doc NEWS
%doc README
%{_bindir}/freetalk
%dir %{_docdir}/freetalk
%dir %{_docdir}/freetalk/examples
%{_docdir}/freetalk/examples/*.ft
%{_docdir}/freetalk/examples/*.scm
%dir %{_datadir}/freetalk
%dir %{_datadir}/freetalk/extensions
%{_datadir}/freetalk/extensions/*.scm
%{_datadir}/freetalk/extensions/*.sh
%{_mandir}/man1/freetalk.1*
%{_infodir}/freetalk.info*

%changelog
%autochangelog
