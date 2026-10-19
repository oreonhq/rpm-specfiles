%global source0_hash b60074835dbfc88b1ff2310317c725daaf6c43debcc18cf597a08fe79ed1454b
%define _legacy_common_support 1
Name:           lterm
Version:        1.5.1
Release:        1%{?dist}
Summary:        Terminal and multi protocol client
License:        GPL-2.0-only
URL:            http://%{name}.sourceforge.net/
Source0:        https://sourceforge.net/projects/%{name}/files/1.5/%{name}-%{version}.tar.gz
Patch0: lterm-c99.patch
Patch1: lterm-c99-2.patch
Patch2: lterm-c99-3.patch
Patch3: lterm-c99-4.patch
Patch4: lterm-c99-5.patch
Patch5: lterm-c99-6.patch
Patch6: lterm-c99-7.patch
Patch7: lterm-c99-8.patch
Patch8: lterm-c99-9.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  libssh-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  vte-devel
# /oreon:deps
%description
It is mainly used as SSH/Telnet client

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CFLAGS="${CFLAGS} -std=gnu99"
%configure --with-gtk2
%install
%make_install
desktop-file-install                                    \
--add-category="TerminalEmulator"                       \
--delete-original                                       \
--dir=%{buildroot}%{_datadir}/applications              \
%{buildroot}/%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
