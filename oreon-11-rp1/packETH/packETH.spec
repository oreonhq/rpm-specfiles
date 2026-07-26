%global source0_hash 1783bac200b861ef40310c9392803a971f6026cc7b5296eefb9ee60824797d77

Name:           packETH
Version:        2.1
Release:        15%{?dist}
Summary:        A GUI packet generator tool

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/jemcek/packETH
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        packETH.desktop

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  autoconf automake
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel

%description
packETH is a Linux GUI tool that is able to send any packet or sequence of 
packets on the Ethernet. It uses the RAW socket option, so it doesn't care 
about ip, routing, etc. It is designed to have all the options available, 
with all the correct and incorrect values (incorrect means, that user can 
send wrong parameters like: incorrect checksum, wrong header length, etc.).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
# Build with new instructions from github
sed -i 's/^LIBS=/LIBS+=/' Makefile.am
sh autogen.sh
autoreconf -vfi
%configure
%make_build CFLAGS="${RPM_OPT_FLAGS} -fcommon"

%install
%make_install
# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/packeth

%changelog
%autochangelog
