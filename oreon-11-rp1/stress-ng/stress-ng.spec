%global source0_hash 67e75894da3f634b85992069b0a888893221a77a3db5e3293cdddd0b1c0d4705
Name:		stress-ng
Version:	0.22.01
Release:        1%{?dist}
Summary:        Stress test a computer system in various ways
License:	GPL-2.0-or-later
URL:		https://github.com/ColinIanKing/stress-ng
Source0:        https://github.com/ColinIanKing/stress-ng/archive/refs/tags/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:     0_18_01-poewrpc-remove-darn.patch
# oreon:deps
BuildRequires:  Judy-devel
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  kernel-headers
BuildRequires:  keyutils-libs-devel
BuildRequires:  libaio-devel
BuildRequires:  libatomic
BuildRequires:  libattr-devel
BuildRequires:  libcap-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  lksctp-tools-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
Stress test a computer system in various ways. It was designed to exercise
various physical subsystems of a computer as well as the various operating
system kernel interfaces.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%make_build
%install
install -p -m 755 -D %{name} %{buildroot}%{_bindir}/%{name}
install -p -m 644 -D %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -pm 644 bash-completion/%{name} \
    %{buildroot}%{_datadir}/bash-completion/completions/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
