%global source0_hash 0b3f3ce16eef060df6e0d90327ee82593dfd75281347908698747cfa3f8d0655

Name:           lsw
Version:        0.3
Release:        26%{?dist}
Summary:        Prints all window titles of DISPLAY to standard output
License:        MIT
URL:            http://tools.suckless.org/%{name}
Source0:        http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
Patch0:         lsw-0.3-config.patch
# 4d6e1b39
Patch1:         lsw-0.3-segfault-avoidance.patch
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  make
BuildRequires:  redhat-rpm-config
BuildRequires:  sed

%description
Lists the titles of all running X windows to stdout, similar to ls(1). Might
be useful for script integration.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .config
%patch -P1 -p1

%build
export LDFLAGS="%{?__global_ldflags}"
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%license LICENSE
%doc README
%{_bindir}/lsw
%{_mandir}/man1/lsw.1*

%changelog
%autochangelog
