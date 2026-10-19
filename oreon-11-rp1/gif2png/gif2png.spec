%global source0_hash a2528adfb284d4d43f3171268c2be2a86d618f2c4a421ea0482541c7878f3348
%global debug_package %{nil}
Summary:        A GIF to PNG converter
Name:		gif2png
Version:	3.0.5
Release:        1%{?dist}
License:	LicenseRef-Callaway-BSD
URL:		http://www.catb.org/~esr/gif2png/
Source0:        http://www.catb.org/~esr/%{name}/%{name}-%{version}.tar.gz
Source100:	test-0.gif
Source101:	test-1.gif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  make
# /oreon:deps
%description
The gif2png program converts files from the obsolescent Graphic Interchange
Format to Portable Network Graphics. The conversion preserves all graphic
information, including transparency, perfectly. The gif2png program can
even recover data from corrupted GIFs.

There exists a 'web2png' program in a separate package which is able
to convert entire directory hierarchies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
%make_install
rm %{buildroot}%{_bindir}/web2png
rm %{buildroot}%{_mandir}/man1/web2png*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
