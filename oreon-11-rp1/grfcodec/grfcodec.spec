%global source0_hash 20448dac4032377ed75f8ddace0192f3c57bdc1b798c76c4f3566135c3b3572a

Version:       6.2.0
%global tag %{version}
%global forgeurl https://github.com/OpenTTD/grfcodec
%forgemeta

Name:           grfcodec
Release:        %autorelease
Summary:        A suite of programs to modify Transport Tycoon Deluxe's GRF files
License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-ng-compat-devel

%description
A suite of programs to modify Transport Tycoon Deluxe's GRF files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc changelog.txt COPYING
%doc docs/*.txt docs/readme.md
%{_bindir}/grfcodec
%{_bindir}/grfid
%{_bindir}/grfstrip
%{_bindir}/nforenum
%{_mandir}/man1/grfcodec.1.gz
%{_mandir}/man1/grfid.1.gz
%{_mandir}/man1/grfstrip.1.gz
%{_mandir}/man1/nforenum.1.gz

%changelog
%autochangelog
