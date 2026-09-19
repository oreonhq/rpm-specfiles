%global source0_hash 6faff1eb8cfa8d2d99302eb9fdb10f0aedb2daf20319cc704b2c80a4f220fc13

%global forgeurl https://github.com/facebook/netconsd

Name:           netconsd
Version:        0.4.1
Release:        %autorelease
Summary:        The Netconsole Daemon

License:        BSD-3-Clause
URL:            https://facebookmicrosites.github.io/netconsd
Source:         %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libstdc++-static

%description
This is a daemon for receiving and processing logs from the Linux Kernel, as
emitted over a network by the kernel's netconsole module. It supports both the
old "legacy" text-only format, and the new extended format added in v4.4.

The core of the daemon does nothing but process messages and drop them: in order
to make the daemon useful, the user must supply one or more "output modules".
These modules are shared object files which expose a small ABI that is called by
netconsd with the content and metadata for netconsole messages it receives.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%if 0%{?rhel} && 0%{?rhel} < 10
%set_build_flags
%endif
%make_build
%make_build utils

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/netconsd

install -m0755 netconsd %{buildroot}%{_bindir}
install -m0755 util/netconsblaster %{buildroot}%{_bindir}
install -m0755 modules/*.so %{buildroot}%{_libdir}/netconsd

%files
%license LICENSE
%doc README.md
%{_bindir}/netconsd
%{_bindir}/netconsblaster
%{_libdir}/netconsd

%changelog
%autochangelog
