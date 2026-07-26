%global source0_hash 5f44d623ef6fda01062dcfe8d5d0b75efad9a38114a28983ae895dbcbf43323e

%global _legacy_common_support 1
Name:		sxhkd
Version:	0.6.1
Release:	18%{?dist}
Summary:	Simple X hotkey daemon

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/baskerville/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:	gcc
%{?systemd_requires}
BuildRequires:	systemd
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-keysyms-devel

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

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_docdir}/%{name}/examples
%{_mandir}/man*/%{name}.1.gz
%{_unitdir}/%{name}.service

%changelog
%autochangelog
