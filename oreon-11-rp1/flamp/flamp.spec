%global source0_hash db8f7dd481db7661c80d7afaa43b044360ee6072d3f3faa1f362b1043a421cb2
%global alpha 0
Name:           flamp
Version:        2.2.14
Release:        1%{?dist}
Summary:        Amateur Multicast Protocol - file transfer program
License:        GPL-3.0-or-later
URL:            http://www.w1hkj.com/
Source0:        http://www.w1hkj.com/files/%{name}/%{name}-%{version}.tar.gz
Provides:       bundled(xz)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Flamp is a program for AMP or Amateur Multicast Protocol. An flamp session will
transmit one or more files with one or more iterations of the transmission.

Each file is broken into blocks, each of which has a check sum. The receiving
station saves the blocks that pass check sum. Successive transmissions will fill
in the missing blocks provided that the new blocks pass the check sum. After the
transmission sequence, the entire file is assembled and may be saved. “Fills”
may be provided by retransmitting the entire file or by the sending station only
sending the missing blocks. Start by downloading the current version of flamp
from http://www.w1hkj.com/download.html. Install the software as you would any
of the NBEMS applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CXXFLAGS="-std=c++17 $RPM_OPT_FLAGS"
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
