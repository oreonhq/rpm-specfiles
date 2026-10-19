%global source1_hash fe49a2224ccd3eaf0d6774f01e318843444fc9b86d9f8f2876d948960c8d3b8d
%global source0_hash 2264622d309d6c87a1cfc19148292b8859a688e9bc02d4702f5cd4f288745542
Name:           ddrescue
Version:        1.30
Release:        1%{?dist}
Summary:        Data recovery tool trying hard to rescue data in case of read errors
License:        GPL-3.0-or-later
URL:            http://www.gnu.org/software/ddrescue/ddrescue.html
Source0:        http://ftpmirror.gnu.org/ddrescue/ddrescue-%{version}.tar.lz
Source1:        http://ftpmirror.gnu.org/ddrescue/ddrescue-%{version}.tar.lz.sig
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  lzip
BuildRequires:  make
# /oreon:deps
%description
GNU ddrescue is a data recovery tool. It copies data from one file or block
device (hard disc, cd-rom, etc) to another, trying hard to rescue data in 
case of read errors. GNU ddrescue does not truncate the output file if not
asked to. So, every time you run it on the same output file, it tries to 
fill in the gaps.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# rpmbuild doesn't support lzip format
#setup -q
%setup -q -T -c
cd ..
lzip -d -c %{SOURCE0} > ddrescue-%{version}.tar
tar xf ddrescue-%{version}.tar
rm ddrescue-%{version}.tar

%build

%configure CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_infodir}/dir
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
