%global source0_hash c2cc67858013d4391236627af0e9d2fd3c75602097b8190f71e8924f27532222

%global commit b4ba3c8030b22e8a8c59dcb538642a29bd6a7085
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           usbsniff
Version:        0
Release:        26.20170624git%{shortcommit}%{?dist}
Summary:        USB traffic capture and replay tools

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/vdudouyt/usbsniff
Source0:        https://github.com/vdudouyt/usbsniff/archive/%{commit}/usbsniff-%{shortcommit}.tar.gz
Patch0:         usbsniff-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  flex-devel
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig(libusb-1.0)

%description
Tools to capture USB traffic, store the capture results and replay them against
the device. Useful for debugging USB devices or reverse-engineering protocols.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n usbsniff-%{commit}

%build
# Parallel make broken, missing deps
make LIBS="$(pkg-config --libs libusb-1.0) -lpcap -ll" \
        CFLAGS="$(pkg-config --cflags libusb-1.0) -DLINUX %{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
make install DESTDIR=%{buildroot}

%files
%{_bindir}/*
%doc LICENSE README.md

%changelog
%autochangelog
