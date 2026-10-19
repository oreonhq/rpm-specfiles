%global source0_hash 69eb3d83bce78b6610f4a8f19d089059079ebc475c36d456ebcb4c8add431166
Name:           fntsample
Version:        5.4
Release:        1%{?dist}
Summary:        A program for making font samples that show Unicode coverage of the font
License:        GPL-3.0-or-later
URL:            https://github.com/eugmes/fntsample/releases
Source0:        https://github.com/eugmes/fntsample/archive/release/%{version}/%{name}-%{version}.tar.gz
Requires:       perl(Locale::TextDomain)
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  pango-devel
BuildRequires:  perl-generators
BuildRequires:  unicode-ucd
# /oreon:deps
%description
A program for making font samples that show Unicode coverage of
the font and are similar in appearance to Unicode charts.
Samples can be saved as PDF or PostScript files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-release-%{version}
%oreon_prep
%build

%cmake -DUNICODE_BLOCKS=%{_datadir}/unicode/ucd/Blocks.txt
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

ctest -V %{?_smp_flags}
%find_lang %{name}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
