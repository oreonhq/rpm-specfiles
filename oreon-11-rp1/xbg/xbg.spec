%global source0_hash 2ae41cbc55b76b6ccda0de5caa0c7904e1d4dd223ecbd9a9402f4c741a959819
Name:           xbg
Version:        0.0.2
Release:        11%{?dist}
Summary:        Tiny XCB root window color setter
License:        MIT
URL:            https://github.com/mcpcpc/xbg
Source0:        https://github.com/mcpcpc/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libxcb-devel
BuildRequires:  make
BuildRequires:  xcb-util-devel
# /oreon:deps
%description
xbg is a tiny XCB root window color setter. It changes the root window
background to a specified X11 color name.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build \
  CC="%{__cc}" \
  CFLAGS="%{optflags}" \
  ALL_LDFLAGS="-lxcb -lxcb-util %{build_ldflags}"
%install
%make_install PREFIX="%{_prefix}"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
