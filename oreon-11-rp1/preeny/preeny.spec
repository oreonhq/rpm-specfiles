%global source0_hash 709fda365246d23eea6aba6ef5b22093289382190dc68a0cb86e632006a0bdb5

Name:             preeny
URL:              https://github.com/zardus/preeny
Version:          0.1
Release:          23%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:          LicenseRef-Callaway-BSD
BuildRequires:    coreutils, make, gcc, libini_config-devel
Summary:          Some helpful preload libraries for pwning stuff
Source0:          https://github.com/zardus/preeny/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
Preeny helps you pwn noobs by making it easier to interact with services
locally. It disables fork(), rand(), and alarm() and, if you want, can convert
a server application to a console one using clever/hackish tricks, and can
even patch binaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
make %{?_smp_mflags}

%install
cd src
# workaround for RHEL-7, "install -pDt" doesn't seem to work
mkdir -p %{buildroot}%{_libdir}/%{name}
install -pt %{buildroot}%{_libdir}/%{name} *.so

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so

%changelog
%autochangelog
