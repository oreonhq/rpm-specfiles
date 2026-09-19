%global source0_hash 5f125d4c94e19e4be48edc43691e46df0b82f0b6ead95453dc7ac775a0d70066

Name:           xscope
Version:        1.4.5
Release:        2%{?dist}
Summary:        X Window Protocol Viewer

License:        MIT AND HPND-sell-variant
URL:            https://gitlab.freedesktop.org/xorg/app/xscope
Source0:        https://www.x.org/releases/individual/app/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  xorg-x11-xtrans-devel, xorg-x11-proto-devel

%description
xscope sits in-between an X11 client and an X11 server and prints the contents
of each request, reply, error, or event that is communicated between them.
This information can be useful in debugging and performance tuning of X11 
servers and clients.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS NEWS ChangeLog README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
