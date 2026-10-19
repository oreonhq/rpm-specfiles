%global source0_hash 19279f70707bbe5ffa619f2dc319f888cec0c4a8d339dc0a21330517bd6f521d
Name:      mythes
Summary:        A thesaurus library
Version:   1.2.5
Release:        1%{?dist}
Source0:        https://github.com/hunspell/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
URL:       https://github.com/hunspell/mythes
License:   BSD-3-Clause-Modification AND MIT
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
BuildRequires:  make
# /oreon:deps
%description
MyThes is a simple thesaurus that uses a structured text data file and an
index file with binary search to look up words and phrases and return 
information on part of speech, meanings, and synonyms.

%package devel
Requires: mythes = %{version}-%{release}, pkgconfig
Summary: Files for developing with mythes
%description devel
Includes and definitions for developing with mythes

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure --disable-rpath --disable-static
%make_build
%check

make check
./example th_en_US_new.idx th_en_US_new.dat checkme.lst
./example morph.idx morph.dat morph.lst morph.aff morph.dic
%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mythes-devel -f %{oreon_filedir}/mythes-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.5-10
- Prepare for Oreon 11 (RP1)
