%global source0_hash ee5ef648ea08d20d9062db22e7bf62a7b7261af02053f916016d1b80a66a5609

Name:           conspy
Version:        1.16
Release:        7%{?dist}
Summary:        Remote control for text mode virtual consoles

License:        AGPL-3.0-or-later
URL:            https://conspy.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}-1/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel

%description
Conspy allows a (possibly remote) user to see what is displayed on
a Linux virtual console, and send keystrokes to it. It is rather
like VNC, but where VNC takes control of a GUI conspy takes control
of a text mode virtual console. Unlike VNC, conspy does not require
a server to be installed prior to being used.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
aclocal
automake --foreign --add-missing --copy
autoconf

%build
%configure
%make_build

%install
%make_install

%files
%doc ChangeLog.txt README.txt conspy.html
%license agpl-3.0.txt
%{_mandir}/man*/*.*
%{_bindir}/%{name}

%changelog
%autochangelog
