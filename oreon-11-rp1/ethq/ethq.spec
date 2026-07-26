%global source0_hash 6e40d98d32abbe0915a7a8996edcdbae61a54bb1f34f2f8a5c9c8d3d2962ec23

# it crashes with lto enabled on StringsetParser::parsers first modification
%define _lto_cflags %{nil}

Name:           ethq
Version:        0.7.0
Release:        %autorelease
Summary:        Ethernet NIC Queue stats viewer

%global gitver %{lua:gv,n=string.gsub(macros.version, '[.]', '_');print(gv)}

License:        MPL-2.0
URL:            https://github.com/isc-projects/ethq
Source0:        %{url}/archive/v%{gitver}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ncurses-devel

%description
Displays an auto-updating per-second count of the number of packets and
bytes being handled by each specified NIC, and on multi-queue NICs shows
the per-queue statistics too.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{gitver}

%build
%make_build CXXFLAGS="${CXXFLAGS}" LDFLAGS="${LDFLAGS}"

%install
# TODO: contribute make install target
%dnl %make_install CFLAGS="${CFLAGS}" LDFLAGS="${LDFLAGS}"
mkdir -p %{buildroot}%{_sbindir}
install ethq %{buildroot}%{_sbindir}

%check
./%{name} -h
./%{name}_test generic < /dev/null

%files
%license LICENSE
%doc README.md
%{_sbindir}/%{name}

%changelog
%autochangelog
