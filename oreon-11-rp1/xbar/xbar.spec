%global source0_hash 7de4b4c90e6b427ea451d9fe52d3883c314ef266428b1140bc64ea775e330e85

Name:           xbar
Version:        0.0.1
Release:        11%{?dist}
Summary:        Tiny XCB information bar

License:        MIT
URL:            https://github.com/mcpcpc/xbar
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-keysyms-devel

%description
xbar is a tiny XCB status bar. An incredibly lightweight information bar,
designed to print important real-time system metrics. Beyond foreground and
background colors, xbar offers limited customization for a distraction-free
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
%{_bindir}/xbar

%changelog
%autochangelog
