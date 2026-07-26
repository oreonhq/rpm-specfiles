%global source0_hash 6ebfebdad21cf381f2026f0b0b0c9dc024b1dd6d156b71b7a6977fdbe2db8a0b

Name: ustreamer
Version: 6.12
Release: 6%{?dist}
Summary: Lightweight and fast MJPG-HTTP streamer
License: GPL-3.0-or-later
URL: https://github.com/pikvm/ustreamer
Source: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: libatomic
BuildRequires: pkgconfig(libbsd)
BuildRequires: pkgconfig(libevent)
BuildRequires: pkgconfig(libevent_pthreads)
BuildRequires: pkgconfig(libgpiod)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(python)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(build)
BuildRequires: python3dist(wheel)
BuildRequires: python3dist(pip)

%description
ustreamer(µStreamer) is a lightweight and very quick server to stream MJPG video
from any V4L2 device to the net.

All new browsers have native support of this video format,
as well as most video players such as mplayer, VLC etc.

µStreamer is a part of the Pi-KVM project designed to stream VGA and HDMI
screencast hardware data with the highest resolution and FPS possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%set_build_flags
%make_build \
    WITH_SYSTEMD=1 \
    WITH_GPIO=1 \
    WITH_PYTHON=1

%install
%make_install 'PREFIX=%{_prefix}'\
    WITH_PYTHON=1

%files
%license LICENSE
%doc README.md
%{_bindir}/ustreamer
%{_bindir}/ustreamer-dump
%{_mandir}/man1/ustreamer.1*
%{_mandir}/man1/ustreamer-dump.1*

%package -n python3-%{name}
Summary: Python 3 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Python 3 bindings for %{name}.

%files -n python3-%{name}
%{python3_sitearch}/%{name}*

%changelog
%autochangelog
