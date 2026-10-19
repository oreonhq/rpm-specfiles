%global source0_hash bde4dcb3b9a888b8876149832fe27198c0a98e8bb7fc865717f8dde90abe4acf
Name:           usbguard-notifier
Version:        0.1.1
Release:        3%{?dist}
Summary:        A tool for detecting usbguard policy and device presence changes
License:        GPL-2.0-or-later
URL:            https://github.com/Cropi/%{name}
Source0:        https://github.com/Cropi/usbguard-notifier/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:         remove-catch.patch
Requires: systemd
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libnotify-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  usbguard-devel
# /oreon:deps
%description
USBGuard Notifier software framework detects usbguard policy modifications
as well as device presence changes and displays them as pop-up notifications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1

%build

mkdir -p ./m4
autoreconf -i -f -v --no-recursive ./
export CXXFLAGS="$RPM_OPT_FLAGS"
%configure \
    --disable-silent-rules \
    --enable-debug-build
%set_build_flags
make %{?_smp_mflags}
%install
make install INSTALL='install -p' DESTDIR=%{buildroot}
%oreon_autofiles main

%post

%systemd_user_post %{name}.service
%preun

%systemd_user_preun %{name}.service
%postun

%systemd_user_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
