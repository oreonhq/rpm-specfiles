%global source0_hash 06401f8abfad7ac3bdbce66ccda2c37878fa103a53a3c3ed35e386f2514dd9bd
%global		mainver		2.61
%global		docver		%{mainver}
%global		yashdocdir		%{_datadir}/doc/%{name}-doc
%global		baserelease	1
%undefine		minorver
%undefine       _changelog_trimtime
Name:		yash
Version:	%{mainver}
Release:        1%{?dist}
Summary:        Yet Another SHell
License:	GPL-2.0-only
URL:		https://github.com/magicant/yash/
Source0:        https://github.com/magicant/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Provides:		/bin/yash
Requires(post):	grep
Requires(post):	coreutils
Requires(postun):	sed
# oreon:deps
BuildRequires:  /usr/bin/a2x
BuildRequires:  /usr/bin/asciidoc
BuildRequires:  /usr/bin/ps
BuildRequires:  /usr/bin/xgettext
BuildRequires:  ed
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
Yash is a command line shell that conforms to the POSIX.1 (IEEE Std
1003.1, 2008 Edition) standard for the most part.

Yash also has its own features beyond POSIX, such as:
  * global aliases
  * random numbers
  * socket redirections and other special redirections
  * right prompt
  * command completion

%package	doc
Summary:	Documentation for %{name}
Version:	%{docver}
License:	CC-BY-SA-2.1-JP
BuildArch:	noarch
Requires:	%{name} = %{mainver}-%{release}
%description	doc
This package contains document files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

./configure \
	--prefix=%{_prefix} \
	--exec-prefix=%{_exec_prefix} \
	--bindir=%{_bindir} \
	--datarootdir=%{_datarootdir} \
	--docdir=%{yashdocdir}/ \
%make_build -k
%install
make install install-html \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p" \
	CPPROG="cp -p"
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

teststatus=0
make test || teststatus=1
cat tests/summary.log
sleep 3
exit $teststatus
%post

if [ -f %{_sysconfdir}/shells ]
then
	grep -q '^/bin/yash$' %{_sysconfdir}/shells || echo '/bin/yash' >> %{_sysconfdir}/shells
else
	echo '/bin/yash' > %{_sysconfdir}/shells
fi
exit 0
%postun

[ "$1" = 0 ] || exit 0
[ -f %{_sysconfdir}/shells ] || exit 0
sed -i -e '\@/bin/yash$@d' %{_sysconfdir}/shells
exit 0
%files -f %{oreon_filedir}/main.list
%files -n yash-doc -f %{oreon_filedir}/yash-doc.list

%changelog

%autochangelog
