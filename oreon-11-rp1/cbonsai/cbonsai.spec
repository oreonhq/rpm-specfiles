%global source0_hash 38531a5f5584185d63b7bcd4a308cad9f61cd829b676c221d254bdcb39c67427

Name:           cbonsai
Version:        1.3.1
Release:        11%{?dist}
Summary:        Grow bonsai trees in your terminal

License:        GPL-3.0-only
URL:            https://gitlab.com/jallbrit/cbonsai
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  scdoc

%description
cbonsai is a bonsai tree generator, written in C using ncurses. It
intelligently creates, colors, and positions a bonsai tree, and is
entirely configurable via CLI options-- see usage. There are 2 modes of
operation: static (see finished bonsai tree), and live (see growth step-by-
step).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version}

%build
%if 0%{?rhel} || 0%{?fedora} == 35
%set_build_flags
%endif
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
