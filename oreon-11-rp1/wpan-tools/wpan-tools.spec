%global source0_hash 797ce516d098a2a7841d3a8a7331fb63b5c9fc0129e7c513cdf02c9f89c26f3c

Name:          wpan-tools
Version:       0.10
Release:       4%{?dist}
Summary:       Userspace tools for the Linux IEEE 802.15.4 stack
License:       ISC
URL:           https://github.com/linux-wpan/wpan-tools/

Source0:       %{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: gcc
BuildRequires: libnl3-devel

%description
Userspace tools for the Linux IEEE 802.15.4 stack.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-static

%make_build

%install
%make_install

%check
make %{?_smp_mflags} check

%files
%license COPYING
%doc wpan-ping/README.wpan-ping
%{_bindir}/iwpan
%{_bindir}/wpan-ping
%{_bindir}/wpan-hwsim

%changelog
%autochangelog
