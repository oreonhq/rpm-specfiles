%global source0_hash 30039bb3a15a1894d27e3d10ccaab943fdf9643a95a1ffd0a33ba778b3ce8f13

Name:           hid-replay
Version:        0.7.1
Release:        26%{?dist}
Summary:        HID Input device recorder and replay

License:        GPL-2.0-or-later
URL:            https://github.com/bentiss/%{name}
Source0:        https://github.com/bentiss/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Patch01:       0001-force-hid-replay-build-for-RHEL-6.patch

BuildRequires:  automake gcc make
BuildRequires:  asciidoc xmlto

%description
%{name} is a tool that allow users to capture hidraw description and
events in order to replay them through the uhid kernel module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P01 -p1

%build
autoreconf -v --install || exit 1
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README
%{_bindir}/hid-replay
%{_bindir}/hid-recorder
%{_mandir}/man1/hid-replay.1*
%{_mandir}/man1/hid-recorder.1*

%changelog
%autochangelog
