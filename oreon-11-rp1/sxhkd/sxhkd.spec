%global source0_hash 9d7a64d73f7114a24ff93a35a2662afd9807e0df9ffbfabd24230b4872503fcb
%global _legacy_common_support 1
Name:		sxhkd
Version:	0.6.3
Release:        1%{?dist}
Summary:        Simple X hotkey daemon
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/baskerville/%{name}
Source0:        https://github.com/baskerville/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%{?systemd_requires}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-keysyms-devel
# /oreon:deps
%description
sxhkd is an X daemon that reacts to input events by executing commands.

Its configuration file is a series of bindings that define the associations
between the input events and the commands.

The format of the configuration file supports a simple notation for mapping
multiple shortcuts to multiple commands in parallel.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%make_build VERBOSE=1 %{?_smp_mflags} CFLAGS="%{optflags}" \
	LDFLAGS="%{?__global_ldflags}"
%install
%make_install PREFIX="%{_prefix}"
install -p -D -m 0644 contrib/systemd/%{name}.service \
	%{buildroot}/%{_unitdir}/%{name}.service
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
