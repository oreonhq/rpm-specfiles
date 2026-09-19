%global source0_hash c048237a4ba396378ac7e8d1997d1a90b67c97864a7b42e9ab13e1ee23318293

Name:           xwm
Version:        0.1.9
Release:        %autorelease
Summary:        Tiny XCB floating window manager

License:        MIT
URL:            https://github.com/mcpcpc/xwm
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-keysyms-devel

Recommends:     dmenu
Recommends:     st
Recommends:     surf
Suggests:       ImageMagick

%description
xwm is a tiny XCB floating window manager. It is a minimal viable solution
that was developed with single-monitor workflows in mind. Despite the small
footprint, xwm maintains extensibility and can be customized to enhance the
user experience.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build \
  CFLAGS="%{optflags}" \
  LDFLAGS="%{build_ldflags}"

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE
%doc README CHANGELOG
%{_bindir}/xwm
%{_mandir}/man1/xwm.1*

%changelog
%autochangelog
