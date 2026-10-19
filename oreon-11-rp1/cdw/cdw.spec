%global source0_hash e7eb49c5c58f26182c13ce62aa80297b281218b1def5f2aad8fa02740cbb979c
Name: cdw
Version: 0.8.1
Release:        1%{?dist}
Summary:        Front-end for tools used for burning data CD/DVD
License: GPL-2.0-or-later 
URL: http://cdw.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: 0001-add-formatstring.patch
Requires: dvd+rw-tools,wodim,genisoimage,xorriso 
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libburn-devel
BuildRequires:  libcdio-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
cdw is a ncurses based front-end for some command-line tools used for burning
data CD and DVD discs and for related tasks. The tools are: cdrecord/wodim,
mkisofs/genisoimage, growisofs, dvd+rw-mediainfo, dvd+rw-format, xorriso.
cdw is able to rip tracks from your audio CD to raw audio files.
Limited support for copying content of data CD and DVD discs to image files
is also provided. cdw can verify correctness of writing ISO9660 image to
CD or DVD disc using md5sum or some of  programs that verifies SHA hashes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CXXFLAGS="%{optflags}" LIBS="-lm"
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

make check LIBS="-lm"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
