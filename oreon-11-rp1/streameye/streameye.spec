%global source0_hash 09fa8dcc72bb4c9db7c2af7f6a48b6bb3e1a908a845ea990fb13e615d5bb0433

Name:		streameye
Version:	0.9
Release:	16%{?dist}
Summary:	Simple MJPEG streamer for Linux
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/ccrisan/streameye
Source0:	https://github.com/ccrisan/streameye/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
%description
Simple MJPEG streamer for Linux. It acts as an HTTP server and is capable
of serving multiple simultaneous clients.

It will feed the JPEGs read at input to all connected clients, in a MJPEG
stream. The JPEG frames at input may be delimited by a given separator.
In the absence of a separator, streamEye will auto-detect all JPEG frames.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{version}

%build
%make_build CFLAGS='%{optflags} -pthread -D_GNU_SOURCE' BINDIR=%{_bindir}

%install
mkdir -p %{buildroot}%{_bindir}
cp -p %{name} %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
