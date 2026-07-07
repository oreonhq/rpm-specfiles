%global source0_hash 18487761f5ca626a036d65ef2db8ad9923bf61685e06e7533676c56d7d60eb14

Summary:        Command line clipboard and X selection tool
Name:           xsel
Version:        1.2.1
Release:        1%{?dist}
License:        MIT
URL:            https://www.kfish.org/software/xsel/
Source0:        https://github.com/kfish/xsel/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(sm)

%description
XSel is a command-line program for getting and setting the contents of the
X selection (aka "the clipboard"). It can also append to and delete the
clipboard, or follow a growing file (similar to tail -f), and act as a
daemon, keeping the clipboard alive after other apps exit.

Used by plasma-applet-translator to grab and set clipboard/selection text.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version}

%build
autoreconf -fvi
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/xsel
%{_mandir}/man1/xsel.1*

%changelog
%autochangelog
