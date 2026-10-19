%global source0_hash a1669e3b5153e2a9e0bb453e937f448bf90764f4d2a7ecea2c9bb3d35ac9f2a6
Name:           taginfo
Version:        1.2
Release:        1%{?dist}
Summary:        Printer of Tag Information from Media Files
License:        GPL-2.0-or-later
URL:            http://grecni.com/software/taginfo/
Source0:        http://grecni.com/software/taginfo/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  taglib-devel
# /oreon:deps
%description
Taginfo is a quick implementation of the TagLib API for use in the music
jukebox program Room Juice.  It's meant to be fast, not featureful. Taginfo
reads what tags TagLib can read, which as of this writing are ID3, ID3V2,
Ogg, and FLAC.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

make %{?_smp_mflags} CC="%{__cxx} %{optflags}"
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 -p %{name} $RPM_BUILD_ROOT%{_bindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
