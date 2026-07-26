%global source0_hash 28bbc33ee64fdcaa086b1b134220b69c9d5a4aec887e043612bbca51dbe17e34

Name:           progman
Version:        1.0
Release:        13%{?dist}
Summary:        Simple X11 window manager modeled after Program Manager

License:        MIT
URL:            https://github.com/jcs/progman
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  gdk-pixbuf2-xlib-devel
BuildRequires:  /usr/bin/xxd

%description
progman is a simple X11 window manager modeled after Program Manager from the
Windows 3 era. It is descended from aewm by Decklin Foster and retains its MIT
license.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Do not strip binaries on install so we can get debuginfo
sed -e 's/install -s/install -p/' -i Makefile

%build
%set_build_flags
%make_build

%install
export PREFIX="%{buildroot}%{_prefix}"
%make_install

%files
%license LICENSE
%doc README.md progman.ini themes
%{_bindir}/progman

%changelog
%autochangelog
