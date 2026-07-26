%global source0_hash caf4770219bf560283f1a991f2383cf0817586d3fa2b413704ccc26e93e9d05a

%define _default_patch_fuzz 2
Summary: An interpreter for AGI games
Name: nagi
Version: 2.06
Release: 40%{?dist}
License: MIT
URL: http://www.agidev.com/projects/nagi/
Source0: http://www.agidev.com/dl_files/nagi/nagi_src_-_2002-11-14.tar.gz
Source1: nagi.sgml
Patch0: nagi-2.06-debian.patch 
Patch1: nagi-2.06-build_with_gcc-3.4.patch
Patch2:nagi-2.06-build_with_gcc-4.0.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: docbook-utils, SDL-devel, SDL-static
%description
NAGI is an interpreter for AGI games, such as the early Space Quest,
Leisure Suit Larry and King's Quest games.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qcn nagi

%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0

%build
export CFLAGS="$RPM_OPT_FLAGS -fcommon"
cd src
make -f Makefile.linux
docbook2man %{SOURCE1} 
cd ..
sed -i 's/\r//' license.txt
sed -i 's/\r//' readme.html

%install
mkdir -p %{buildroot}/%{_bindir}
install -Dp -m755 bin/nagi %{buildroot}/%{_bindir}/nagi
mkdir -p %{buildroot}%{_datadir}/nagi
install -Dp -m644 bin/*.nbf %{buildroot}%{_datadir}/nagi/
mkdir -p %{buildroot}%{_sysconfdir}/nagi
install -Dp -m644 bin/nagi.ini %{buildroot}%{_sysconfdir}/nagi/
install -Dp -m644 bin/standard.ini %{buildroot}%{_sysconfdir}/nagi/
mkdir -p %{buildroot}%{_mandir}/man1
install -Dp -m644 src/nagi.1 %{buildroot}%{_mandir}/man1

%files
%license license.txt
%doc readme.html
%{_bindir}/nagi 
%{_datadir}/nagi/
%config(noreplace) %{_sysconfdir}/nagi/
%{_mandir}/man1/nagi.1.gz

%changelog
%autochangelog
