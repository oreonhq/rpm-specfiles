%global source0_hash 111ade20cc545e8dfd7ce4e293bd6b31cd1678a989b6a730bd2fa2acc6254818

Name:           nethogs
Version:        0.8.8
Release:        4%{?dist}
Summary:        A tool resembling top for network traffic

License:        GPL-1.0-or-later
URL:            https://github.com/raboof/nethogs/

Source0:        https://github.com/raboof/nethogs/archive/v%{version}/nethogs-%{version}.tar.gz

Requires:       ncurses 
BuildRequires: make
BuildRequires:  libstdc++-devel, ncurses-devel, libpcap-devel, gcc-c++

%description
NetHogs is a small "net top" tool.

Instead of breaking the traffic down per protocol or per subnet, like
most such tools do, it groups bandwidth by process and does not rely
on a special kernel module to be loaded.

So if there's suddenly a lot of network traffic, you can fire up
NetHogs and immediately see which PID is causing this, and if it's
some kind of spinning process, kill it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 

%build
make %{?_smp_mflags} CFLAGS="${RPM_OPT_FLAGS}" CXXFLAGS="${RPM_OPT_FLAGS}" %{name}

%install
rm -rf "${RPM_BUILD_ROOT}"

mkdir -p "${RPM_BUILD_ROOT}%{_sbindir}"
install -m 0755 src/nethogs "${RPM_BUILD_ROOT}%{_sbindir}/"

mkdir -p "${RPM_BUILD_ROOT}%{_mandir}/man8"
install -m 0644 doc/nethogs.8 "${RPM_BUILD_ROOT}%{_mandir}/man8/"

%files
%doc INSTALL DESIGN README.md
%{_sbindir}/nethogs
%doc %{_mandir}/man*/*

%changelog
%autochangelog
