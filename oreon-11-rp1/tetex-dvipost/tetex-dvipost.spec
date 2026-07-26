%global source0_hash da05010ec47b7bc6b410d9c1eb7b083eeeed1a96f1986470377e604a64fa425a

%define real_name dvipost
%{!?_texmf_vendor: %define _texmf %(eval "echo `kpsewhich -expand-var '$TEXMFDIST'`")}

Name:           tetex-%{real_name}
Version:        1.1
Release:        45%{?dist}
Summary:        LaTeX post filter command to support change bars and overstrike mode

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://efeu.cybertec.at/
Source0:        http://efeu.cybertec.at/%{real_name}.tar.gz
Patch0:         %{name}-destdir.patch
Patch1:         tetex-dvipost-configure-c99.patch

BuildRequires: make
BuildRequires:  tex(latex)
BuildRequires:  /usr/bin/kpsewhich
BuildRequires:  gcc-c++

Requires:	tex(latex)

%description
The command dvipost is a post procesor for dvi files, created by latex
or tex. It is used for special modes, which normally needs the support
of dvi drivers (such as dvips). With dvipost, this features could be
implemented independent of the preferred driver. Currently, the post
processor supports layout raster, change bars and overstrike mode.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{real_name}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%configure
%make_build

%install
%make_install

%post -p /usr/bin/texhash

%postun -p /usr/bin/texhash

%files
%license COPYING
%{_bindir}/*
%{_texmf_vendor}/tex/latex/misc/*

%doc README NOTES dvipost.html
%{_mandir}/man*/*

%changelog
%autochangelog
