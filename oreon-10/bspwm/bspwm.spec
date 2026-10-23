%define _legacy_common_support 1

Name:		bspwm
Version:	0.9.9
Release:	1%{?dist}
Summary:	A tiling window manager based on binary space partitioning

License:	LicenseRef-Callaway-BSD
URL:		https://github.com/baskerville/bspwm
Source0:	%{url}/archive/%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	desktop-file-utils
BuildRequires:	make

%description
bspwm is a tiling window manager that represents windows as the leaves of a
full binary tree.

It only responds to X events, and the messages it receives on a dedicated
socket.

bspc is a program that writes messages on bspwm's socket.

bspwm doesn't handle any keyboard or pointer inputs: a third party program
(e.g. sxhkd) is needed in order to translate keyboard and pointer events to
bspc invocations.

%prep
%setup -q

%build
make VERBOSE=1 %{?_smp_mflags} CFLAGS="%{optflags}" \
	LDFLAGS="%{?__global_ldflags}"

%install
%make_install PREFIX="%{_prefix}"

%check
desktop-file-validate %{buildroot}/%{_datadir}/xsessions/%{name}.desktop

%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/bspc
%{_docdir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/bspc.1.gz
%{_datadir}/bash-completion/completions/bspc
%{_datadir}/zsh/site-functions/_bspc
%{_datadir}/fish/vendor_completions.d/bspc.fish
%{_datadir}/xsessions/%{name}.desktop

%changelog
* Thu Oct 22 2026 Oreon <oreonproject.org> - 0.9.9-1
- import
