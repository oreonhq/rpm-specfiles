%global _legacy_common_support 1

Name:		sxhkd
Version:	0.6.1
Release:	1%{?dist}
Summary:	Simple X hotkey daemon

License:	LicenseRef-Callaway-BSD
URL:		https://github.com/baskerville/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	make
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
* Thu Oct 22 2026 Oreon <oreonproject.org> - 0.6.1-1
- import
