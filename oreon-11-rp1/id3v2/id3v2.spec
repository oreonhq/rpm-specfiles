%global source0_hash 74d617eb21206b8b052933aae3f3bda35827f70e9303d87155b99926387f67c1
Name:           id3v2
Version:        0.1.12
Release:        1%{?dist}
Summary:        Command line ID3 tag editor
License:        GPL-2.0-or-later
URL:            http://id3v2.sourceforge.net/
Source0:        %{name}-%{version}-fedora.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  id3lib-devel
BuildRequires:  make
# /oreon:deps
%description
id3v2 is a command line tool to add, modify, remove, or view ID3v2
tags, as well as convert or list ID3v1 tags.  ID3 tags are commonly
embedded in compressed music files and are the standard way to more
fully describe the work than would normally be allowed by putting the
information in the filename.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-fedora

%build

CXXFLAGS="$RPM_OPT_FLAGS" make %{?_smp_mflags} PREFIX="%{_prefix}"
%install
install -Dpm 755 id3v2 $RPM_BUILD_ROOT%{_bindir}/id3v2
install -Dpm 644 id3v2.1 $RPM_BUILD_ROOT%{_mandir}/man1/id3v2.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
