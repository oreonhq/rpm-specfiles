%global source0_hash b4e56cb00d3e509acfba9a9b627ffd8273b876b4e2408642259f6da28fa0ff86
Name:          opus-tools
Version:       0.2
Release:        1%{?dist}
Summary:        A set of tools for the opus audio codec
License:       LicenseRef-Callaway-BSD AND GPL-2.0-only
URL:           http://www.opus-codec.org/
Source0:        http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  flac-devel
BuildRequires:  gcc
BuildRequires:  libogg-devel
BuildRequires:  libopusenc-devel
BuildRequires:  make
BuildRequires:  opus-devel
BuildRequires:  opusfile-devel
# /oreon:deps
%description
The Opus codec is designed for interactive speech and audio transmission over 
the Internet. It is designed by the IETF Codec Working Group and incorporates 
technology from Skype's SILK codec and Xiph.Org's CELT codec.

This is a set of tools for the opus codec.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

make check %{?_smp_mflags} V=1
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
