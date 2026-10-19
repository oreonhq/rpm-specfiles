%global source0_hash 661a808dfffa933d78c6beb47a2937d572b9f03e94cbaaab3d4c0d72f410e9be
Name:		jpegoptim
Version:	1.5.6
Release:        1%{?dist}
Summary:        Utility to optimize JPEG files
License:	GPL-3.0-or-later
URL:		http://www.kokkonen.net/tjko/projects.html
Source0:        https://github.com/tjko/jpegoptim/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  make
# /oreon:deps
%description
Jpegoptim is an utility to optimize JPEG files. Provides lossless optimization
(based on optimizing the Huffman tables) and "lossy" optimization based on
setting maximum quality factor.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
