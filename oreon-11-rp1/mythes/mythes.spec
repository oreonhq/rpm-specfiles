Name:      mythes
Summary:   A thesaurus library
Version:   1.2.5
Release:   10%{?dist}
Source:    https://github.com/hunspell/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 19279f70707bbe5ffa619f2dc319f888cec0c4a8d339dc0a21330517bd6f521d
%global source0_file mythes-1.2.5.tar.xz
# oreon url source checksums end
URL:       https://github.com/hunspell/mythes
License:   BSD-3-Clause-Modification AND MIT
BuildRequires: make
BuildRequires: hunspell-devel, gcc-c++

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/mythes-1.2.5.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "19279f70707bbe5ffa619f2dc319f888cec0c4a8d339dc0a21330517bd6f521d" || { echo "oreon: Source0 SHA256 mismatch for mythes-1.2.5.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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

%files
%doc README COPYING AUTHORS
%{_libdir}/*.so.*
%{_datadir}/mythes

%files devel
%doc data_layout.txt
%{_includedir}/mythes.hxx
%{_libdir}/*.so
%{_libdir}/pkgconfig/mythes.pc
%{_bindir}/th_gen_idx.pl

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.5-10
- Prepare for Oreon 11 (RP1)
