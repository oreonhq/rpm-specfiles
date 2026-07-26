%global source0_hash b1438c3cad13b6101edb31ce8d00ba4ed2f972754e85b90f763e04fa5143c6fc

%define _legacy_common_support 1

Name:		bspwm
Version:	0.9.9
Release:	19%{?dist}
Summary:	A tiling window manager based on binary space partitioning

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/baskerville/bspwm
Source0:	%{url}/archive/%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	desktop-file-utils
BuildRequires: make

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
%autochangelog
