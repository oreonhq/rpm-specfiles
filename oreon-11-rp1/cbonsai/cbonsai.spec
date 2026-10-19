%global source0_hash 1ded632e90644d29ad6c142c62aa2e66eab3c7a6dee23dfb6f7a12a973c3fc50
Name:           cbonsai
Version:        1.4.2
Release:        1%{?dist}
Summary:        Grow bonsai trees in your terminal
License:        GPL-3.0-only
URL:            https://gitlab.com/jallbrit/cbonsai
Source0:        https://gitlab.com/jallbrit/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  scdoc
# /oreon:deps
%description
cbonsai is a bonsai tree generator, written in C using ncurses. It
intelligently creates, colors, and positions a bonsai tree, and is
entirely configurable via CLI options-- see usage. There are 2 modes of
operation: static (see finished bonsai tree), and live (see growth step-by-
step).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%make_build
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
