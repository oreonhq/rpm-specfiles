%global source0_hash 7eb22c30a99dcdb50a8630ef7ff3e4642491ac4f8cd1aa9f3182264df4f4ad08
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: ed
Version: 1.22
Release: 1%{?dist}
Summary: Line-oriented text editor
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/ed/
Source0: https://ftp.gnu.org/gnu/ed/ed-%{version}.tar.lz
Source1: ed-%{version}.tar.lz.sig
Source2: ed-key.asc

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: patchelf
BuildRequires: lzip
BuildRequires: tar
%endif

%description
GNU ed is a line-oriented text editor, the standard Unix editor.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n ed-%{version} -p1

%build
./configure --prefix=%{_prefix} --bindir=%{_bindir} --mandir=%{_mandir} --infodir=%{_infodir} CFLAGS="%{_oreon_cflags}" LDFLAGS="%{_oreon_ldflags}"
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
