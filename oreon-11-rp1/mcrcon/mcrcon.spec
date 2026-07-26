%global source0_hash 1743b25a2d031b774e805f4011cb7d92010cb866e3b892f5dfc5b42080973270

Name:           mcrcon
Version:        0.7.2
Release:        11%{?dist}
Summary:        Console based rcon client for minecraft servers
License:        Zlib
URL:            https://github.com/Tiiffi/mcrcon/
Source0:        https://github.com/Tiiffi/mcrcon/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description
Mcrcon is powerful IPv6 compliant minecraft rcon client with bukkit coloring
support. It is well suited for remote administration and to be used as part of
automated server maintenance scripts. Does not cause "IO: Broken pipe" or
"IO: Connection reset" spam in server console.

Features:
- Interactive terminal mode - keeps the connection alive
- Send multiple commands in one command line
- Silent mode - does not print rcon output
- Support for bukkit coloring on Windows and Linux (sh compatible shells)
- Multiplatform code - compiles on many platforms with only minor changes

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Fix line endings
sed -i 's/\r$//' README.md

%build
%make_build CFLAGS="-std=gnu99" EXTRAFLAGS="%{?__global_cflags} %{?__global_ldflags}"

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/mcrcon
%{_mandir}/man1/mcrcon.1*

%changelog
%autochangelog
