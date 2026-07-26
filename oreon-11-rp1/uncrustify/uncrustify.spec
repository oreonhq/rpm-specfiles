%global source0_hash 3bb56ebdb16397d6c9dc6b5be8ed6e16ee158399019485d1c8fc4980f864a8bb

Name:		uncrustify
Version:	0.82.0
Release:	%autorelease
Summary:	Reformat Source

License:	GPL-2.0-or-later
URL:		https://uncrustify.sourceforge.net/
Source0:	https://prdownloads.sourceforge.net/uncrustify/uncrustify-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Source Code Beautifier for C, C++, C#, D, Java, and Pawn

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n uncrustify-uncrustify-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc NEWS
%doc documentation
%{_bindir}/uncrustify
%{_datadir}/doc/uncrustify/*
%{_mandir}/man1/uncrustify.1*

%changelog
%autochangelog
