%global source0_hash ba075a43aa6ead51940e892ecffa4d0b8b40c241e4e2bc4bd9bd26b61fde23bd

# -*-Mode: rpm-spec-mode; -*-

%undefine __cmake_in_source_build

%global debug_package %{nil}

Name:     ydotool
Version:  1.0.4
Release:  8%{?dist}
Summary:  Generic command-line automation tool (no X!)
# Automatically converted from old format: AGPLv3
License:  AGPL-3.0-only
URL:      https://github.com/ReimuNotMoe/%{name}

Source0:  %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: make
BuildRequires: scdoc
BuildRequires: systemd-rpm-macros

%description

Performs some of the functions of xdotool(1) without requiring X11 -
however, it generally requires root permission (to open /dev/uinput)

N.B. it is strongly recommended to start the ydotoold daemon with:

- systemctl enable ydotool
- systemctl start ydotool

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF

make -C %{_vpath_builddir} -j `nproc`

%install
mkdir -p %{buildroot}/%{_bindir}
strip */%{name}
strip */%{name}d
install -p -m 0755 */%{name} %{buildroot}/%{_bindir}
install -p -m 0755 */%{name}d %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_unitdir}
install -p -m 0644 */%{name}.service %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_mandir}/man8
scdoc < manpage/%{name}.1.scd > %{buildroot}/%{_mandir}/man1/%{name}.1
scdoc < manpage/%{name}d.8.scd > %{buildroot}/%{_mandir}/man8/%{name}d.8

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_unitdir}/%{name}.service
%{_bindir}/%{name}*
%license LICENSE
%doc README.md
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man8/%{name}d.8.*

%changelog
%autochangelog
