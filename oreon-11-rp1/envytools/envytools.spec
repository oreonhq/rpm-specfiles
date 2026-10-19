%global source0_hash 859c32db8882af56c2a31683e239686afec7bb3c8d825d289fda345b17a1a552
%global gitdate 20200810
Name:           envytools
Version:        0.0
Release:        1%{?dist}
Summary:        Tools for people envious of nvidia's blob driver
License:        MIT
URL:            https://github.com/envytools/envytools
Source0:        %{name}-%{gitdate}.tar.bz2
Source1:        make-git-snapshot.sh
Patch1:         envytools-add-missing-GETPARAM_PHYS-defines.patch
ExclusiveArch: %{ix86} x86_64 %{arm} aarch64 riscv64
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libdrm-devel
BuildRequires:  libpciaccess-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libxml2-devel
BuildRequires:  python3-devel
# /oreon:deps
%description
Envytools contains a number of tools used for debugging / development of
the nouveau driver:

envydis: Disassembler and assembler for various ISAs found on nvidia GPUs
nvbios:  Tools to decode the card description structures found in nvidia VBIOS
nva:     Tools to directly access the GPU registers
vstream: Tools to decode and encode raw video bitstreams

%package        hwdocs
Summary:        Nouveau hardware documentation
BuildArch:      noarch
%description    hwdocs
The %{name}-hwdocs package contains hardware documentation for video
hardware supported by the nouveau driver project.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{gitdate}

%build

%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build
%install
%cmake_install
cp -p COPYING $RPM_BUILD_ROOT%{_docdir}/%{name}
rm $RPM_BUILD_ROOT%{_bindir}/headergen
rm $RPM_BUILD_ROOT%{_bindir}/lookup
rm $RPM_BUILD_ROOT%{_bindir}/hwtest
rm $RPM_BUILD_ROOT%{_libdir}/*.a
rm -r $RPM_BUILD_ROOT%{_includedir}/%{name}
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/hwdocs/*.py
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n envytools-hwdocs -f %{oreon_filedir}/envytools-hwdocs.list

%changelog

%autochangelog
