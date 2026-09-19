%global source0_hash d4416176e65e584c848617e1110078d2e2dfebec0e6832591ba6d8891db70dad

%global git_commit 9c7ec82dfebef238a61e5a6788f043420d30193f
%global git_date 20250901

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:		softwedge
Version:	0.1^%{git_suffix}
Release:	2%{?dist}
Summary:	A serial software keyboard wedge for *nix X11
License:	GPL-2.0-only
URL:		https://github.com/theatrus/softwedge
Source0:	%{url}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
BuildRequires:	gcc
BuildRequires:	libX11-devel
BuildRequires:	libXtst-devel

%description
Small Linux utility which forwards data from a serial port (such as
from a tty, or a barcode scanner) and re-issues the data as X11 key press
events.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_commit}

%build
# Included Makefile isn't much useful
gcc %{build_cflags} %{build_ldflags} -o %{name} -Isw sw/main.c sw/softwedge.c -lX11 -lXtst

%install
install -Dpm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README
%{_bindir}/softwedge

%changelog
%autochangelog
